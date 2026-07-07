import sys


def mod_pow(a: int, b: int, mod: int) -> int:
    a %= mod
    result = 1 % mod
    while b:
        if b & 1:
            result = result * a % mod
        a = a * a % mod
        b >>= 1
    return result


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    q = data[0]
    out = []
    idx = 1
    for _ in range(q):
        a, b, mod = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        out.append(str(mod_pow(a, b, mod)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
