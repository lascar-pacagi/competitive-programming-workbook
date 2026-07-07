"""Reference solution for B. Rank Table."""

import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        rows: list[tuple[str, int, int]] = []
        for _ in range(n):
            name = data[idx].decode()
            score = int(data[idx + 1])
            penalty = int(data[idx + 2])
            idx += 3
            rows.append((name, score, penalty))
        rows.sort(key=lambda row: (-row[1], row[2], row[0]))
        out.append(" ".join(row[0] for row in rows))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

