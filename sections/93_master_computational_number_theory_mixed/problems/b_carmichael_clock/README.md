# Carmichael Clock

For each positive `n < 2^64`, print the Carmichael value `lambda(n)`, the smallest positive `L` such that `a^L = 1 (mod n)` for every `a` coprime to `n`. Define `lambda(1)=1`. At most 200 queries.

Sample input
```text
3
1
8
15
```
Sample output
```text
1
2
4
```
