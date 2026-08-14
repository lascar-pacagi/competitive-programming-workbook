# R. Coverage Patches

You are given `n` positive integers and a target `T`. You may add any positive
integers to the collection. Every integer from `1` through `T` must be
representable as the sum of some subset of the final collection, using each
element at most once.

Print the minimum number of integers that must be added.

## Input

```text
n T
a1 a2 ... an
```

`0 <= n <= 200000`, `1 <= T <= 10^18`, and
`1 <= a_i <= 10^18`. The input integers are not necessarily sorted. When
`n = 0`, the second input line is empty and may be omitted.

## Output

Print the minimum number of added integers.

## Sample Input

```text
3 20
1 5 10
```

## Sample Output

```text
2
```
