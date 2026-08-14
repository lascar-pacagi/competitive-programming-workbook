# Offline companion: 520B -- Two Buttons (1400)

This is an original, locally judgeable companion for [520B -- Two Buttons (1400)](https://codeforces.com/problemset/problem/520/B). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


For each test case, split an array between two adjacent elements. Both parts
must be nonempty. Print the smallest possible absolute difference between the
sum of the left part and the sum of the right part, followed by the smallest
split position that achieves it. A split position `p` means the left part is
the **inclusive** range of positions `1` through `p`, and the right part is the
**inclusive** range `p + 1` through `n`. Therefore `p` can range only from `1`
to `n - 1`: both parts must contain at least one element.

## Input

```text
T
n
a1 a2 ... an
...
```

`1 <= T <= 100`, `2 <= n <= 200000`, the total `n` is at most `200000`, and
`|ai| <= 10^9`.

## Output

Print `minimum_difference position` for each test case.

## Sample

```text
2
5
3 1 4 1 5
4
1 2 2 1
```

```text
2 3
0 2
```
