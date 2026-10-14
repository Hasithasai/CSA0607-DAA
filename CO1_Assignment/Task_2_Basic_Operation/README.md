# Task 2 — Basic Operation
- **Linear search:** key-to-array-element equality comparison. A successful query at zero-based index k performs k+1 comparisons; a miss performs n.
- **Recursive binary search:** comparison of key to the midpoint element. The code increments one comparison per recursive level (one equality test; branch direction follows if unequal). Some textbooks count both equality and ordering tests separately; state the convention consistently.
- **Hash table:** membership operation `contains(key)`. Java `HashSet` does not expose its internal key-comparison count; count API calls, and do not present these as internal comparisons.
- **Other measurements:** preprocessing/build time, lookup time, total time, correctness verification, query count, memory footprint if available.
