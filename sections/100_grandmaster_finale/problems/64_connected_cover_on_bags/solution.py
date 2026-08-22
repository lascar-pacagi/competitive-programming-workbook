import sys

def main():
    lines = sys.stdin.buffer.readlines()
    n, m = map(int, lines[0].split())
    weight = list(map(int, lines[1].split()))
    adj = [0] * n
    for line in lines[2:2 + m]:
        u, v = map(int, line.split())
        u -= 1
        v -= 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    t = int(lines[2 + m])
    dp = []
    bags = []
    for line in lines[3 + m:3 + m + t]:
        z = line.split()
        kind = z[0]
        if kind == b'L':
            bags.append(0)
            dp.append({0: 0})
        elif kind == b'I':
            child = int(z[1]) - 1
            v = int(z[2]) - 1
            bags.append(bags[child] | 1 << v)
            cur = dict(dp[child])
            for mask, val in dp[child].items():
                if not mask & adj[v]:
                    cur[mask | 1 << v] = max(cur.get(mask | 1 << v, -10 ** 30), val + weight[v])
            dp.append(cur)
        elif kind == b'F':
            child = int(z[1]) - 1
            v = int(z[2]) - 1
            bags.append(bags[child] & ~(1 << v))
            cur = {}
            for mask, val in dp[child].items():
                key = mask & ~(1 << v)
                cur[key] = max(cur.get(key, -10 ** 30), val)
            dp.append(cur)
        else:
            a = int(z[1]) - 1
            b = int(z[2]) - 1
            bags.append(bags[a])
            cur = {}
            for mask, val in dp[a].items():
                if mask in dp[b]:
                    cur[mask] = val + dp[b][mask] - sum((weight[v] for v in range(n) if mask >> v & 1))
            dp.append(cur)
    print(sum(weight) - dp[-1].get(0, max(dp[-1].values())))
if __name__ == '__main__':
    main()
