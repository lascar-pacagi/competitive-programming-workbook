# K. Quota Manifests

A shipping manifest must deliver exactly `K` crates from `n` depots to `m`
destinations. Depot `i` must send between `lo[i]` and `hi[i]` crates in total.
Destination `j` must receive between `low[j]` and `high[j]` crates in total.
Each listed lane has its own maximum capacity; unlisted lanes cannot be used.

Decide whether nonnegative integer amounts on the lanes can satisfy every
lower and upper bound and the exact overall total simultaneously. A crate
travels on exactly one lane. No transshipment or disposal is allowed.

## Input

```text
n m e K
lo[1] hi[1]
...
lo[n] hi[n]
low[1] high[1]
...
low[m] high[m]
u1 v1 capacity1
...
ue ve capacitye
```

- `1 <= n, m <= 100`, `0 <= e <= min(2000,n*m)`.
- `0 <= K <= 10^11`.
- All interval endpoints and lane capacities are integers in `[0,10^9]`.
- Every interval has its lower endpoint at most its upper endpoint.
- `1 <= uk <= n`, `1 <= vk <= m`; lane pairs are distinct.

## Output

Print `YES` if a valid manifest exists, or `NO` otherwise. You do not need
to print the lane amounts. Input bounds need not be jointly feasible.

## Sample

```text
2 2 3 3
1 2
1 2
1 2
1 2
1 1 2
1 2 1
2 1 1
```

```text
YES
```

One valid manifest sends one crate on each listed lane. Both depot totals,
both destination totals, all lane limits, and the overall total are satisfied.
