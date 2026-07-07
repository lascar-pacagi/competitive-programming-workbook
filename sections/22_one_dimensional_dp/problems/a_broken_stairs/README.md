# A. Broken Stairs

You are standing before step `0` and want to reach step `n`. In one move you
may climb either `1` or `2` steps. Some steps are broken, and you may not land
on a broken step.

Count the number of valid ways to reach step `n`, modulo `1_000_000_007`.

## Input

```text
n b
x1 x2 ... xb
```

`1 <= n <= 2 * 10^5`, `0 <= b <= n`, and the broken step numbers are distinct.

If `b = 0`, the third line is omitted.

## Output

Print the number of valid ways.

## Sample

Input:

```text
5 1
3
```

Output:

```text
2
```

