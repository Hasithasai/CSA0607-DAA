# Task 6 — Recurrence Formulation
Recursive binary search reduces the search interval from n to approximately n/2 and performs constant work for midpoint calculation and comparisons.

T(n) = T(⌊n/2⌋) + c, for n > 1; T(0)=d₀ and T(1)=d₁, where c,d₀,d₁ are constants. The floor does not change the asymptotic result. This recurrence assumes a sorted array and one recursive branch per call.
