# Binary Search
```text
low=0; high=n-1
while low<=high:
 mid=floor((low+high)/2)
 if A[mid]==key return mid
 if A[mid]<key low=mid+1 else high=mid-1
return NOT_FOUND
```
Sorted order proves the discarded half cannot contain the key. T(n)=T(n/2)+Θ(1)=Θ(log n).
