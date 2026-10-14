# Task 7 — Recurrence Solution (Expansion)
T(n)=T(n/2)+c
= T(n/4)+2c
= T(n/8)+3c
= T(n/2ᵏ)+kc.

The recursion stops when n/2ᵏ ≤ 1, hence 2ᵏ ≥ n and k ≥ log₂n. The number of levels is Θ(log n). The base-case cost is constant, so T(n)=Θ(log n). The recursion depth and stack usage are also Θ(log n).
