# Merge Sort and Quick Sort
```text
MERGESORT(A): split into halves; recursively sort; merge sorted halves.
QUICKSORT(A): choose last item pivot; partition into <=pivot and >pivot; recursively sort both; concatenate.
```
Merge: T(n)=2T(n/2)+Θ(n)=Θ(n log n). Quick: T(k)+T(n−k−1)+Θ(n), balanced Θ(n log n), repeated 0:(n−1) splits Θ(n²).
