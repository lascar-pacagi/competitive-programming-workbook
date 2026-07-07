# C. Possible Sums

You are given `n` positive integers. Each integer may be used at most once.

Print all positive sums that can be formed by choosing a subset of the numbers.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 100`, `1 <= ai <= 1000`, and `sum(ai) <= 100000`.

## Output

First print the number of positive reachable sums. On the next line, print the
reachable sums in increasing order. If there are no positive reachable sums,
the second line may be empty.

## Sample

Input:

```text
4
4 2 5 2
```

Output:

```text
9
2 4 5 6 7 8 9 11 13
```

