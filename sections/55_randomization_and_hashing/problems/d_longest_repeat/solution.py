import sys


MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 911_382_323


def main() -> None:
    s = sys.stdin.buffer.readline().strip()
    n = len(s)
    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)
    hash1 = [0] * (n + 1)
    hash2 = [0] * (n + 1)
    for index, byte in enumerate(s, 1):
        power1[index] = power1[index - 1] * BASE % MOD1
        power2[index] = power2[index - 1] * BASE % MOD2
        hash1[index] = (hash1[index - 1] * BASE + byte) % MOD1
        hash2[index] = (hash2[index - 1] * BASE + byte) % MOD2

    def repeated(length: int) -> bool:
        seen: set[tuple[int, int]] = set()
        for left in range(n - length + 1):
            right = left + length
            key = (
                (hash1[right] - hash1[left] * power1[length]) % MOD1,
                (hash2[right] - hash2[left] * power2[length]) % MOD2,
            )
            if key in seen:
                return True
            seen.add(key)
        return False

    low, high, answer = 1, n, 0
    while low <= high:
        middle = (low + high) // 2
        if repeated(middle):
            answer = middle
            low = middle + 1
        else:
            high = middle - 1
    print(answer)


if __name__ == "__main__":
    main()
