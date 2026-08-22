# D. Weighted Bounded Isotonic

For every position `i`, you are given an integer target `a[i]` and a positive
weight `w[i]`. Choose integers

```text
L <= b[1] <= b[2] <= ... <= b[n] <= R
```

minimizing

```text
sum w[i] * |b[i] - a[i]|.
```

Print the minimum cost.

Input consists of `n L R`, followed by `n` lines `a[i] w[i]`.

Constraints: `1 <= n <= 200000`, `-10^9 <= L <= R <= 10^9`,
`|a[i]| <= 10^9`, and `1 <= w[i] <= 10^9`. The answer can exceed signed
64-bit range.

Sample input:

```text
4 0 10
8 2
3 1
12 3
7 2
```

Sample output:

```text
17
```
