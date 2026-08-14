# B. Build Timeline

There are `n` modules. Module `i` takes `time[i]` days. A dependency `a b`
means module `a` must finish before module `b` can start.

For each queried module, print its earliest finish day. If the dependencies
contain a cycle, print `IMPOSSIBLE`.

## Input

```text
n m q
t1 t2 ... tn
a1 b1
...
am bm
x1 x2 ... xq
```

The integer constraints are:

- `1 <= n, q <= 2 * 10^5`;
- `0 <= m <= 2 * 10^5`;
- `1 <= t_i <= 10^9`;
- `1 <= a_j, b_j <= n` for every dependency;
- `1 <= x_j <= n` for every query.

When the graph is acyclic, every earliest finish day is at most
`n * 10^9 <= 2 * 10^14`, so it must be stored in a signed 64-bit integer.

## Output

Print `IMPOSSIBLE`, or print `q` integers.

## Sample

Input:

```text
5 5 3
3 2 4 6 1
1 3
2 3
3 4
2 5
5 4
3 4 5
```

Output:

```text
7 13 3
```
