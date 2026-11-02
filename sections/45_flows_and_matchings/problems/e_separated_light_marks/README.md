# E. Separated Light Marks

A gallery floor is an `h` by `w` grid. A `.` is a floor cell and a `#` is an
opaque partition. You may put at most one light mark on any floor cell.

A mark emits a signal horizontally and vertically until a partition or the
edge of the grid stops it. Two marks interfere if they lie in the same row
or column with no partition strictly between them. Diagonal signals do not
exist. Partitions block signals completely; empty floor cells do not.

Find the largest number of marks that can be placed without interference.

## Input

```text
h w
row1
...
rowh
```

- `1 <= h, w <= 60`.
- Each row has exactly `w` characters, all `.` or `#`.
- The grid may have no floor cells.

## Output

Print the maximum number of marks.

## Sample

```text
3 3
.#.
###
.#.
```

```text
4
```

All four floor cells are separated horizontally and vertically by partitions,
so all four may contain marks, even though some share a grid row or column.
