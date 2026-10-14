# Task 5 — Asymptotic Analysis
| Algorithm | Preprocessing | Lookup | q lookups after preprocessing | Auxiliary space |
|---|---|---|---|---|
| Linear | Θ(1) | Θ(n) | Θ(qn) | Θ(1) |
| Recursive binary | Θ(n log n) to sort | Θ(log n) | Θ(n log n + q log n) | Θ(log n) recursion plus sorting space as implementation-dependent |
| Hash table | Expected Θ(n) | Expected Θ(1), worst O(n) | Expected Θ(n+q); worst O(n+qn) | Θ(n) |

Notation: O is an asymptotic upper bound; Ω is a lower bound; Θ is a tight asymptotic bound. Bounds ignore constant factors and machine-specific timing effects.
