# Versioned Convex DP

Version `0` contains the line `y=0`, whose identifier is `0`. Each of the next
`q` operations creates a new version `i` from an earlier version `p`.

- `p A m b`: version `i` contains all lines of version `p` and additionally
  the line `y=m*x+b`. Its identifier is `i`.
- `p Q x`: version `i` contains exactly the lines of version `p`. Among them,
  find the minimum value at coordinate `x` and the identifier of a line
  attaining it.

If several lines attain the minimum, output the smallest identifier.
Branching versions are independent: a line belongs only to descendants of the
version where it was added.

## Input

```text
q
q operations
```

- `1 <= q <= 200000`
- `0 <= p < i`
- `|m|,|b|,|x| <= 10^9`
- every evaluated value fits in a signed 64-bit integer.

## Output

For every query operation, print `minimum line_identifier`.

## Sample input

```text
6
0 A 2 3
1 Q -4
0 A -1 5
3 Q 10
1 A -3 20
5 Q 10
```

## Sample output

```text
-5 1
-5 3
-10 5
```

The sample deliberately shows that lines from the two branches do not leak
into one another.
