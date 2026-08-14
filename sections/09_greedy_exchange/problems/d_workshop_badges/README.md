# D. Workshop Badges

## Statement

For each test case, there are `n` attendees. Attendee `i` is available on every
integer day from `l[i]` through `r[i]`, inclusive.

Choose the minimum number of badge-pickup days so that every attendee is
available on at least one chosen day.

Think of choosing a day as opening one badge desk on that day. The desk may
give badges to **all** attendees who are available that day; opening it still
costs only one pickup day, regardless of how many people use it. An attendee
needs a badge on one day inside their own availability interval. They do not
need a badge on every day of that interval.

The endpoints are inclusive. For example, an attendee with availability
`[2, 5]` can collect a badge on day `2`, `3`, `4`, or `5`. An attendee with
`[6, 6]` can collect it only on day `6`.

For the first sample case, the availability intervals are:

```text
attendee 1: [1, 3]
attendee 2: [2, 5]
attendee 3: [4, 6]
attendee 4: [6, 6]
```

Choose pickup days `3` and `6`:

```text
day 3 serves attendees 1 and 2
day 6 serves attendees 3 and 4
```

Thus two days are sufficient. One day cannot serve both attendee 1, who must
collect no later than day `3`, and attendee 4, who can collect only on day
`6`, so the minimum is exactly `2`.

## Input

```text
T
n
l1 r1
l2 r2
...
```

`1 <= T <= 50`, `1 <= n <= 200000`, the total `n` over all test cases is at
most `200000`, and `-10^9 <= l[i] <= r[i] <= 10^9`.

## Output

Print the minimum number of pickup days for each test case.

## Sample

Input:

```text
3
4
1 3
2 5
4 6
6 6
3
-5 -3
-2 0
1 4
1
7 7
```

Output:

```text
2
3
1
```
