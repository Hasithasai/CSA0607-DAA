# Maximum Subarray Sum D&C
```text
if one item return it
split at midpoint; recursively get best-left and best-right
scan leftwards from midpoint for best suffix
scan rightwards for best prefix
return maximum of left, right, suffix+prefix
```
Every optimal interval lies left, right, or crosses midpoint. T(n)=2T(n/2)+Θ(n)=Θ(n log n), brute force Θ(n²).
