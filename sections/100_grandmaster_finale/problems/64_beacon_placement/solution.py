import sys
from bisect import bisect_left


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    S = 2 * n
    sites = sorted((int(data[1 + k]), k >> 1) for k in range(S))
    pos = [p for p, _ in sites]
    partner = [0] * S
    first = [-1] * n
    for k, (_, owner) in enumerate(sites):
        if first[owner] < 0:
            first[owner] = k
        else:
            partner[k] = first[owner]
            partner[first[owner]] = k
    size = 1
    while size < S:
        size *= 2
    V = S + 2 * size

    # Fixed part of the implication graph: tree edges and leaf -> negation.
    base = [[] for _ in range(V)]
    for t in range(1, size):
        base[S + t] = [S + 2 * t, S + 2 * t + 1]
    for k in range(S):
        base[S + size + k] = [partner[k]]

    def feasible(d):
        adj = base[:]
        for k in range(S):
            out = []
            p = pos[k]
            for l, r in ((bisect_left(pos, p - d + 1), k), (k + 1, bisect_left(pos, p + d))):
                l += size
                r += size
                while l < r:
                    if l & 1:
                        out.append(S + l)
                        l += 1
                    if r & 1:
                        r -= 1
                        out.append(S + r)
                    l >>= 1
                    r >>= 1
            adj[k] = out
        # Iterative Tarjan.
        index = [-1] * V
        low = [0] * V
        comp = [-1] * V
        on_stack = [False] * V
        stack = []
        counter = 0
        comps = 0
        for s in range(V):
            if index[s] >= 0:
                continue
            index[s] = low[s] = counter
            counter += 1
            stack.append(s)
            on_stack[s] = True
            call = [(s, iter(adj[s]))]
            while call:
                v, it = call[-1]
                advanced = False
                for w in it:
                    if index[w] < 0:
                        index[w] = low[w] = counter
                        counter += 1
                        stack.append(w)
                        on_stack[w] = True
                        call.append((w, iter(adj[w])))
                        advanced = True
                        break
                    if on_stack[w] and index[w] < low[v]:
                        low[v] = index[w]
                if advanced:
                    continue
                call.pop()
                if call:
                    u = call[-1][0]
                    if low[v] < low[u]:
                        low[u] = low[v]
                if low[v] == index[v]:
                    while True:
                        w = stack.pop()
                        on_stack[w] = False
                        comp[w] = comps
                        if w == v:
                            break
                    comps += 1
        for k in range(S):
            if comp[k] == comp[partner[k]]:
                return False
        return True

    lo, hi = 0, pos[-1] - pos[0] + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if feasible(mid):
            lo = mid
        else:
            hi = mid
    print(lo)


if __name__ == "__main__":
    main()
