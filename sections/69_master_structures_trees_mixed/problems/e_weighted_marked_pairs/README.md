# E. Weighted Marked Pairs

In a weighted tree, a query gives distinct marked vertices `vi`, each with a
positive coefficient `ci`. Print

```text
sum over i<j of ci * cj * distance(vi,vj).
```

## Input
```text
n q
n-1 weighted edges
for each query: k v1 c1 ... vk ck
```
The total `k` is at most `200000`; all answers fit signed 64-bit integers.

## Sample
```text
3 1
1 2 2
2 3 3
3 1 2 2 1 3 4
```
```text
56
```
