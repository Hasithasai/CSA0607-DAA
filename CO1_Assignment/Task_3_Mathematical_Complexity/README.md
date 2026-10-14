# Task 3 — Mathematical Complexity
## Linear search
For a hit at position k (0-indexed), C(k)=k+1. For a miss, Cmiss(n)=n. If successful positions are equally likely, E[C|hit]=(1+2+…+n)/n=(n+1)/2. For hit probability p, E[C] = p(n+1)/2 + (1-p)n. With p=1/2, E[C]=(3n+1)/4 = Θ(n).

## Recursive binary search
At each level the active interval is halved and only constant work is performed: T(n)=T(⌊n/2⌋)+c for n>1; T(0 or 1)=d. After k levels, T(n)=T(⌊n/2^k⌋)+kc. Stop when n/2^k≤1, so k≥log₂n and k=Θ(log n); therefore T(n)=Θ(log n).

## Hash table
Building by n insertions is expected Θ(n) with controlled load factor and well-distributed hashes. A membership query is expected Θ(1), so q queries cost expected Θ(n+q) including construction. In the general collision worst case, a lookup may degrade to O(n), and q lookups to O(qn). These are expected/general bounds, not a guarantee for every implementation and workload.
