# Median of Medians
Group into fives; sort groups and take medians; recursively select median of medians; partition around pivot; recurse only into rank-containing partition. Worst-case T(n)≤T(n/5)+T(7n/10)+Θ(n)=Θ(n).
