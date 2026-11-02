# F. Crate Routing

Depot `i` has `a[i]` indistinguishable crates. Destination `j` can receive
at most `b[j]` crates. A listed direct shipping lane from depot `i` to
destination `j` can carry at most `c` crates. Unlisted lanes cannot be used.
Crates cannot pass through another depot or destination.

You may leave crates at depots and destinations may receive less than their
limits. Choose a nonnegative integer amount for every listed lane, respecting
all depot stocks, destination limits, and lane limits. Maximize the total
number delivered.

## Input

```text
n m e
a1 ... an
b1 ... bm
u1 v1 c1
...
ue ve ce
```

- `1 <= n, m <= 150`, `0 <= e <= n*m`.
- `0 <= ai, bj, ck <= 10^9`.
- `1 <= uk <= n`, `1 <= vk <= m`.
- No depot-destination pair occurs twice.

## Output

Print the maximum number of crates delivered. Use a 64-bit integer.

## Sample

```text
2 2 3
3 2
2 3
1 1 2
1 2 2
2 1 2
```

```text
4
```

Send two crates from depot 1 to destination 2 and two from depot 2 to
destination 1. Although total stock and total destination capacity are both
five, the listed lanes do not allow all five crates to be delivered.
