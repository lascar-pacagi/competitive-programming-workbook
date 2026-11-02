# L. Calendar Reinforcement

A workshop schedules work on integer-numbered days `0,1,...,T-1`. On day `d`,
its existing staff can process at most `base[d]` units of work in total.
A piecewise-constant calendar specifies these capacities.

Job `i` needs exactly `work[i]` units, all on days in `[release[i],deadline[i])`.
It may be interrupted and resumed on other days, but **one job may receive
at most one unit on any single day**, even if many workers are available.
Different jobs may be processed on the same day within the total capacity.

Hire `x` additional workers, each available on every day. This increases
every daily capacity by `x`. Find the smallest nonnegative integer `x`
that allows all jobs to be completed. Workers may switch jobs between days.

## Input

```text
n p
l1 r1 capacity1
...
lp rp capacityp
release1 deadline1 work1
...
releasen deadlinen workn
```

- `1 <= n, p <= 80`, `1 <= T <= 10^9`.
- The calendar intervals are listed in order, with `l1=0`, `ri=l(i+1)`,
  `rp=T`, and `li < ri`. Thus they cover all days exactly once.
- All endpoints are integers; `0 <= capacityi <= 10^9`.
- `0 <= releasei < deadlinei <= T`, `1 <= worki <= 10^9`.
- Every job-window interval includes its release day and excludes its deadline.

## Output

Print the minimum `x`, or `-1` if no amount of additional staff can complete
all jobs under the one-unit-per-job-per-day restriction.

## Sample

```text
3 2
0 2 1
2 4 0
0 3 2
1 4 2
0 4 1
```

```text
1
```

Without hiring, only two units can be processed but the jobs need five.
With one additional worker, a schedule is: job 1 on days 0 and 1, job 2
on days 2 and 3, and job 3 on day 0. All daily limits are respected.
