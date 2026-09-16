# F. Mutable Priority Queue

Maintain a collection of tasks. Each task has a unique integer identifier and
an integer priority.

## Input

The first line contains the number of operations `q`. Each operation has one
of these forms:

- `A id priority`: add a task whose identifier is not currently present.
- `U id priority`: change the priority of a task that is currently present.
- `P`: remove and print the identifier of the task with greatest priority.

If several tasks have the greatest priority, remove the one with the smallest
identifier. If the collection is empty, `P` prints `-1` and changes nothing.

The input guarantees that every `A` and `U` operation is valid. An identifier
removed by `P` may be added again later.

## Output

For every `P` operation, print the requested identifier or `-1`.

## Constraints

- `1 <= q <= 200000`
- `1 <= id <= 10^9`
- `-10^9 <= priority <= 10^9`

## Sample

```text
9
A 10 5
A 3 5
P
A 7 2
U 10 1
P
U 10 9
P
P
```

```text
3
7
10
-1
```
