# Q. Event Attendance

There are `n` events. Event `i` may be attended on any one integer day from
`start_i` through `end_i`, inclusive. You may attend at most one event per day,
and attending an event occupies that whole day. Find the maximum number of
events you can attend.

## Input

```text
n
start1 end1
start2 end2
...
startn endn
```

`1 <= n <= 200000` and
`1 <= start_i <= end_i <= 10^9`.

## Output

Print the maximum number of events that can be attended.

## Sample

```text
4
1 2
2 2
1 3
3 3
```

```text
3
```
