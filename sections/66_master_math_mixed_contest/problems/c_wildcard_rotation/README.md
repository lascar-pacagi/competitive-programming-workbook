# C. Wildcard Rotation

Strings `s` and `t` have equal length and use `A`, `C`, `G`, `T`, and `?`.
A question mark is compatible with every character. A concrete character is
compatible only with itself or a question mark.

For shift `r`, compare `s[i]` with `t[(i+r) mod n]`. Count the shifts for which
all `n` positions are compatible, and print the smallest such shift.

## Input

```text
n
s
t
```

- `1 <= n <= 60000`

## Output

Print `count smallest_shift`. If no shift is valid, print `0 -1`.

## Sample

```text
4
A?GT
GTAC
```

```text
1 2
```
