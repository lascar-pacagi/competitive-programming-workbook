# A. Cyclic Agreement

Two circular sensor rings are encoded by strings `s` and `t` of equal length
over `A`, `C`, `G`, and `T`. For a shift `r`, compare `s[i]` with
`t[(i+r) mod n]` for every zero-based index `i`.

Find the maximum number of equal positions and the smallest shift attaining
that maximum.

## Input

```text
n
s
t
```

- `1 <= n <= 100000`
- both strings have length `n`
- every character belongs to `ACGT`

## Output

Print `best smallest_shift`.

## Sample

```text
4
ACGT
CGTA
```

```text
4 3
```
