# Max-Min D&C
```text
MAXMIN(A,l,r)
 if l=r return (A[l],A[l])
 if r=l+1 compare and return (smaller,larger)
 m=floor((l+r)/2)
 (mnL,mxL)=MAXMIN(A,l,m)
 (mnR,mxR)=MAXMIN(A,m+1,r)
 return (min(mnL,mnR),max(mxL,mxR))
```
Recurrence T(n)=2T(n/2)+2; tournament comparisons about 3n/2−2 for powers of two, versus 2n−2 for separate scans.
