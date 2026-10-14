# Task 4 — Best, Average, Worst Case
| Algorithm | Best lookup | Average/expected lookup | Worst lookup | Conditions |
|---|---:|---:|---:|---|
| Linear | Θ(1) | Θ(n) | Θ(n) | Best: first element; worst: last/missing |
| Recursive binary | Θ(1) | Θ(log n) | Θ(log n) | Input must be sorted; best: midpoint hit |
| Hash table | Θ(1) expected | Θ(1) expected | O(n) | Expected bound assumes reasonable hashing/load factor |

For binary search on an unsorted input, sorting must be included in end-to-end cost. For a single query, sorting may outweigh lookup savings; for repeated queries, the preprocessing cost can be amortized.
