# N. Signal Concentration

A network has `n` stations. Activating station `i` has positive integer
running weight `c[i]`. An undirected link `(u,v,w)` contributes signal reward
`w` if both endpoints are active, and zero otherwise. All such rewards add.
Stations with no active neighbor still contribute their running weight.

Choose a **nonempty** subset of stations to maximize

```text
sum of rewards of links whose two endpoints are chosen
-----------------------------------------------------
       sum of running weights of chosen stations
```

Print the exact optimal ratio as a reduced fraction. A link is counted once,
not once per endpoint. You may choose disconnected stations; there is no
requirement to form a connected network.

## Input

```text
n m
c1 ... cn
u1 v1 w1
...
um vm wm
```

- `1 <= n <= 60`, `0 <= m <= min(300,n*(n-1)/2)`.
- `1 <= ci <= 20`, `0 <= wk <= 10^6`.
- `1 <= uk < vk <= n`; each unordered pair is listed at most once.

## Output

Print two integers `a b`, where `a/b` is the optimal ratio, `b > 0`, and
`gcd(a,b)=1`. Print `0 1` if the optimal reward is zero. Approximate decimal
output is not accepted.

## Sample

```text
3 2
1 2 1
1 2 6
2 3 2
```

```text
2 1
```

Choosing stations 1 and 2 gives reward 6 and weight 3. Choosing all three
also gives ratio two, while choosing stations 2 and 3 gives only `2/3`.
Either optimal subset is allowed internally, but the printed reduced ratio
must be the same.
