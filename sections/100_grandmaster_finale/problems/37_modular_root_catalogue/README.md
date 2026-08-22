# Modular Root Catalogue

Primitive-root coordinates turn the power constraint into a linear congruence and return its smallest root exponent.

For odd prime `p <= 10^12`, let `g` be its smallest primitive root. Given `k > 0` and `a` in `[1,p)`, print the smallest `y >= 0` satisfying `(g^y)^k = a (mod p)`, or `-1`. At most 50 queries.

Sample input
```text
2
7 2 2
7 2 3
```
Sample output
```text
1
-1
```
