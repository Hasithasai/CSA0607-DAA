# Task 1 — Algorithm Design
## Problem
Given a collection of unique student registration numbers and a query key, return its position/presence or report that it is absent.

### Approach A: Linear search
Inspect each ID from the first record onward until a match is found or the array ends.
```text
LINEAR-SEARCH(A, key)
  for i = 0 to length(A)-1
    if A[i] == key: return i
  return NOT_FOUND
```
Time: best Θ(1), average Θ(n), worst Θ(n). Extra space Θ(1). No preprocessing.

### Approach B: Recursive binary search
Requires sorted data. Compare with the middle element and recurse into only the half that can contain the key.
```text
BINARY-SEARCH(A, key, low, high)
  if low > high: return NOT_FOUND
  mid = low + floor((high-low)/2)
  if A[mid] == key: return mid
  if key < A[mid]: return BINARY-SEARCH(A,key,low,mid-1)
  return BINARY-SEARCH(A,key,mid+1,high)
```
Lookup Θ(log n); sorting unsorted input costs Θ(n log n). Recursion stack Θ(log n).

### Approach C: Hash-table search
Build a hash-based set/index of IDs, then test membership for each key.
```text
BUILD-HASH-INDEX(A)
  H = empty hash set
  for id in A: H.add(id)
  return H
HASH-SEARCH(H,key)
  return H.contains(key)
```
Expected build Θ(n), expected lookup Θ(1), worst-case lookup O(n) under pathological collisions. Space Θ(n).

### Flow summary
Input IDs → validate uniqueness → (sort for binary / build hash index for hash) → issue query → return found/not found → verify result.
