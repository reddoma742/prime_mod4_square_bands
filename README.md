# Differential Behaviour of Primes ≡1 and ≡3 (mod 4) Within Square-Layer Bands

**Repository for Paper 2** — Berramdane Reddouane, Independent Researcher (reddoma@gmail.com)

> ⚠️ **Working title / draft status.** This README assumes Paper 2 formalises the mod-4
> differential analysis first introduced as an exploratory appendix in Paper 1
> ("A Geometric Sieve for Composite Detection...", §5, Appendix A) and referenced again
> in Paper 3. Edit the title, abstract, and status table below once the paper text is finalised.

---

## Abstract (draft placeholder)

Building on the square-layer framework $L_m = [m^2,(m+1)^2)$ introduced in [Paper 1], we
present a systematic study of the differential behaviour of primes congruent to 1 and 3
modulo 4 within square-layer bands. Across multiple independent analyses — band-position
scans, symmetry profiles, heatmaps, direct pairwise comparisons, side-of-band comparisons,
and a unified multi-dimensional score — we consistently observe a small but persistent gap
between the two residue classes, with the $4k{+}1$ class showing a slightly higher
representation/ratio statistic than the $4k{+}3$ class across nearly all tested dimensions.
This paper elevates the exploratory observations of Paper 1 (§5) into a dedicated,
multi-angle empirical study, while explicitly preserving the heuristic (non-theorem) status
of the central claim.

*(Replace this abstract with the final text once the paper is written; keep the "Status"
table in §Companion Papers accurate.)*

---

## Companion Papers

| # | Title | Repository | Status |
|---|---|---|---|
| 1 | A Geometric Sieve for Composite Detection and an Empirical Constant in Prime Representations | `reddouane_2026_geometric-sieve` | Published/drafted |
| 2 | **This paper** — Differential Behaviour of 4k+1 vs 4k+3 Primes in Square Bands | `reddouane_2026_mod4-differential` (this repo) | Draft |
| 3 | Geometric and Arithmetic Properties of the $n=2a\pm b$ Representation Network | `reddouane_2026_representation-network` | Drafted |
| 4 | The Immunity Index: A Local Explanation of Prime Density Fluctuations Near Square Layers | `reddouane_2026_immunity-index` | Drafted |

See the meta-repository `reddouane-research-index` for the full map of this research programme.

---

## Repository Structure

```
reddouane_2026_mod4-differential/
├── README.md                  ← this file
├── LICENSE                    ← MIT licence (code)
├── LICENSE-DATA                ← CC-BY-4.0 licence (data/figures)
├── CITATION.cff                ← machine-readable citation metadata
├── requirements.txt             ← Python dependencies to reproduce results
├── .gitignore
├── paper/
│   └── paper2_draft.md          ← manuscript source (add final PDF/tex here too)
├── src/
│   ├── band_scan.py              ← generates odd_vs_prime_* and mod4_prime_band_* files
│   ├── direct_compare.py         ← generates mod4_direct_compare_* files
│   ├── side_compare.py           ← generates mod4_side_* files
│   ├── unified_score.py          ← generates mod4_unified_* files
│   └── utils.py                  ← shared helpers (is_prime, get_layer, band_position)
├── data/
│   ├── band_scan/
│   │   ├── odd_vs_prime_band_summary.csv
│   │   ├── odd_vs_prime_band_symmetry.csv
│   │   ├── odd_vs_prime_band_symmetry_overall.csv
│   │   ├── odd_vs_prime_band_symmetry_summary.csv
│   │   ├── odd_vs_prime_heatmap_prime.csv
│   │   └── odd_vs_prime_scan_band.csv
│   ├── mod4_band/
│   │   ├── mod4_prime_band_scan.csv
│   │   ├── mod4_prime_band_slope.csv
│   │   ├── mod4_prime_band_summary.csv
│   │   ├── mod4_prime_band_symmetry.csv
│   │   ├── mod4_prime_band_symmetry_overall.csv
│   │   ├── mod4_heatmap_prime_4k1.csv
│   │   ├── mod4_heatmap_prime_4k3.csv
│   │   └── mod4_heatmap_composite.csv
│   ├── direct_compare/
│   │   ├── mod4_direct_compare_scan.csv
│   │   ├── mod4_direct_compare_by_t.csv
│   │   ├── mod4_direct_compare_by_dist.csv
│   │   ├── mod4_direct_compare_delta_heatmap.csv
│   │   └── mod4_direct_compare_zone_summary.csv
│   ├── side_compare/
│   │   ├── mod4_side_scan.csv
│   │   ├── mod4_side_by_dist.csv
│   │   ├── mod4_side_summary.csv
│   │   ├── mod4_side_zone_summary.csv
│   │   └── mod4_side_compare.csv
│   └── unified/
│       ├── mod4_unified_scan.csv
│       ├── mod4_unified_compare.csv
│       └── mod4_unified_dimension_summary.csv
└── figures/
    ├── mod4_prime_band_scan.jpeg
    ├── mod4_direct_compare.jpeg
    ├── mod4_side_compare.jpeg
    └── mod4_unified_compare.jpeg
```

---

## Reproducing the Results

```bash
git clone https://github.com/reddoma/reddouane_2026_mod4-differential.git
cd reddouane_2026_mod4-differential
pip install -r requirements.txt

python src/band_scan.py         # → data/band_scan/, data/mod4_band/
python src/direct_compare.py    # → data/direct_compare/
python src/side_compare.py      # → data/side_compare/
python src/unified_score.py     # → data/unified/, figures/
```

Each script should read its parameters (scale range, band-position bins, etc.) from
constants at the top of the file, matching the values reported in the paper's tables.

---

## Status of Claims

Following the rigour convention established in Papers 1 and 3, all claims in this
repository/paper are **heuristic and exploratory**, not theorems, unless explicitly
labelled otherwise in `paper/paper2_draft.md`. Effect sizes observed here are small
(see the unified score $U \approx 0.048$ reported in Paper 1 §5.3) and have not been
tested against a rigorous null model with formal confidence intervals.

---

## Data and Code Availability

All code and data used in this paper are available in this repository. Raw CSV outputs
in `data/` were generated by the scripts in `src/`; regenerate them locally to verify
reproducibility rather than treating the committed CSVs as ground truth for future edits.

## Acknowledgments

This work was developed through an iterative human-led research process supported by
AI-assisted research tools used for methodological review, code debugging, and manuscript
structuring. All AI-assisted contributions were directed, reviewed, and validated by the
human author, who bears full responsibility for the content of this repository and paper.

## License

- Code: MIT License (see `LICENSE`)
- Data and figures: CC-BY 4.0 (see `LICENSE-DATA`)

## Citation

See `CITATION.cff`. Please cite the paper (once finalised) rather than this repository
alone when referencing the scientific results.
