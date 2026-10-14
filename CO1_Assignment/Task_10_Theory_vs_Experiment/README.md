# Task 10 — Theory versus Experiment
- Linear comparison totals grow approximately linearly with n for a fixed query mix; observed timings rise sharply at one million records.
- Binary search performs logarithmic comparisons per query, and the recorded counts are far below linear search. Sorting/preprocessing must be included in end-to-end comparisons.
- Hash lookup has expected constant-time membership, but building the index costs time and memory. The million-record build cost is visible in the supplied run; repeated queries amortize that cost.
- Timings can be non-monotonic at small sizes because of JIT compilation, garbage collection, CPU scheduling, cache state, and timer resolution. Operation counts and asymptotic analysis are generally more stable than a single timing sample.
