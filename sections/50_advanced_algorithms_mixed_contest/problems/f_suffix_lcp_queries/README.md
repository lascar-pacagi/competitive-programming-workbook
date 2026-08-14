# F. Suffix LCP Queries

For each pair of positions `(i,j)` in a lowercase string, print the longest
common prefix length of suffixes `s[i..]` and `s[j..]`.

## Input
```text
s
q
i j
...
```
Positions are 1-based. `|s|,q <= 200000`.

## Sample
```text
banana
3
2 4
1 3
3 5
```
```text
3
0
2
```
