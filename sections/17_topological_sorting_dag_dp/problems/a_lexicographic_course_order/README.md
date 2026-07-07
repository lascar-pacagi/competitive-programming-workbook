# A. Lexicographic Course Order

There are `n` courses and `m` prerequisite rules. A rule `a b` means course
`a` must be completed before course `b`.

Output the lexicographically smallest valid order of all courses. Among all
valid orders, this is the one whose first differing course number is as small
as possible.

If no valid order exists, print `IMPOSSIBLE`.

## Input

```text
n m
a1 b1
a2 b2
...
am bm
```

`1 <= n <= 2 * 10^5`  
`0 <= m <= 2 * 10^5`

## Output

Print either `IMPOSSIBLE` or one line with `n` integers: the lexicographically
smallest valid course order.

## Sample

Input:

```text
5 4
1 3
2 3
2 4
4 5
```

Output:

```text
1 2 3 4 5
```

