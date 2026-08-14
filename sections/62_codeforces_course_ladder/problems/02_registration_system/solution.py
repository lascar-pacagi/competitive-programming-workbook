import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    out = []
    for _ in range(t):
        n = int(data[index])
        pos = int(data[index + 1])
        moves = data[index + 2].decode()
        index += 3
        visits = [0] * (n + 1)
        visits[pos] += 1
        for move in moves:
            if move == "R":
                pos = 1 if pos == n else pos + 1
            else:
                pos = n if pos == 1 else pos - 1
            visits[pos] += 1
        best = max(range(1, n + 1), key=lambda slot: (visits[slot], -slot))
        out.append(f"{pos} {best}")
    print("\n".join(out))


if __name__ == "__main__":
    main()
