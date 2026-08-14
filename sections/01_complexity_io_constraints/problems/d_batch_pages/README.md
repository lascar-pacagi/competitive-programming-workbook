# D. Batch Pages

For each query, a print job has `n` records. A page holds exactly `k` records.
Pages are filled in order; the last page may be partially filled.

Print two integers: the number of pages used and the number of empty record
slots on the final page. When `n = 0`, use zero pages and zero empty slots.

## Input

```text
Q
n1 k1
n2 k2
...
```

`1 <= Q <= 200000`, `0 <= n <= 10^18`, and `1 <= k <= 10^18`.

## Output

Print one `pages empty_slots` pair per query.

## Sample

```text
4
0 7
7 7
8 7
25 6
```

Output:

```text
0 0
1 0
2 6
5 5
```
