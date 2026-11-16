# D&C Closest Pair
```text
sort points by x; if <=3 use brute force
split at median x; recurse on both halves; d=min(dLeft,dRight)
form strip |x-midX|<d; sort strip by y
compare only following points with y-gap<d; return best pair
```
T(n)=2T(n/2)+Θ(n)=Θ(n log n), compared with brute force Θ(n²).
