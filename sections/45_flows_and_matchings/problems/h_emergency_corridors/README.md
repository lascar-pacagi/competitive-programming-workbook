# H. Emergency Corridors

A building has `n` rooms and `m` one-way corridors. Some rooms contain hazard
sources; some other rooms contain archives. A hazard can follow any directed
path of rooms not closed by the administrator. Close rooms so that no hazard
source can reach any archive, minimizing the total closure cost.

Closing a room removes it and every incident corridor. A room with listed
cost `-1` cannot be closed. Hazard rooms and archive rooms also cannot be
closed, regardless of their listed costs. All closures happen simultaneously;
you may close any subset of the remaining rooms. A zero-cost closure is allowed.

## Input

```text
n m k q
c1 ... cn
s1 ... sk
t1 ... tq
u1 v1
...
um vm
```

- `2 <= n <= 150`, `0 <= m <= min(2000,n*(n-1))`.
- `1 <= k, q`, `k+q <= n`.
- Each `ci` is `-1` or an integer in `[0,10^9]`.
- Hazard IDs and archive IDs are distinct, and the two lists are disjoint.
- `1 <= ui, vi <= n`, `ui != vi`; no directed corridor occurs twice.
- Opposite corridors may both exist. Corridors cannot be closed separately.

## Output

Print the minimum total cost, or `-1` if no allowed set of closures can
protect every archive. Print `0` if they are already protected. The total
cost can exceed 32-bit range.

## Sample

```text
5 5 1 1
-1 4 2 7 -1
1
5
1 2
2 5
1 3
3 4
4 5
```

```text
6
```

Closing rooms 2 and 3 costs six and stops both routes to room 5. Closing
only one of them leaves another route open.
