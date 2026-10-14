# CO1 Assignment — Student Registration Number Search

**Course:** CSA06 — Design and Analysis of Algorithms (CO1)  
**Language:** Java  
**Algorithms:** Linear Search, Recursive Binary Search, Hash Table Search

## Problem
Design, implement, test, and analyse exact lookup of unique student registration numbers for datasets of 1,000, 10,000, 100,000, and 1,000,000 records. The design challenge is 50,000 search requests/hour and daily additions.

## Repository structure

- `Task_1_Algorithm_Design/` — algorithm descriptions and pseudocode
- `Task_2_Basic_Operation/` — comparison/basic-operation definitions
- `Task_3_Mathematical_Complexity/` — mathematical derivations
- `Task_4_Case_Analysis/` — best, average, and worst cases
- `Task_5_Asymptotic_Analysis/` — Big-O, Theta, and Omega analysis
- `Task_6_Recurrence_Formulation/` — recursive binary-search recurrence
- `Task_7_Recurrence_Solution/` — expansion and recurrence solution
- `Task_8_Implementation_Testing/Source_Code/` — Java benchmark implementation
- `Task_9_Experimental_Performance/` — benchmark methodology/results
- `Task_10_Theory_vs_Experiment/` — interpretation of measured results
- `Task_11_Final_Recommendation/` — recommended production approach
- `Task_12_Design_Challenge/` — capacity reasoning for 50,000 requests/hour
- `Report/` — analysis, graphs, evidence folders, and documentation

## Run the Java benchmark

Requires JDK 11 or newer (tested design targets modern Java; use JDK 21 if available).

```bash
cd Task_8_Implementation_Testing/Source_Code
javac SearchBenchmark.java
java SearchBenchmark 1000
```

The program writes `benchmark_results.csv` in the current directory. It tests 1,000 requests per dataset by default, with 50% hits and 50% misses. The seed is fixed to make query generation reproducible. Search correctness is checked and reported. Run multiple times on the target machine and report median/percentile measurements for a stronger experiment.

## Important measurement notes

- The CSV included in `Report/Documentation/` is the single-run dataset transcribed from the supplied assignment report; it is not a universal performance guarantee.
- Re-run the code on your own machine and replace or supplement those results with your own genuine output before submission.
- HashSet's internal key comparisons are not exposed by Java's public API, so the program records membership calls, not a fabricated hash comparison count.
- The screenshot directories intentionally contain instructions, not fabricated screenshots. Capture real IDE/terminal screenshots after running the code if screenshots are required.
- The benchmark is an in-memory microbenchmark. It does not model database/network latency, concurrent load, durable writes, or crash recovery.
