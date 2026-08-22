# A. Branching Multiset

Version `0` is an empty multiset of integers from `1..M`. Process operations:

- `I v x`: create the next version by inserting one `x` into version `v`;
- `E v x`: create the next version by erasing one `x` from version `v`;
- `K v k`: print the k-th smallest value in version `v`;
- `C v x`: print how many values in version `v` are at most `x`.

Only update operations create versions, numbered `1,2,...` in update order.
Every erase and k-th query is guaranteed valid. Versions may branch.

## Input

```text
M q
q operations
```

`1 <= M,q <= 200000`.

## Sample

```text
8 7
I 0 5
I 1 2
I 1 7
K 2 1
C 3 6
E 2 5
K 4 1
```

```text
2
1
2
```
