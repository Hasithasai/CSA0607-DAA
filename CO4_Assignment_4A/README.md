# CSA06 – Design and Analysis of Algorithms
## Assignment 4A (CO4) – Algorithmic Design through Pseudocode

Individual assignment: Greedy and Dynamic Programming design, pseudocode, traces and verification programs (Python 3, standard library only).

| Task | Topic | Program |
|------|-------|---------|
| 1 | Repair of poor pseudocode – fractional knapsack (greedy) | `Source_Code/Task_1/task1_fractional_knapsack.py` |
| 2 | Job sequencing with deadlines (greedy) | `Source_Code/Task_2/task2_job_sequencing.py` |
| 3 | 0/1 knapsack (dynamic programming, with reconstruction) | `Source_Code/Task_3/task3_knapsack_dp.py` |
| 4 | WordBreak defect, failing input and repair | `Source_Code/Task_4/task4_wordbreak.py` |
| 5 | Dijkstra, Bellman-Ford, Floyd-Warshall | `Source_Code/Task_5/task5_shortest_paths.py` |
| 6 | Design challenge – energy-aware job scheduling (DP) | `Source_Code/Task_6/task6_energy_scheduling.py` |

## Run
```
cd Source_Code/Task_N
python3 taskN_*.py
```
Each program prints its trace and ends with `All Task N tests passed.` (assertions check the results). The output of the last run is stored in `Source_Code/Task_N/output.txt`.

## Report
`Report/CO4_Assignment_4A_Report.pdf` – problem analysis, pseudocode, manual traces, test cases, results and source listing for all six tasks.

## Results
- Task 1: capacity 50 → value 240
- Task 2: schedule C, A, D → profit 180 (B changed to 90 → B, A, D → 210)
- Task 3: capacity 7 → items Q, R → value 45
- Task 4: "abcd" with {"cd"} breaks the original (DP[4]); fix is `DP[j] = TRUE AND ...`
- Task 5: shortest distance A→E = 10; negative edge breaks Dijkstra; Bellman-Ford detects negative cycles
- Task 6: J2, J5, J7, J8 → 200; adversarial set: DP 110 vs greedy 90
