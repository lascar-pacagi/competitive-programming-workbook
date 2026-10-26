# Q. Exact Beacon Codes

There are `n` beacons. Beacon `i` has integer code `code[i]`. Activate exactly
`k` distinct beacons. Their combined code is the bitwise XOR of their codes.

Count the activation subsets whose combined code equals a given `target`.
Beacons are distinguished by index: equal codes do not make two beacons
interchangeable when counting subsets. An activation subset has no ordering.
The XOR of the empty subset is defined to be `0`.

## Input

The first line contains `n k target`. The second line contains the `n` codes.

- `1 <= n <= 40` and `0 <= k <= n`.
- `0 <= target, code[i] < 2^30`.

## Output

Print the exact number of valid subsets, without taking a modulus. The answer
fits a signed 64-bit integer.

## Sample

Input:

```text
4 2 0
1 1 2 2
```

Output:

```text
2
```

The valid subsets are beacon indices `{1,2}` and `{3,4}`. Each selected pair
has equal codes, whose XOR is zero.
