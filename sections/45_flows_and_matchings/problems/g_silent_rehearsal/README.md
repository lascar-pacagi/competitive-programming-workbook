# G. Silent Rehearsal

Each of `n` performers must rehearse in a different room. There are `m` rooms.
A listed pair `(u,v,d)` means performer `u` may use room `v`, and needs `d`
minutes to prepare it. Unlisted pairs are forbidden.

All performers prepare their chosen rooms simultaneously. The rehearsal
starts when everyone is ready, so its waiting time is the largest preparation
time among the chosen pairs. Assign every performer a distinct compatible
room and minimize this waiting time. There is no requirement to use all rooms.

## Input

```text
n m e
u1 v1 d1
...
ue ve de
```

- `1 <= n, m <= 250`, `0 <= e <= n*m`.
- `1 <= uk <= n`, `1 <= vk <= m`, `0 <= dk <= 10^9`.
- Each performer-room pair is listed at most once.

## Output

Print the smallest waiting time, or `-1` if some performer cannot receive a
room in any complete assignment. Zero is a valid waiting time.

## Sample

```text
2 3 4
1 1 1
1 2 4
2 1 2
2 3 7
```

```text
4
```

Assign performer 1 to room 2 and performer 2 to room 1. Waiting only two
minutes would allow both performers to use only room 1, so it is impossible.
