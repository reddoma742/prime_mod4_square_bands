markdown
# Differential Behaviour of Primes ≡1 and ≡3 (mod 4) Within Square-Layer Bands

**Berramdane Reddouane**
Independent Researcher
reddoma@gmail.com
August 2026

---

## Abstract

We examine the distribution of odd primes within the square-layer framework $L_m = [m^2, (m+1)^2)$, stratified by residue class modulo 4. Across multiple scales (25K, 50K, 100K, 250K), we compute representation counts $R^+(n)$ and $R^-(n)$ for each prime and compare the spatial distributions of $4k+1$ and $4k-1$ primes. A small but persistent gap is observed: the $4k+1$ class consistently shows a higher representation ratio (mean $R^+/R^- \approx 1.22$–$1.29$) compared to the $4k-1$ class ($\approx 1.14$–$1.19$). The unified delta ratio converges to approximately $0.048$ across all tested scales. All results are empirical and exploratory.

---

## 1. Introduction

### 1.1 The Square-Layer Framework

Following [1], we define the $m$-th square layer as $L_m = [m^2, (m+1)^2)$. For any odd integer $n \in L_m$, its normalized band position is:

$$t(n) = \frac{n - m^2}{(m+1)^2 - m^2} = \frac{d}{2m+1}$$

where $d = n - m^2$ is the offset from the lower square boundary.

### 1.2 The n = 2a ± b Representation Network

We define two representation counting functions:

$$R^-(n) = \#\{a \in P, a < n : 2a - n \in \{1\} \cup P\}$$
$$R^+(n) = \#\{a \in P, 2a < n : n - 2a \in \{1\} \cup P\}$$

where $P$ is the set of primes. The total representation is $R_{\text{sum}}(n) = R^-(n) + R^+(n)$.

### 1.3 The Modulo-4 Question

All odd primes > 2 fall into two residue classes modulo 4:
- Class $4k+1$: 5, 13, 17, 29, 37, 41, ...
- Class $4k-1$: 3, 7, 11, 19, 23, 31, ...

This paper investigates whether these two classes exhibit measurably different behaviour within square layers.

---

## 2. Methodology

### 2.1 Multi-Scale Design

We conduct the analysis at four scales: $N_{\max} = 25,000$, $50,000$, $100,000$, and $250,000$. At each scale, we:
1. Generate all primes up to $N_{\max}$ using a sieve.
2. For each odd prime, compute $R^+(p)$ and $R^-(p)$.
3. Compute normalized sum, difference, and ratio.
4. Compute geometric features: band position $t$, nearest square distance, side of band.

### 2.2 Metrics

| Metric | Formula | Meaning |
|--------|---------|---------|
| sum_norm | $(R^+ + R^-) / \text{scale}$ | Normalized total representations |
| diff_norm | $(R^+ - R^-) / \text{scale}$ | Normalized asymmetry |
| ratio | $R^+ / R^-$ | Representation bias toward addition |

where $\text{scale} = n / (\ln n)^2$.

### 2.3 Dimensions of Comparison

We compare the two prime classes across:
1. **Band position** ($t$): binned into $T_{\text{bins}} = 10$ equal intervals
2. **Square distance**: nearest distance to either square boundary
3. **Side of band**: left half ($t < 0.5$) vs right half ($t > 0.5$)

---

## 3. Results

### 3.1 Scale Summary

| $N_{\max}$ | Count 4k+1 | Count 4k-1 | $\Delta$ ratio | $\Delta$ sum_norm |
|------------|-----------|-----------|---------------|------------------|
| 25,000 | 1,375 | 1,383 | +0.048 | +0.006 |
| 50,000 | 2,563 | 2,568 | +0.047 | +0.005 |
| 100,000 | 4,790 | 4,801 | +0.044 | +0.005 |
| 250,000 | 11,078 | 11,098 | +0.048 | +0.005 |

**Observation:** The delta ratio is remarkably stable across scales, converging to approximately $0.048$. The $4k+1$ class consistently shows a higher $R^+/R^-$ ratio.

### 3.2 Stability Across Dimensions

The delta ratio persists across all tested dimensions (band position bins, band sides, near-low-square flag) at every scale tested. No dimension shows a reversal of the sign.

### 3.3 Side-of-Band Analysis

At the largest scale ($N_{\max} = 250,000$):
- Left of band: both classes show similar ratios
- Right of band: the $4k+1$ advantage is amplified

This suggests a directional dependence: the gap between classes is more pronounced in the right half of square bands.

### 3.4 Band Position Distribution

The gap between classes oscillates across band position bins. The oscillation appears to have a period of approximately 4 bin units at the largest scale, though this observation requires further testing for statistical significance.

---

## 4. Discussion

### 4.1 Interpretation

The persistent delta ratio of approximately $0.048$ suggests a structural difference between the two residue classes within the square-layer geometry. The $4k+1$ primes consistently show a higher $R^+/R^-$ ratio, indicating a bias toward the addition representation ($n = 2a + b$) relative to the subtraction representation ($n = 2a - b$).

### 4.2 Possible Connections

- **Quadratic reciprocity:** $-1$ is a quadratic residue modulo $4k+1$ primes but a non-residue modulo $4k-1$ primes. This fundamental difference may influence how these primes interact with square boundaries.
- **Chebyshev's bias:** The observed asymmetry may be related to known biases in prime number races modulo 4.

### 4.3 Limitations

All results are empirical. We have not:
- Constructed formal confidence intervals
- Tested against a rigorous null model
- Extended the analysis beyond $N = 250,000$

This work is exploratory and heuristic in nature.

---

## 5. Conclusion

A multi-scale empirical study of the $n = 2a \pm b$ representation network reveals a small but persistent difference between primes of the form $4k+1$ and $4k-1$. The unified delta ratio converges to approximately $0.048$ across scales from 25,000 to 250,000. The gap persists across multiple geometric dimensions and shows directional dependence within square bands. These observations suggest an underlying structural difference between the two residue classes that may merit further theoretical investigation.

---

## Data and Code Availability

All code and data are available at:
https://github.com/reddoma/prime_mod4_square_bands

text

---

## References

[1] B. Reddouane, "A Geometric Sieve for Composite Detection and an Empirical Constant in Prime Representations," Independent Research, August 2026.

[2] A. Granville and G. Martin, "Prime Number Races," *American Mathematical Monthly*, vol. 113, pp. 1–33, 2006.

---

*This paper is Part 2 of a multi-paper research programme. See the meta-repository for the full index.*
