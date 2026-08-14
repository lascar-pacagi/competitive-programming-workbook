# J. Target LCM Subsets

Given `n` positive integers and a target `T`, count the nonempty index subsets
whose least common multiple is exactly `T`.

Equal values at different indices are distinct choices. Print the answer
modulo `1000000007`.

## Input

```text
n T
a[1] a[2] ... a[n]
```

`1 <= n <= 200000`, `1 <= a[i],T <= 10^9`.

## Output

Print the required subset count.

## Sample

```text
5 12
2 3 4 6 12
```

```text
22
```
