# Prime Power Xor Sum

Define a function `f` on positive integers by

- `f(1) = 1`;
- `f(p^e) = p XOR e` for every prime `p` and exponent `e >= 1`, where `XOR`
  is the bitwise exclusive or;
- `f(ab) = f(a) f(b)` whenever `gcd(a,b) = 1`.

For example, `f(8) = 2 XOR 3 = 1` and `f(12) = f(4) f(3) = 0 * 2 = 0`.

Given `N`, print `f(1) + f(2) + ... + f(N)` modulo `1,000,000,007`.

## Input

One integer `N`.

- `1 <= N <= 10^10`.

## Output

Print the sum modulo `1,000,000,007`.

## Sample input

```text
10
```

## Sample output

```text
36
```
