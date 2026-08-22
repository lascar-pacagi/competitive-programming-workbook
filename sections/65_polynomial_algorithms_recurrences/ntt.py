MOD = 998_244_353
ROOT = 3


def transform(values: list[int], inverse: bool) -> None:
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
        root = pow(ROOT, (MOD - 1) // length, MOD)
        if inverse:
            root = pow(root, MOD - 2, MOD)
        half = length // 2
        for start in range(0, n, length):
            current = 1
            for offset in range(half):
                left = values[start + offset]
                right = values[start + offset + half] * current % MOD
                values[start + offset] = (left + right) % MOD
                values[start + offset + half] = (left - right) % MOD
                current = current * root % MOD
        length <<= 1

    if inverse:
        inverse_n = pow(n, MOD - 2, MOD)
        for i, value in enumerate(values):
            values[i] = value * inverse_n % MOD


def convolution(
    left: list[int], right: list[int], keep: int | None = None
) -> list[int]:
    if not left or not right:
        return []
    result_size = len(left) + len(right) - 1
    if keep is not None:
        result_size = min(result_size, keep)
    if min(len(left), len(right)) <= 24:
        result = [0] * result_size
        for i, a in enumerate(left):
            for j, b in enumerate(right[: result_size - i]):
                result[i + j] = (result[i + j] + a * b) % MOD
        return result

    size = 1 << (len(left) + len(right) - 2).bit_length()
    a = left + [0] * (size - len(left))
    b = right + [0] * (size - len(right))
    transform(a, False)
    transform(b, False)
    for i in range(size):
        a[i] = a[i] * b[i] % MOD
    transform(a, True)
    return a[:result_size]
