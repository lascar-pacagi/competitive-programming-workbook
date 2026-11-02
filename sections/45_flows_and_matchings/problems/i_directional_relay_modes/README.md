# I. Directional Relay Modes

Every relay must be set to mode 0 or mode 1. Relay `i` costs `c0[i]` to run
in mode 0 and `c1[i]` in mode 1. A directed compatibility notice `(u,v,p)`
adds penalty `p` exactly when relay `u` is in mode 0 and relay `v` is in
mode 1. None of the other three combinations triggers that notice.

Several notices may be triggered simultaneously, and their penalties add.
Choose all modes to minimize running costs plus triggered penalties. There
is no restriction on how many relays use either mode.

## Input

```text
n m
c0[1] c1[1]
...
c0[n] c1[n]
u1 v1 p1
...
um vm pm
```

- `1 <= n <= 250`, `0 <= m <= min(3000,n*(n-1))`.
- `0 <= c0[i], c1[i], pk <= 10^9`.
- `1 <= uk, vk <= n`, `uk != vk`.
- Ordered pairs are distinct. Both `(u,v)` and `(v,u)` may be listed;
  they are separate notices with their own triggering conditions.

## Output

Print the minimum total cost as a 64-bit integer.

## Sample

```text
2 1
0 5
4 0
1 2 10
```

```text
4
```

Using each relay's cheapest mode gives modes `(0,1)` and triggers penalty 10.
Modes `(0,0)` cost four and trigger no penalty. The notice does not penalize
modes `(1,0)` merely because the modes differ.
