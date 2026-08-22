# Subset Partition Spectrum

The full mask spectrum is one ranked/disjoint subset-convolution layer.

Given functions `f,g` on all subsets of a `k`-element universe, print subset convolution `h[S]=sum_{A subset S} f[A]*g[S\A]` where `A` and `S\A` are disjoint. `k <= 16`.

Sample input
```text
2
1 2 3 4
5 6 7 8
```
Sample output
```text
5 16 22 60
```
