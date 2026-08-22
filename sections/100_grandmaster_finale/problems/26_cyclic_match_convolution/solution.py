import sys

MOD = 998244353
ROOT = 3


def ntt(values, inverse):
    n = len(values)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            values[i], values[j] = values[j], values[i]
    length = 2
    while length <= n:
        step = pow(ROOT, (MOD - 1) // length, MOD)
        if inverse:
            step = pow(step, MOD - 2, MOD)
        half = length // 2
        for start in range(0, n, length):
            root = 1
            stop = start + half
            for left in range(start, stop):
                right = left + half
                u = values[left]
                v = values[right] * root % MOD
                values[left] = (u + v) % MOD
                values[right] = (u - v) % MOD
                root = root * step % MOD
        length <<= 1
    if inverse:
        scale = pow(n, MOD - 2, MOD)
        for i in range(n):
            values[i] = values[i] * scale % MOD


def transformed_indicators(first, second, predicate, size):
    left = [int(predicate(c)) for c in reversed(first)]
    right = [int(predicate(c)) for c in second + second]
    left.extend([0] * (size - len(left)))
    right.extend([0] * (size - len(right)))
    ntt(left, False)
    ntt(right, False)
    return left, right


def main():
    data = sys.stdin.buffer.read().split()
    n, limit = map(int, data[:2])
    first, second = data[2], data[3]
    size = 1
    while size < 3 * n - 1:
        size <<= 1

    left, right = transformed_indicators(
        first, second, lambda c: c != 63, size)
    mismatch = [left[i] * right[i] % MOD for i in range(size)]
    del left, right

    for character in (97, 98, 99):
        left, right = transformed_indicators(
            first, second, lambda c, wanted=character: c == wanted, size)
        for i in range(size):
            mismatch[i] = (mismatch[i] - left[i] * right[i]) % MOD
        del left, right

    ntt(mismatch, True)
    answer = [shift for shift in range(n)
              if mismatch[n - 1 + shift] <= limit]
    print(len(answer))
    print(*answer)


if __name__ == "__main__":
    main()
