# Prime Discrete Log

For prime `p < 2^63` and integers `a,b` in `[0,p)`, print the smallest `x >= 0` satisfying `a^x = b (mod p)`, or `-1`. There are at most 100 queries and `p <= 10^12`.

Sample input
```text
2
13 2 8
7 3 5
```
Sample output
```text
3
5
```
