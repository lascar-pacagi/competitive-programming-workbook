import sys
MOD = 1000000007

def canon(a):
    mp = {}
    nxt = 1
    out = []
    for x in a:
        if x and x not in mp:
            mp[x] = nxt
            nxt += 1
        out.append(mp.get(x, 0))
    return tuple(out)

def main():
    data = sys.stdin.buffer.read().split()
    h, w = map(int, data[:2])
    g = [x.decode() for x in data[2:]]
    dp = {(tuple([0] * w), False): 1}
    for r in range(h):
        for c in range(w):
            nd = {}
            for (labels, closed), value in dp.items():
                old = list(labels)
                up = old[c]
                left = old[c - 1] if c else 0
                new = old[:]
                new[c] = 0
                vanished = up and up not in new
                if not vanished or (not any(new) and (not closed)):
                    key = (canon(new), closed or bool(vanished))
                    nd[key] = (nd.get(key, 0) + value) % MOD
                if g[r][c] == '.' and (not closed):
                    new = old[:]
                    if left and up and (left != up):
                        new = [left if x == up else x for x in new]
                    new[c] = left or up or max(new, default=0) + 1
                    key = (canon(new), False)
                    nd[key] = (nd.get(key, 0) + value) % MOD
            dp = nd
    answer = 0
    for (labels, closed), value in dp.items():
        if closed or len(set(labels) - {0}) == 1:
            answer = (answer + value) % MOD
    print(answer)
if __name__ == '__main__':
    main()
