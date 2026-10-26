# N. Archive Reassembly

An archive contains one source string `s`. A machine can copy any nonempty
contiguous substring of `s`. Copies are unlimited: they may overlap in the
source, use the same source positions repeatedly, and be chosen in any order.

Produce a target string `t` by concatenating copied pieces without inserting,
deleting, or changing any letters. Find the smallest number of pieces needed,
or determine that producing `t` is impossible. The target need not occur as one
contiguous substring of the source.

## Input

The first line contains `s`. The second line contains `t`.

- `1 <= |s|, |t| <= 200000`.
- Both strings contain only lowercase English letters.

## Output

Print the minimum number of copied pieces, or `-1` if no construction exists.

## Sample

Input:

```text
abac
acaba
```

Output:

```text
2
```

Copy `ac` from source positions `3..4`, then `aba` from positions `1..3`.
The target itself is not a substring of `abac`, so one piece cannot suffice.
