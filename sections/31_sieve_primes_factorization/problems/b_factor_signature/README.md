# B. Factor Signature

For each query `x`, print three values:

```text
number_of_distinct_prime_factors total_prime_factors_with_multiplicity largest_prime_factor
```

For `x = 1`, print `0 0 1`.

## Input

```text
q
x1
x2
...
xq
```

`1 <= q <= 200,000`, `1 <= x <= 1,000,000`.

## Output

Print one line per query.

## Sample

Input:

```text
4
1
12
97
360
```

Output:

```text
0 0 1
2 3 3
1 1 97
3 6 5
```
