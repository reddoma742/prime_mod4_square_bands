import os
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('output', exist_ok=True)

# Multi-scale replication study for mod-4 prime band signatures
# Scales: 25k, 50k, 100k, 250k

SCALES = [25_000, 50_000, 100_000, 250_000]
LIMIT = max(SCALES) + 100
MAX_DIST = 30
T_BINS = 10


def sieve(limit: int):
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            is_prime[i * i::i] = False
    return is_prime


is_prime = sieve(LIMIT)


def prime_or_one(x: int) -> bool:
    return x == 1 or (0 <= x < len(is_prime) and is_prime[x])


def features(n: int):
    k = int(math.isqrt(n))
    low_sq = k * k
    high_sq = (k + 1) * (k + 1)
    dist_low = n - low_sq
    dist_high = high_sq - n
    t = (n - low_sq) / (high_sq - low_sq)
    return low_sq, high_sq, dist_low, dist_high, min(dist_low, dist_high), t


scale_rows = []
full_rows = []

for N_MAX in SCALES:
    rows = []
    for n in range(3, N_MAX + 1, 2):
        if not is_prime[n]:
            continue
        low_sq, high_sq, dist_low, dist_high, nearest, t = features(n)
        minus = plus = 0
        for a in range(1, n):
            b = 2 * a - n
            if b >= 1 and is_prime[a] and prime_or_one(b):
                minus += 1
        for a in range(1, (n - 1) // 2 + 1):
            b = n - 2 * a
            if b >= 1 and is_prime[a] and prime_or_one(b):
                plus += 1
        scale = n / (math.log(max(n, 3)) ** 2)
        row = {
            'N_MAX': N_MAX,
            'n': n,
            'prime_class': 'prime_4k1' if n % 4 == 1 else 'prime_4k3',
            'sum_norm': (minus + plus) / scale,
            'diff_norm': (plus - minus) / scale,
            'ratio': (plus / minus) if minus > 0 else np.nan,
            'band_t': t,
            't_bin': min(int(t * T_BINS), T_BINS - 1),
            'nearest_square_dist': nearest,
            'dist_bin': min(nearest, MAX_DIST),
            'dist_low_square': dist_low,
            'dist_high_square': dist_high,
            'side_of_band': 'left_of_band' if dist_low <= dist_high else 'right_of_band',
            'near_low_flag': dist_low <= dist_high,
        }
        rows.append(row)
        full_rows.append(row)
    df = pd.DataFrame(rows)
    summary = df.groupby('prime_class', as_index=False).agg({
        'sum_norm': 'mean',
        'diff_norm': 'mean',
        'ratio': 'mean',
        'band_t': 'mean',
        'nearest_square_dist': 'mean',
        'n': 'count'
    }).rename(columns={'n': 'count'})
    if 'prime_4k1' in summary['prime_class'].values and 'prime_4k3' in summary['prime_class'].values:
        p1 = summary[summary['prime_class'] == 'prime_4k1'].iloc[0]
        p3 = summary[summary['prime_class'] == 'prime_4k3'].iloc[0]
        scale_rows.append({
            'N_MAX': N_MAX,
            'count_4k1': int(p1['count']),
            'count_4k3': int(p3['count']),
            'delta_sum_norm': float(p1['sum_norm'] - p3['sum_norm']),
            'delta_diff_norm': float(p1['diff_norm'] - p3['diff_norm']),
            'delta_ratio': float(p1['ratio'] - p3['ratio']),
            'ratio_4k1': float(p1['ratio']),
            'ratio_4k3': float(p3['ratio']),
        })

all_df = pd.DataFrame(full_rows)
all_df.to_csv('output/mod4_multiscale_scan.csv', index=False)
scale_df = pd.DataFrame(scale_rows)
scale_df.to_csv('output/mod4_multiscale_summary.csv', index=False)

# stability checks over t_bin and side_of_band by scale
stability_rows = []
for N_MAX in SCALES:
    sub = all_df[all_df['N_MAX'] == N_MAX]
    for dim in ['t_bin', 'side_of_band', 'near_low_flag']:
        tmp = sub.groupby([dim, 'prime_class'], as_index=False).agg({'ratio': 'mean'})
        for key, grp in tmp.groupby(dim):
            if len(grp) == 2:
                p1 = grp[grp['prime_class'] == 'prime_4k1']['ratio'].iloc[0]
                p3 = grp[grp['prime_class'] == 'prime_4k3']['ratio'].iloc[0]
                stability_rows.append({
                    'N_MAX': N_MAX,
                    'dimension': dim,
                    'bucket': key,
                    'delta_ratio': float(p1 - p3),
                })

stability_df = pd.DataFrame(stability_rows)
stability_df.to_csv('output/mod4_multiscale_stability.csv', index=False)

# Plot
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

axes[0,0].plot(scale_df['N_MAX'], scale_df['delta_ratio'], marker='o', color='black')
axes[0,0].set_title('Unified delta_ratio across scales')
axes[0,0].set_xlabel('N_MAX')
axes[0,0].set_ylabel('delta_ratio')
axes[0,0].grid(alpha=0.3)

axes[0,1].plot(scale_df['N_MAX'], scale_df['delta_sum_norm'], marker='o', color='blue')
axes[0,1].set_title('Unified delta_sum_norm across scales')
axes[0,1].set_xlabel('N_MAX')
axes[0,1].set_ylabel('delta_sum_norm')
axes[0,1].grid(alpha=0.3)

for dim, color in [('t_bin', 'red'), ('side_of_band', 'green'), ('near_low_flag', 'purple')]:
    sub = stability_df[(stability_df['dimension'] == dim) & (stability_df['N_MAX'] == SCALES[-1])]
    if len(sub):
        axes[1,0].plot(range(len(sub)), sub['delta_ratio'].values, marker='o', label=dim, color=color)
axes[1,0].set_title('Bucket delta_ratio at largest scale')
axes[1,0].set_ylabel('delta_ratio')
axes[1,0].grid(alpha=0.3)
axes[1,0].legend()

# side of band summary at largest scale
sub = all_df[all_df['N_MAX'] == SCALES[-1]]
side_sum = sub.groupby(['side_of_band', 'prime_class'], as_index=False).agg({'ratio': 'mean'})
for side in ['left_of_band', 'right_of_band']:
    grp = side_sum[side_sum['side_of_band'] == side]
    if len(grp) == 2:
        axes[1,1].bar([f'{side}\n4k1', f'{side}\n4k3'], grp['ratio'].values)
axes[1,1].set_title('Ratios by side at largest scale')
axes[1,1].grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('output/mod4_multiscale.png', dpi=180)
plt.show()

print('=== SCALE SUMMARY ===')
print(scale_df.to_string(index=False))
print('\n=== STABILITY HEAD ===')
print(stability_df.head(40).to_string(index=False))
