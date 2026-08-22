import sys

MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    x = [0] * n
    y = [0] * n
    reward = [0] * n
    at = 1
    for i in range(n):
        x[i], y[i], reward[i] = data[at:at + 3]
        at += 3
    ys = sorted(set(y))
    rank_y = [0] * n
    position = {value: i + 1 for i, value in enumerate(ys)}
    for i in range(n):
        rank_y[i] = position[y[i]]

    dp = reward.copy()
    ways = [1] * n
    bit_score = [0] * (len(ys) + 1)
    bit_ways = [0] * (len(ys) + 1)
    touched = []

    def update(pos: int, score: int, count: int) -> None:
        while pos < len(bit_score):
            if score > bit_score[pos]:
                bit_score[pos] = score
                bit_ways[pos] = count
            elif score == bit_score[pos] and score:
                bit_ways[pos] = (bit_ways[pos] + count) % MOD
            touched.append(pos)
            pos += pos & -pos

    def query(pos: int) -> tuple[int, int]:
        score = count = 0
        while pos:
            if bit_score[pos] > score:
                score, count = bit_score[pos], bit_ways[pos]
            elif bit_score[pos] == score and score:
                count = (count + bit_ways[pos]) % MOD
            pos -= pos & -pos
        return score, count

    sys.setrecursionlimit(1_000_000)

    def cdq(left: int, right: int) -> None:
        if right - left == 1:
            return
        middle = (left + right) // 2
        cdq(left, middle)
        first = sorted(range(left, middle), key=lambda i: (x[i], y[i]))
        second = sorted(range(middle, right), key=lambda i: (x[i], y[i]))
        pointer = 0
        for j in second:
            while pointer < len(first) and x[first[pointer]] < x[j]:
                i = first[pointer]
                pointer += 1
                update(rank_y[i], dp[i], ways[i])
            best, count = query(rank_y[j] - 1)
            if best:
                candidate = best + reward[j]
                if candidate > dp[j]:
                    dp[j], ways[j] = candidate, count
                elif candidate == dp[j]:
                    ways[j] = (ways[j] + count) % MOD
        for pos in touched:
            bit_score[pos] = bit_ways[pos] = 0
        touched.clear()
        cdq(middle, right)

    cdq(0, n)
    best = max(dp)
    count = sum(ways[i] for i in range(n) if dp[i] == best) % MOD
    print(best, count)


if __name__ == "__main__":
    main()
