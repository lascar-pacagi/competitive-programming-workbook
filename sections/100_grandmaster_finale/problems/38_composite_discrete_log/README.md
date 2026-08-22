# Composite Discrete Log

GCD reduction extends baby-step--giant-step to composite, non-coprime instances.

For each `1 <= a,b < m <= 10^12`, print the smallest `x >= 0` with `a^x = b (mod m)`, or `-1`. The base need not be coprime to the modulus. At most 100 queries.

Sample input
```text
3
2 8 12
4 2 14
3 5 7
```
Sample output
```text
3
2
5
```
