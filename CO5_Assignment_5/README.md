# CO5 Assignment 5 - Search, Complexity and Approximation Engineering

Backtracking, tractability (P / NP) and approximation algorithms. Python 3, standard library only (no installs needed).

## Layout
| Path | Content |
|---|---|
| `Report/CO5_Assignment_5_Report.pdf` | Consolidated report: Part A (A1-A5 pseudocode, traces, analysis) and Part B (B1-B4 results and interpretation) |
| `Source_Code/Task_B1_Graph_Colouring/` | `graph_colouring.py` (instrumented backtracking, 2 vertex orders), `test_graph_colouring.py`, `compare_orderings.py`, `trace_demo.py` + saved outputs |
| `Source_Code/Task_B2_Adversarial_Search/` | `adversarial.py` (same-size easy vs hard instance, growth table) + `adversarial_output.txt` |
| `Source_Code/Task_B3_Exact_vs_Approximation/` | `set_cover.py` (brute force, branch & bound, greedy), `run_experiments.py` + `experiment_output.txt` |
| `Source_Code/Task_B4_Bin_Packing/` | `bin_packing.py` (First-Fit / First-Fit Decreasing, exact solver), `run_experiments.py`, `exact_blowup_probe.py` + outputs |

## How to run
```
cd Source_Code/Task_B1_Graph_Colouring        && python3 test_graph_colouring.py && python3 compare_orderings.py && python3 trace_demo.py
cd ../Task_B2_Adversarial_Search              && python3 adversarial.py
cd ../Task_B3_Exact_vs_Approximation          && python3 run_experiments.py
cd ../Task_B4_Bin_Packing                     && python3 run_experiments.py && python3 exact_blowup_probe.py   # probe stops after 60 s by design
```
All randomised experiments use fixed seeds, so the counts are reproducible (timings vary by machine).

## Headline results
* B1: DSATUR-style ordering cuts search on hard "no" instances by 3x-250x (e.g. 17,752 -> 70 nodes); no change where nothing needs backtracking.
* B2: two isomorphic 14-vertex graphs, k=3: 16 nodes vs 130,636 nodes (8,165x) depending only on where the K4 appears in the order.
* B3: greedy set cover optimal on 3 of 7 scale instances, one centre more on the other 4; counterexample 3 vs 2 centres.
* B4: First-Fit Decreasing within 0.3% of the lower bound at 20,000 workloads; counterexample 4 vs 3 servers.
