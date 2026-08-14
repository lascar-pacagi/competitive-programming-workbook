# F. Shared Maintenance Window

Machine A signals at times

```text
offsetA, offsetA + periodA, offsetA + 2*periodA, ...
```

Machine B behaves similarly. For each query, find the earliest integer time
`t >= earliest` at which both machines signal. Print `-1` if they never signal
together.

## Input
```text
q
offsetA periodA offsetB periodB earliest
...
```
`1 <= q <= 200000`, `1 <= periodA,periodB <= 10^9`,
`0 <= offsetA < periodA`, `0 <= offsetB < periodB`, and
`0 <= earliest <= 10^18`.

## Sample
```text
3
2 6 5 9 0
2 6 5 9 20
1 4 2 6 100
```
```text
14
32
-1
```
