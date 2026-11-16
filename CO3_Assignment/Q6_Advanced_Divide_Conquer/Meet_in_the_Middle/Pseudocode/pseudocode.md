# Meet-in-the-Middle Subset Sum
Split values into L/R; enumerate all subset sums in each half; sort right sums; for each left sum binary-search target−leftSum; combine witness if found. About 2^(n/2) sums per half, Θ(2^(n/2)) storage; saves time relative to 2^n enumeration at memory cost.
