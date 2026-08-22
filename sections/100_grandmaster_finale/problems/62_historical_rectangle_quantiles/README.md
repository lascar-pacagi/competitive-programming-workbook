# Historical Rectangle Quantiles

CDQ lifetime ordering and Fenwick rollback are the historical counting kernel used inside parallel value search.

`n` records arrive in order. Record `i` has coordinates `(x[i],y[i])` and a
positive reward `w[i]`.

Choose a nonempty subsequence of record indices

```text
i1 < i2 < ... < ik
```

such that both coordinates increase strictly:

```text
x[i1] < x[i2] < ... < x[ik]
y[i1] < y[i2] < ... < y[ik].
```

The score is the sum of selected rewards. Output the maximum score and the
number of different index subsequences attaining it, modulo `1,000,000,007`.
Records with identical coordinates remain different records.

## Input

```text
n
x[1] y[1] w[1]
...
x[n] y[n] w[n]
```

- `1 <= n <= 100000`
- `|x[i]|,|y[i]| <= 10^9`
- `1 <= w[i] <= 10^9`
- the maximum score fits in a signed 64-bit integer.

## Output

Print `maximum_score number_of_optimal_subsequences`.

## Sample input

```text
4
1 1 5
2 3 4
2 2 4
3 4 1
```

## Sample output

```text
10 2
```

The two optimal subsequences use indices `(1,2,4)` and `(1,3,4)`.
