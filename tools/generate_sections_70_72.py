"""Generate the original local packages for Master+ Sections 70--72."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


CPP_STUB = """#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // TODO: solve the problem.
    return 0;
}
"""

PY_STUB = """import sys


def main() -> None:
    # TODO: solve the problem.
    pass


if __name__ == "__main__":
    main()
"""


DINIC_CPP = r"""#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

struct Dinic {
    struct Edge { int to, rev; int64 cap; };
    vector<vector<Edge>> g;
    vector<int> level, it;
    Dinic(int n) : g(n), level(n), it(n) {}
    void add_edge(int u, int v, int64 cap) {
        Edge a{v, (int)g[v].size(), cap};
        Edge b{u, (int)g[u].size(), 0};
        g[u].push_back(a); g[v].push_back(b);
    }
    bool bfs(int s, int t) {
        fill(level.begin(), level.end(), -1);
        queue<int> q; level[s] = 0; q.push(s);
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (auto &e : g[u]) if (e.cap && level[e.to] < 0)
                level[e.to] = level[u] + 1, q.push(e.to);
        }
        return level[t] >= 0;
    }
    int64 dfs(int u, int t, int64 pushed) {
        if (u == t) return pushed;
        for (int &i = it[u]; i < (int)g[u].size(); ++i) {
            Edge &e = g[u][i];
            if (!e.cap || level[e.to] != level[u] + 1) continue;
            int64 take = dfs(e.to, t, min(pushed, e.cap));
            if (take) { e.cap -= take; g[e.to][e.rev].cap += take; return take; }
        }
        return 0;
    }
    int64 flow(int s, int t) {
        int64 ans = 0, pushed;
        while (bfs(s, t)) {
            fill(it.begin(), it.end(), 0);
            while ((pushed = dfs(s, t, (1LL << 62)))) ans += pushed;
        }
        return ans;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m; if (!(cin >> n >> m)) return 0;
    int ss = n, tt = n + 1; Dinic dinic(n + 2);
    vector<int64> balance(n);
    for (int i = 0, u, v; i < m; ++i) {
        int64 low, high; cin >> u >> v >> low >> high; --u; --v;
        dinic.add_edge(u, v, high - low);
        balance[u] -= low; balance[v] += low;
    }
    int64 need = 0;
    for (int v = 0; v < n; ++v) {
        if (balance[v] > 0) dinic.add_edge(ss, v, balance[v]), need += balance[v];
        if (balance[v] < 0) dinic.add_edge(v, tt, -balance[v]);
    }
    cout << (dinic.flow(ss, tt) == need ? "YES\n" : "NO\n");
}
"""

DINIC_PY = r"""import collections
import sys


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        self.g[u].append([v, cap, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u]) - 1])

    def flow(self, s, t):
        answer = 0
        while True:
            level = [-1] * len(self.g)
            level[s] = 0
            q = collections.deque([s])
            while q:
                u = q.popleft()
                for v, cap, _ in self.g[u]:
                    if cap and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                return answer
            it = [0] * len(self.g)

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    v, cap, rev = e
                    if cap and level[v] == level[u] + 1:
                        take = dfs(v, min(pushed, cap))
                        if take:
                            e[1] -= take
                            self.g[v][rev][1] += take
                            return take
                    it[u] += 1
                return 0

            while pushed := dfs(s, 10**30):
                answer += pushed


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[:2]
    dinic = Dinic(n + 2)
    balance = [0] * n
    at = 2
    for _ in range(m):
        u, v, low, high = data[at : at + 4]
        at += 4
        u -= 1
        v -= 1
        dinic.add_edge(u, v, high - low)
        balance[u] -= low
        balance[v] += low
    need = 0
    for v, value in enumerate(balance):
        if value > 0:
            dinic.add_edge(n, v, value)
            need += value
        elif value < 0:
            dinic.add_edge(v, n + 1, -value)
    print("YES" if dinic.flow(n, n + 1) == need else "NO")


if __name__ == "__main__":
    main()
"""


MCF_CPP_CORE = r"""#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
const int64 INF = (1LL << 62);

struct MCF {
    struct Edge { int to, rev, cap, initial; int64 cost; };
    vector<vector<Edge>> g;
    MCF(int n) : g(n) {}
    pair<int, int> add_edge(int u, int v, int cap, int64 cost) {
        int id = g[u].size();
        g[u].push_back({v, (int)g[v].size(), cap, cap, cost});
        g[v].push_back({u, id, 0, 0, -cost});
        return {u, id};
    }
    pair<int, int64> flow(int s, int t, int limit) {
        int n = g.size(), sent = 0;
        int64 cost = 0;
        vector<int64> pot(n, INF), dist(n);
        pot[s] = 0;
        for (int rep = 0; rep < n; ++rep) {
            bool changed = false;
            for (int u = 0; u < n; ++u) if (pot[u] < INF)
                for (auto &e : g[u]) if (e.cap && pot[e.to] > pot[u] + e.cost)
                    pot[e.to] = pot[u] + e.cost, changed = true;
            if (!changed) break;
        }
        for (auto &x : pot) if (x == INF) x = 0;
        vector<int> pv(n), pe(n);
        while (sent < limit) {
            fill(dist.begin(), dist.end(), INF); dist[s] = 0;
            priority_queue<pair<int64, int>, vector<pair<int64, int>>, greater<pair<int64, int>>> pq;
            pq.push({0, s});
            while (!pq.empty()) {
                auto [d, u] = pq.top(); pq.pop();
                if (d != dist[u]) continue;
                for (int i = 0; i < (int)g[u].size(); ++i) {
                    auto &e = g[u][i];
                    int64 nd = d + e.cost + pot[u] - pot[e.to];
                    if (e.cap && nd < dist[e.to])
                        dist[e.to] = nd, pv[e.to] = u, pe[e.to] = i, pq.push({nd, e.to});
                }
            }
            if (dist[t] == INF) break;
            for (int v = 0; v < n; ++v) if (dist[v] < INF) pot[v] += dist[v];
            int add = limit - sent;
            for (int v = t; v != s; v = pv[v]) add = min(add, g[pv[v]][pe[v]].cap);
            for (int v = t; v != s; v = pv[v]) {
                Edge &e = g[pv[v]][pe[v]];
                cost += (int64)add * e.cost; e.cap -= add; g[v][e.rev].cap += add;
            }
            sent += add;
        }
        return {sent, cost};
    }
};
"""

MCF_PY_CORE = r"""import heapq
import sys


class MCF:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap, cost):
        ref = (u, len(self.g[u]))
        self.g[u].append([v, cap, cost, len(self.g[v]), cap])
        self.g[v].append([u, 0, -cost, len(self.g[u]) - 1, 0])
        return ref

    def flow(self, s, t, limit):
        n = len(self.g)
        inf = 10**40
        potential = [inf] * n
        potential[s] = 0
        for _ in range(n):
            changed = False
            for u in range(n):
                if potential[u] == inf:
                    continue
                for v, cap, cost, _, _ in self.g[u]:
                    if cap and potential[v] > potential[u] + cost:
                        potential[v] = potential[u] + cost
                        changed = True
            if not changed:
                break
        potential = [0 if x == inf else x for x in potential]
        sent = total = 0
        while sent < limit:
            dist = [inf] * n
            prev = [None] * n
            dist[s] = 0
            pq = [(0, s)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for i, (v, cap, cost, _, _) in enumerate(self.g[u]):
                    nd = d + cost + potential[u] - potential[v]
                    if cap and nd < dist[v]:
                        dist[v] = nd
                        prev[v] = (u, i)
                        heapq.heappush(pq, (nd, v))
            if dist[t] == inf:
                break
            for v in range(n):
                if dist[v] < inf:
                    potential[v] += dist[v]
            add = limit - sent
            v = t
            while v != s:
                u, i = prev[v]
                add = min(add, self.g[u][i][1])
                v = u
            v = t
            while v != s:
                u, i = prev[v]
                e = self.g[u][i]
                total += add * e[2]
                e[1] -= add
                self.g[v][e[3]][1] += add
                v = u
            sent += add
        return sent, total
"""


SHIP_CPP = MCF_CPP_CORE + r"""
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, need; if (!(cin >> n >> m >> need)) return 0;
    int s, t; cin >> s >> t; --s; --t;
    MCF mcf(n);
    for (int i = 0, u, v, cap; i < m; ++i) {
        int64 cost; cin >> u >> v >> cap >> cost;
        mcf.add_edge(--u, --v, cap, cost);
    }
    auto [sent, cost] = mcf.flow(s, t, need);
    if (sent < need) cout << "IMPOSSIBLE\n"; else cout << cost << '\n';
}
"""

SHIP_PY = MCF_PY_CORE + r"""

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m, need, s, t = data[:5]
    mcf = MCF(n)
    at = 5
    for _ in range(m):
        u, v, cap, cost = data[at : at + 4]
        at += 4
        mcf.add_edge(u - 1, v - 1, cap, cost)
    sent, cost = mcf.flow(s - 1, t - 1, need)
    print(cost if sent == need else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
"""


QUOTA_CPP = MCF_CPP_CORE + r"""
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, p, m; if (!(cin >> n >> p >> m)) return 0;
    vector<int> low(p), high(p);
    int required = 0;
    for (int j = 0; j < p; ++j) cin >> low[j] >> high[j], required += low[j];
    struct Choice { int w, j, profit; };
    vector<Choice> choices(m); int max_profit = 0;
    for (auto &[w, j, profit] : choices) {
        cin >> w >> j >> profit; --w; --j; max_profit = max(max_profit, profit);
    }
    int s = n + p, t = s + 1; MCF mcf(t + 1);
    for (int w = 0; w < n; ++w) mcf.add_edge(s, w, 1, 0);
    for (auto [w, j, profit] : choices) mcf.add_edge(w, n + j, 1, -profit);
    int64 big = (int64)(n + 1) * (max_profit + 1);
    vector<pair<int, int>> mandatory;
    for (int j = 0; j < p; ++j) {
        mandatory.push_back(mcf.add_edge(n + j, t, low[j], -big));
        mcf.add_edge(n + j, t, high[j] - low[j], 0);
    }
    auto [sent, cost] = mcf.flow(s, t, n);
    bool ok = sent == n;
    for (auto [u, id] : mandatory) ok &= mcf.g[u][id].cap == 0;
    if (!ok) cout << "IMPOSSIBLE\n";
    else cout << -cost - big * required << '\n';
}
"""

QUOTA_PY = MCF_PY_CORE + r"""

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, p, m = data[:3]
    at = 3
    low = []
    high = []
    for _ in range(p):
        lo, hi = data[at : at + 2]
        at += 2
        low.append(lo)
        high.append(hi)
    choices = []
    max_profit = 0
    for _ in range(m):
        w, j, profit = data[at : at + 3]
        at += 3
        choices.append((w - 1, j - 1, profit))
        max_profit = max(max_profit, profit)
    s = n + p
    t = s + 1
    mcf = MCF(t + 1)
    for w in range(n):
        mcf.add_edge(s, w, 1, 0)
    for w, j, profit in choices:
        mcf.add_edge(w, n + j, 1, -profit)
    big = (n + 1) * (max_profit + 1)
    mandatory = []
    for j in range(p):
        mandatory.append(mcf.add_edge(n + j, t, low[j], -big))
        mcf.add_edge(n + j, t, high[j] - low[j], 0)
    sent, cost = mcf.flow(s, t, n)
    ok = sent == n and all(mcf.g[u][i][1] == 0 for u, i in mandatory)
    print(-cost - big * sum(low) if ok else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
"""


MONO_CPP = r"""#include <bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; if (!(cin >> n)) return 0;
    priority_queue<long long> left;
    long long answer = 0;
    for (int i = 0; i < n; ++i) {
        long long x; cin >> x;
        left.push(x); left.push(x);
        answer += left.top() - x; left.pop();
    }
    cout << answer << '\n';
}
"""

MONO_PY = r"""import heapq
import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    heap = []
    answer = 0
    for x in data[1:]:
        heapq.heappush(heap, -x)
        heapq.heappush(heap, -x)
        answer += -heapq.heappop(heap) - x
    print(answer)


if __name__ == "__main__":
    main()
"""


MST_CPP = r"""#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
struct DSU {
    vector<int> p, sz;
    DSU(int n) : p(n), sz(n, 1) { iota(p.begin(), p.end(), 0); }
    int find(int x) { while (x != p[x]) x = p[x]; return x; }
    bool unite(int a, int b) {
        a = find(a); b = find(b); if (a == b) return false;
        if (sz[a] < sz[b]) swap(a, b); p[b] = a; sz[a] += sz[b]; return true;
    }
};
struct Edge { int u, v, red; int64 w; };
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, wanted; if (!(cin >> n >> m >> wanted)) return 0;
    vector<Edge> edges(m);
    for (auto &e : edges) { char c; cin >> e.u >> e.v >> e.w >> c; --e.u; --e.v; e.red = c == 'R'; }
    auto run = [&](int64 lambda, bool prefer_red) {
        vector<int> order(m); iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int i, int j) {
            int64 a = edges[i].w + lambda * edges[i].red;
            int64 b = edges[j].w + lambda * edges[j].red;
            if (a != b) return a < b;
            return prefer_red ? edges[i].red > edges[j].red : edges[i].red < edges[j].red;
        });
        DSU dsu(n); int used = 0, red = 0; int64 value = 0;
        for (int id : order) if (dsu.unite(edges[id].u, edges[id].v)) {
            ++used; red += edges[id].red; value += edges[id].w + lambda * edges[id].red;
        }
        return tuple<int, int, int64>{used, red, value};
    };
    auto [u1, min_red, z1] = run(400000000000000LL, false);
    auto [u2, max_red, z2] = run(-400000000000000LL, true);
    if (u1 != n - 1 || wanted < min_red || wanted > max_red) { cout << "IMPOSSIBLE\n"; return 0; }
    int64 lo = -400000000000000LL, hi = 400000000000000LL;
    while (lo < hi) {
        int64 mid = lo + (hi - lo + 1) / 2;
        auto [used, red, value] = run(mid, true);
        if (red >= wanted) lo = mid; else hi = mid - 1;
    }
    auto [used, red, modified] = run(lo, true);
    cout << modified - lo * wanted << '\n';
}
"""

MST_PY = r"""import sys


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n, m, wanted = int(next(it)), int(next(it)), int(next(it))
    edges = []
    for _ in range(m):
        u, v, w, color = int(next(it)) - 1, int(next(it)) - 1, int(next(it)), next(it)
        edges.append((u, v, w, color == b"R"))

    def run(lam, prefer_red):
        order = sorted(
            edges,
            key=lambda e: (e[2] + lam * e[3], -e[3] if prefer_red else e[3]),
        )
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        used = red = value = 0
        for u, v, w, is_red in order:
            u, v = find(u), find(v)
            if u == v:
                continue
            if size[u] < size[v]:
                u, v = v, u
            parent[v] = u
            size[u] += size[v]
            used += 1
            red += is_red
            value += w + lam * is_red
        return used, red, value

    bound = 400_000_000_000_000
    used, minimum, _ = run(bound, False)
    _, maximum, _ = run(-bound, True)
    if used != n - 1 or not minimum <= wanted <= maximum:
        print("IMPOSSIBLE")
        return
    lo, hi = -bound, bound
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if run(mid, True)[1] >= wanted:
            lo = mid
        else:
            hi = mid - 1
    _, _, modified = run(lo, True)
    print(modified - lo * wanted)


if __name__ == "__main__":
    main()
"""


ALLOC_CPP = r"""#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using i128 = __int128_t;
string show(i128 x) {
    if (x == 0) return "0";
    bool neg = x < 0; if (neg) x = -x;
    string s; while (x) s.push_back('0' + x % 10), x /= 10;
    if (neg) s.push_back('-');
    reverse(s.begin(), s.end()); return s;
}
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n; int64 k; if (!(cin >> n >> k)) return 0;
    vector<int64> a(n), b(n), cap(n); int64 total = 0;
    for (int i = 0; i < n; ++i) cin >> a[i] >> b[i] >> cap[i], total += cap[i];
    if (total < k) { cout << "IMPOSSIBLE\n"; return 0; }
    auto count = [&](i128 threshold) {
        int64 result = 0;
        for (int i = 0; i < n; ++i) {
            if (threshold < a[i] + b[i]) continue;
            int64 x = min<i128>(cap[i], (threshold - b[i] + a[i]) / (2 * a[i]));
            result += min(cap[i], x);
            if (result >= k) return k;
        }
        return result;
    };
    if (k == 0) { cout << "0\n"; return 0; }
    i128 lo = 0, hi = 0; bool first = true;
    for (int i = 0; i < n; ++i) if (cap[i]) {
        i128 first_cost = (i128)a[i] + b[i];
        i128 last_cost = (i128)a[i] * (2 * (i128)cap[i] - 1) + b[i];
        if (first) lo = first_cost, hi = last_cost, first = false;
        else lo = min(lo, first_cost), hi = max(hi, last_cost);
    }
    while (lo < hi) {
        i128 mid = lo + (hi - lo) / 2;
        if (count(mid) >= k) hi = mid; else lo = mid + 1;
    }
    i128 threshold = lo, answer = 0; int64 used = 0;
    for (int i = 0; i < n; ++i) {
        int64 x = 0;
        if (threshold - 1 >= a[i] + b[i])
            x = min<i128>(cap[i], (threshold - 1 - b[i] + a[i]) / (2 * a[i]));
        used += x; answer += (i128)a[i] * x * x + (i128)b[i] * x;
    }
    answer += (i128)(k - used) * threshold;
    cout << show(answer) << '\n';
}
"""

ALLOC_PY = r"""import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, k = data[:2]
    machines = [tuple(data[i : i + 3]) for i in range(2, 3 * n + 2, 3)]
    if sum(cap for _, _, cap in machines) < k:
        print("IMPOSSIBLE")
        return

    def count(threshold):
        result = 0
        for a, b, cap in machines:
            if threshold >= a + b:
                result += min(cap, (threshold - b + a) // (2 * a))
            if result >= k:
                return k
        return result

    lo, hi = -4 * 10**18, 4 * 10**18
    while lo < hi:
        mid = (lo + hi) // 2
        if count(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
    threshold = lo
    used = answer = 0
    for a, b, cap in machines:
        x = 0
        if threshold - 1 >= a + b:
            x = min(cap, (threshold - 1 - b + a) // (2 * a))
        used += x
        answer += a * x * x + b * x
    print(answer + (k - used) * threshold)


if __name__ == "__main__":
    main()
"""


MATRIX_CPP = DINIC_CPP.replace(
    "int n, m; if (!(cin >> n >> m)) return 0;",
    "int rows, cols, m; if (!(cin >> rows >> cols >> m)) return 0;\n    int n = rows + cols + 2;",
).replace(
    "int ss = n, tt = n + 1; Dinic dinic(n + 2);\n    vector<int64> balance(n);\n    for (int i = 0, u, v; i < m; ++i) {\n        int64 low, high; cin >> u >> v >> low >> high; --u; --v;\n        dinic.add_edge(u, v, high - low);\n        balance[u] -= low; balance[v] += low;\n    }",
    """int source = rows + cols, sink = source + 1, ss = n, tt = n + 1;
    Dinic dinic(n + 2); vector<int64> balance(n); int64 total = 0;
    auto bounded = [&](int u, int v, int64 low, int64 high) {
        dinic.add_edge(u, v, high - low); balance[u] -= low; balance[v] += low;
    };
    for (int i = 0; i < rows; ++i) { int64 demand; cin >> demand; bounded(source, i, demand, demand); total += demand; }
    for (int j = 0; j < cols; ++j) { int64 low, high; cin >> low >> high; bounded(rows + j, sink, low, high); }
    for (int i = 0, r, c; i < m; ++i) { cin >> r >> c; bounded(--r, rows + --c, 0, 1); }
    bounded(sink, source, total, total);""",
)

MATRIX_PY = (
    r"""import collections
import sys
"""
    + DINIC_PY.split("import sys\n", 1)[1].split("\ndef main():", 1)[0]
    + r"""

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    rows, cols, m = data[:3]
    at = 3
    demands = data[at : at + rows]
    at += rows
    bounds = []
    for _ in range(cols):
        bounds.append(tuple(data[at : at + 2]))
        at += 2
    n = rows + cols + 2
    source, sink, ss, tt = rows + cols, rows + cols + 1, n, n + 1
    dinic = Dinic(n + 2)
    balance = [0] * n

    def bounded(u, v, low, high):
        dinic.add_edge(u, v, high - low)
        balance[u] -= low
        balance[v] += low

    total = sum(demands)
    for r, demand in enumerate(demands):
        bounded(source, r, demand, demand)
    for c, (low, high) in enumerate(bounds):
        bounded(rows + c, sink, low, high)
    for _ in range(m):
        r, c = data[at : at + 2]
        at += 2
        bounded(r - 1, rows + c - 1, 0, 1)
    bounded(sink, source, total, total)
    need = 0
    for v, value in enumerate(balance):
        if value > 0:
            dinic.add_edge(ss, v, value)
            need += value
        elif value < 0:
            dinic.add_edge(v, tt, -value)
    print("YES" if dinic.flow(ss, tt) == need else "NO")


if __name__ == "__main__":
    main()
"""
)


CONVEX_QUOTA_CPP = MCF_CPP_CORE + r"""
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, p, m; if (!(cin >> n >> p >> m)) return 0;
    vector<int> low(p), high(p), a(p); int required = 0, max_a = 0;
    for (int j = 0; j < p; ++j) cin >> low[j] >> high[j] >> a[j], required += low[j], max_a = max(max_a, a[j]);
    struct Choice { int w, j, profit; }; vector<Choice> choices(m); int max_profit = 0;
    for (auto &[w, j, profit] : choices) cin >> w >> j >> profit, --w, --j, max_profit = max(max_profit, profit);
    int s = n + p, t = s + 1; MCF mcf(t + 1);
    for (int w = 0; w < n; ++w) mcf.add_edge(s, w, 1, 0);
    for (auto [w, j, profit] : choices) mcf.add_edge(w, n + j, 1, -profit);
    int64 big = (int64)(n + 1) * (max_profit + 2LL * max_a * n + 1);
    vector<pair<int, int>> mandatory;
    for (int j = 0; j < p; ++j) for (int k = 1; k <= high[j]; ++k) {
        int64 cost = (int64)a[j] * (2LL * k - 1);
        auto ref = mcf.add_edge(n + j, t, 1, cost - (k <= low[j] ? big : 0));
        if (k <= low[j]) mandatory.push_back(ref);
    }
    auto [sent, cost] = mcf.flow(s, t, n); bool ok = sent == n;
    for (auto [u, id] : mandatory) ok &= mcf.g[u][id].cap == 0;
    if (!ok) cout << "IMPOSSIBLE\n"; else cout << -cost - big * required << '\n';
}
"""

CONVEX_QUOTA_PY = MCF_PY_CORE + r"""

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, p, m = data[:3]
    at = 3
    projects = []
    for _ in range(p):
        projects.append(tuple(data[at : at + 3]))
        at += 3
    choices = []
    max_profit = 0
    for _ in range(m):
        w, j, profit = data[at : at + 3]
        at += 3
        choices.append((w - 1, j - 1, profit))
        max_profit = max(max_profit, profit)
    s, t = n + p, n + p + 1
    mcf = MCF(t + 1)
    for w in range(n):
        mcf.add_edge(s, w, 1, 0)
    for w, j, profit in choices:
        mcf.add_edge(w, n + j, 1, -profit)
    max_a = max(a for _, _, a in projects)
    big = (n + 1) * (max_profit + 2 * max_a * n + 1)
    mandatory = []
    for j, (low, high, a) in enumerate(projects):
        for k in range(1, high + 1):
            ref = mcf.add_edge(n + j, t, 1, a * (2 * k - 1) - (big if k <= low else 0))
            if k <= low:
                mandatory.append(ref)
    sent, cost = mcf.flow(s, t, n)
    ok = sent == n and all(mcf.g[u][i][1] == 0 for u, i in mandatory)
    print(-cost - big * sum(low for low, _, _ in projects) if ok else "IMPOSSIBLE")


if __name__ == "__main__":
    main()
"""


PROBLEMS = {
    70: [
        (
            "a_bounded_circulation",
            "A. Bounded Circulation",
            "circulation",
            DINIC_CPP,
            DINIC_PY,
        ),
        (
            "b_exact_cost_shipment",
            "B. Exact-Cost Shipment",
            "shipment",
            SHIP_CPP,
            SHIP_PY,
        ),
        ("c_quota_assignment", "C. Quota Assignment", "quota", QUOTA_CPP, QUOTA_PY),
    ],
    71: [
        ("a_monotone_l1", "A. Monotone L1 Repair", "monotone", MONO_CPP, MONO_PY),
        ("b_exact_red_mst", "B. Exact Red Spanning Tree", "mst", MST_CPP, MST_PY),
        (
            "c_convex_allocation",
            "C. Massive Convex Allocation",
            "allocation",
            ALLOC_CPP,
            ALLOC_PY,
        ),
    ],
    72: [
        ("a_exam_room_bounds", "A. Exam Room Bounds", "matrix", MATRIX_CPP, MATRIX_PY),
        ("b_night_delivery", "B. Night Delivery", "shipment", SHIP_CPP, SHIP_PY),
        ("c_team_quota_profit", "C. Team Quota Profit", "quota", QUOTA_CPP, QUOTA_PY),
        ("d_monotone_signal", "D. Monotone Signal", "monotone", MONO_CPP, MONO_PY),
        ("e_exact_discount_tree", "E. Exact Discount Tree", "mst", MST_CPP, MST_PY),
        (
            "f_congested_team_assignment",
            "F. Congested Team Assignment",
            "convex_quota",
            CONVEX_QUOTA_CPP,
            CONVEX_QUOTA_PY,
        ),
    ],
}

SECTION_NAMES = {
    70: "Bounded And Minimum-Cost Flows",
    71: "Discrete Convexity And Lagrangian Optimization",
    72: "Master+ Flow And Convex Optimization Mixed Contest",
}

SECTION_DIRS = {
    70: "70_bounded_min_cost_flows",
    71: "71_discrete_convex_lagrangian",
    72: "72_master_flow_convex_mixed",
}

STATEMENTS = {
    "circulation": """You are given a directed graph. Edge `i` must carry an integer flow between its lower and upper bounds. At every vertex, total incoming flow must equal total outgoing flow. Print `YES` if such a circulation exists, otherwise `NO`.

## Input
`n m`, followed by `m` lines `u v low high`. Parallel edges are allowed.

`1 <= n <= 200`, `0 <= m <= 2000`, `0 <= low <= high <= 10^9`.

## Sample
```text
3 3
1 2 2 4
2 3 1 3
3 1 2 5
```
```text
YES
```""",
    "shipment": """Send exactly `F` units from `s` to `t` through a directed network. An edge has an integer capacity and a cost per unit. Find the minimum total cost, or print `IMPOSSIBLE` when fewer than `F` units can be sent.

Costs may be negative, but the input graph contains no reachable negative-cost directed cycle with positive residual capacity before any flow is sent.

## Input
`n m F`, then `s t`, followed by `m` lines `u v capacity cost`.

`2 <= n <= 200`, `0 <= m <= 2000`, `0 <= F <= 200`, `0 <= capacity <= 200`, `|cost| <= 10^6`.

## Sample
```text
4 5 3
1 4
1 2 2 1
1 3 2 4
2 3 1 -2
2 4 2 3
3 4 2 1
```
```text
9
```""",
    "quota": """Assign every worker to exactly one eligible project. Project `j` must receive between `low[j]` and `high[j]` workers. An eligible assignment has a profit; maximize total profit, or print `IMPOSSIBLE`.

## Input
`n p m`; `p` lines `low high`; then `m` distinct lines `worker project profit`.

`1 <= n,p <= 200`, `0 <= m <= 20000`, `0 <= profit <= 10^6`.

## Sample
```text
3 2 5
1 2
1 2
1 1 8
1 2 4
2 1 5
2 2 9
3 1 7
```
```text
24
```""",
    "monotone": """Replace the integer sequence `a` by any nondecreasing integer sequence `b`. Minimize `sum |a[i]-b[i]|` and print the minimum cost.

## Input
`n`, followed by `n` integers.

`1 <= n <= 200000`, `|a[i]| <= 10^9`.

## Sample
```text
5
5 1 4 2 7
```
```text
6
```""",
    "mst": """Each edge of a connected undirected weighted graph is red or blue. Find the minimum weight of a spanning tree containing exactly `k` red edges, or print `IMPOSSIBLE`.

## Input
`n m k`, followed by `m` lines `u v weight color`, where `color` is `R` or `B`.

`2 <= n <= 200`, `n-1 <= m <= 5000`, `0 <= k < n`, `|weight| <= 10^9`.

## Sample
```text
4 5 2
1 2 3 R
2 3 2 B
3 4 4 R
1 4 8 B
1 3 6 R
```
```text
9
```""",
    "allocation": """Allocate exactly `K` indistinguishable units among `n` machines. Machine `i` receives an integer `x[i]` with `0 <= x[i] <= cap[i]` and costs `a[i]*x[i]^2 + b[i]*x[i]`, where `a[i] > 0`. Print the minimum total cost, or `IMPOSSIBLE` if total capacity is too small.

## Input
`n K`, followed by `n` lines `a b cap`.

`1 <= n <= 200000`, `0 <= K,cap[i] <= 10^14`, `1 <= a[i] <= 10^6`, `|b[i]| <= 10^12`. The answer fits a signed 128-bit integer.

## Sample
```text
3 5
1 0 4
2 -1 3
3 2 5
```
```text
15
```""",
    "matrix": """There are `R` exam groups and `C` rooms. Group `r` needs exactly `need[r]` distinct rooms, and room `c` must be used by between `low[c]` and `high[c]` groups. Only listed group-room pairs are allowed. Print whether a valid selection exists.

## Input
`R C E`; one line with the `R` needs; `C` lines `low high`; then `E` allowed pairs `r c`.

`1 <= R,C <= 200`, `0 <= E <= 20000`.

## Sample
```text
2 3 5
2 1
1 1
1 2
0 2
1 1
1 2
2 2
2 3
1 3
```
```text
YES
```""",
    "convex_quota": """Assign every specialist to one eligible team. Team `j` must receive between `low[j]` and `high[j]` specialists. Assignment `(i,j)` earns `profit`, while a team of final size `x` pays congestion cost `a[j]*x^2`. Maximize profit minus total congestion, or print `IMPOSSIBLE`.

## Input
`n p m`; `p` lines `low high a`; then `m` lines `specialist team profit`.

`1 <= n,p <= 250`, `0 <= m <= 30000`, `0 <= a,profit <= 10^6`.

## Sample
```text
3 2 5
1 2 1
1 2 2
1 1 8
1 2 7
2 1 6
2 2 10
3 1 7
```
```text
19
```""",
}

SAMPLES = {
    "circulation": ("3 3\n1 2 2 4\n2 3 1 3\n3 1 2 5\n", "YES\n"),
    "shipment": ("4 5 3\n1 4\n1 2 2 1\n1 3 2 4\n2 3 1 -2\n2 4 2 3\n3 4 2 1\n", "9\n"),
    "quota": ("3 2 5\n1 2\n1 2\n1 1 8\n1 2 4\n2 1 5\n2 2 9\n3 1 7\n", "24\n"),
    "monotone": ("5\n5 1 4 2 7\n", "6\n"),
    "mst": ("4 5 2\n1 2 3 R\n2 3 2 B\n3 4 4 R\n1 4 8 B\n1 3 6 R\n", "9\n"),
    "allocation": ("3 5\n1 0 4\n2 -1 3\n3 2 5\n", "15\n"),
    "matrix": ("2 3 5\n2 1\n1 1\n1 2\n0 2\n1 1\n1 2\n2 2\n2 3\n1 3\n", "YES\n"),
    "convex_quota": (
        "3 2 5\n1 2 1\n1 2 2\n1 1 8\n1 2 7\n2 1 6\n2 2 10\n3 1 7\n",
        "19\n",
    ),
}


LESSONS = {
    70: r"""# From lower bounds to imbalance

Ordinary flow starts every edge at zero. A lower bound `low(e)` forbids that.
Pretend the mandatory part has already been sent and write
`flow(e) = low(e) + extra(e)`. The extra flow has capacity
`high(e)-low(e)`, but the mandatory parts leave vertex imbalances.

For every mandatory `low` on `u -> v`, subtract it from `balance[u]` and add
it to `balance[v]`. A positive balance means the vertex has already received
too much and must send that amount through optional residual edges; a negative
balance must receive flow.

# Feasible circulation reduction

Add a super-source `SS` and super-sink `TT`:

- if `balance[v] > 0`, add `SS -> v` with that capacity;
- if `balance[v] < 0`, add `v -> TT` with `-balance[v]` capacity.

A bounded circulation exists exactly when a maximum flow saturates every edge
out of `SS`. Necessity follows by subtracting the lower bounds from any valid
circulation. Sufficiency follows by adding them back to a saturating auxiliary
flow.

For a bounded `s -> t` flow, add a return edge `t -> s`; fixing its lower and
upper bounds to `F` asks for exactly `F` units.

# Minimum-cost augmenting paths

In a residual graph, a forward edge costs `c` and its reverse costs `-c`.
The reverse edge is essential: it lets a later augmentation repair an earlier
choice. Repeatedly augmenting on a cheapest residual `s -> t` path gives a
minimum-cost flow of every attained value.

Negative reverse edges prevent plain Dijkstra. Maintain vertex potentials
`p[v]` such that every residual reduced cost

```text
c'(u,v) = c(u,v) + p[u] - p[v]
```

is nonnegative. Initialize potentials with Bellman--Ford distances when input
costs may be negative. After Dijkstra, set `p[v] += dist[v]` for reached
vertices. The triangle inequality proves that reduced costs stay nonnegative;
edges on the chosen shortest path have reduced cost zero in both residual
directions after reversal.

# Modeling quotas and convex costs

A unit-capacity worker edge enforces “at most once”; sending exactly `n` units
enforces “exactly once.” Project lower and upper quotas are bounded edges.

If using a min-cost-flow implementation without lower bounds, lower slots may
receive a reward `-BIG`. Choose `BIG` larger than the complete range of real
objectives, then verify that all rewarded slots were filled. This is a
lexicographic reduction, not a heuristic.

A separable convex cost can be expanded into increasing marginal costs. Since

```text
a*x^2 + b*x = sum from k=1 to x of (a*(2*k-1)+b),
```

create one unit-capacity edge for every marginal unit when capacities are
small enough.

# Complexity and failure modes

Dinic gives the usual maximum-flow bounds. Successive shortest augmenting path
with binary-heap Dijkstra costs `O(F * E log V)` when at most `F` unit
augmentations occur.

Common errors are reversing the signs of balances, omitting the `t -> s`
return edge, applying Dijkstra before potentials are feasible, updating
potentials for unreachable vertices, or choosing `BIG` without proving a
global objective bound.

# Exercises

A isolates bounded-circulation feasibility. B adds costs, residual repair, and
potentials. C hides both quota feasibility and optimization inside assignment.
Derive each network on paper before reading its editorial.
""",
    71: r"""# Convexity as ordered marginal decisions

Convex optimization in contests often means this discrete statement:

> Taking the next unit becomes no cheaper as more units are already taken.

Once the marginal costs are sorted inside every choice, a large state space
can collapse into heaps, a threshold search, or a penalty parameter.

# Slope trick through isotonic L1 repair

After processing a prefix, regard its optimal cost as a convex piecewise-linear
function of the last chosen value. Adding `|x-a[i]|` inserts a slope change at
`a[i]`. Requiring the sequence to be nondecreasing discards the part of the
function that would need a decreasing final value.

The compact implementation stores left breakpoints in a max-heap. For each
`x`, insert it twice, remove the largest breakpoint `y`, and add `y-x` to the
answer. One copy represents the new absolute-value kink; the second allows the
monotonicity projection to move a previous kink down to `x`. Because `x` was
just inserted, `y >= x`.

The heap is not an unexplained trick: it is a compressed derivative. Its
elements are exactly the points where the slope of the current convex value
function increases.

# Lagrangian relaxation: price the hard count

Suppose a feasible object has original cost `cost(T)` and uses `r(T)` red
edges, but we require `r(T)=k`. Add a price `lambda` per red edge and solve

```text
minimize cost(T) + lambda * r(T).
```

As `lambda` increases, optimal solutions use no more red edges. This monotonic
response permits binary search. For a fixed price, an MST is still obtained by
Kruskal after adding `lambda` to every red edge.

At equal modified weights, run Kruskal once preferring red and once preferring
blue. These give the maximum and minimum red counts among modified-optimal
trees. The graphic-matroid exchange property ensures all intermediate counts
are attainable without changing modified cost. If `k` lies in that interval,

```text
exact answer = modified optimum - lambda*k.
```

Always test global feasibility first: the minimum and maximum possible red
counts among all spanning trees must bracket `k`.

# Huge separable convex allocation

Machine `i` has marginal cost

```text
delta_i(j) = a_i*(2*j-1) + b_i
```

for its `j`-th unit. Each machine contributes a sorted arithmetic progression;
the answer is the sum of the globally smallest `K` marginals. Expanding them
is impossible when capacities are enormous.

Binary-search the smallest threshold `T` for which at least `K` marginals are
at most `T`. Count a machine's qualifying marginals with one division, capped
by its capacity. Sum every marginal strictly below `T`, then take exactly the
remaining number equal to `T`. Strict versus non-strict thresholding is what
handles ties correctly.

# Recognition checklist

1. Write the slow DP or allocation problem.
2. Ask whether its value function is convex or its marginal choices are sorted.
3. Identify the compressed representation: breakpoints, a penalty, or a
   threshold count.
4. Prove monotonicity and tie behavior before binary searching.
5. Keep the original objective separate from the penalized one.

# Exercises

A develops the breakpoint view of slope trick. B requires an exact-count
penalty with rigorous tie handling. C replaces an enormous allocation state
space by a threshold over sorted marginal sequences.
""",
    72: r"""# Contest contract

This six-problem contest mixes Sections 70--71. All statements are local and
self-contained. The order is progressive, but later tasks deliberately hide
the reduction behind assignment, graph, or resource language.

| Problem | Main compression |
|---|---|
| A | lower bounds become vertex imbalances |
| B | reduced costs and potential-based shortest paths |
| C | lower-quota slots plus min-cost assignment |
| D | convex derivative stored as heap breakpoints |
| E | Lagrangian price for an exact color count |
| F | quota flow plus convex marginal-cost edges |

# Suggested contest use

Allow four hours. Before coding, write one sentence naming the conserved
quantity or ordered marginal structure. For E and F, also write how ties or
the forcing constant are certified. Upsolve every task with a tiny brute-force
oracle; these techniques are especially vulnerable to plausible but false
binary-search conditions.

# Exercises

Solve A--F as one contest. The mixed set contains exactly six new local
problems and covers every principal invariant introduced in Sections 70--71.
""",
}


EDITORIAL_NOTES = {
    "circulation": "Subtract every lower bound and accumulate vertex balance. The super-source flow is feasible exactly when all positive balances can be routed to all deficits through the remaining capacities. Add the lower bounds back conceptually. Complexity is one maximum-flow computation.",
    "shipment": "A residual reverse edge permits replacing earlier choices. Initial Bellman--Ford potentials make every reachable reduced cost nonnegative; Dijkstra then finds each cheapest augmentation. Updating reached potentials by their Dijkstra distances preserves feasibility. Stop after exactly F units or report impossibility.",
    "quota": "Send one unit through each worker. Project-to-sink capacity enforces upper quotas. Give the first low[j] parallel slots a reward -BIG, where BIG exceeds every possible difference in real profit, and verify all rewarded slots are saturated. The remaining min-cost objective is precisely negative total profit.",
    "monotone": "The prefix optimum as a function of its final value is convex. Its derivative changes only at stored breakpoints. Adding |x-a| inserts x twice; truncating choices that violate monotonicity removes the largest left breakpoint and charges its displacement. Thus the heap maintains the exact compressed derivative.",
    "mst": "Price every red edge by lambda. Kruskal solves the penalized problem, and the red count is nonincreasing in lambda. Opposite tie rules give the extreme red counts among equally optimal trees. Matroid basis exchange fills the interval between them, so subtracting lambda*k recovers the exact-k objective.",
    "allocation": "The j-th unit on a machine has marginal cost a(2j-1)+b, an increasing arithmetic progression. Binary-search the K-th smallest marginal globally. Take every marginal below the threshold and only as many tied threshold marginals as still needed.",
    "matrix": "Create source-to-group edges fixed at each demand, allowed unit group-to-room edges, room-to-sink bounded edges, and a sink-to-source edge fixed at total demand. This is a bounded circulation, so the balance reduction decides feasibility.",
    "convex_quota": "Worker-to-team edges contribute negative profit. Replace team cost a*x^2 by x unit slots with marginal costs a(2k-1). Reward the mandatory lower-quota slots by -BIG and verify them afterward. A single exact min-cost flow now optimizes assignment and congestion together.",
}

EDITORIAL_DETAILS = {
    "circulation": """## How to find it

The obstacle is that zero flow is no longer a legal starting point. Separate
what is forced from what remains optional: write every edge flow as its lower
bound plus an extra amount. The forced parts no longer conserve flow locally,
so the only missing information is one signed imbalance per vertex.

## Correctness

Given a valid bounded circulation, subtracting every lower bound leaves a flow
within capacities `high-low`. Its imbalance at each vertex is exactly repaired
by the auxiliary super-source and super-sink edges, so all super-source edges
can be saturated. Conversely, a saturating auxiliary flow repairs every
imbalance. Removing the auxiliary edges and adding each lower bound back gives
conservation and respects both bounds. Thus the reduction is equivalent in
both directions.

## Complexity and tests

The transformed graph has `n+2` vertices and `m+O(n)` edges; the cost is one
Dinic maximum-flow run. Test isolated forced edges, `low=high`, parallel edges,
zero bounds, and total balance zero with locally impossible routing.""",
    "shipment": """## How to find it

A greedy cheapest original path fails because a later unit may need to undo an
earlier route. That observation asks for a residual graph: every used edge
creates a reverse edge of opposite cost. We still want shortest augmenting
paths, so potentials are introduced solely to make Dijkstra legal.

## Correctness

Feasible potentials make all reduced residual costs nonnegative, and path
reweighting changes every `s-t` path cost by the same constant. Dijkstra
therefore chooses a truly cheapest residual augmenting path. Updating reached
potentials with shortest reduced distances preserves nonnegative reduced
costs by the triangle inequality. The standard residual optimality criterion
then shows inductively that after each augmentation the current flow has
minimum cost among flows of its value. Hence the state after `F` units is the
required optimum.

## Complexity and tests

With integral capacities, at most `F` augmentations are needed here, for
`O(F E log V)` after the initial shortest-distance computation. Test negative
input edges, a case where a reverse residual edge changes the first choice,
parallel routes, zero requested flow, and insufficient capacity.""",
    "quota": """## How to find it

“Every worker exactly once” naturally means one unit leaving every worker;
eligibility edges encode the choices and their costs are negative profits.
Upper quotas are capacities. To use a plain min-cost-flow implementation for
lower quotas, turn the first `low[j]` project slots into lexicographically
mandatory slots with reward `-BIG`.

## Correctness

Every integral flow of value `n` decomposes into one eligible project choice
per worker, and every assignment yields such a flow. Project capacities enforce
the upper bounds. If a quota-feasible assignment exists, it fills all mandatory
slots. Because `BIG` exceeds the maximum possible difference between two total
profits, every minimum-cost flow first maximizes the number of mandatory slots
filled and only then maximizes real profit. Verifying their saturation rejects
exactly the infeasible instances; removing their constant reward recovers the
true optimum.

## Complexity and tests

There are `O(n+p)` vertices and `O(n+m+p)` edges. Successive shortest paths
take `O(n E log V)`. Test a worker with no choices, tight quotas, infeasible
lower quotas despite sufficient total capacity, and an optimum using a
lower-profit edge to satisfy a project minimum.""",
    "monotone": """## How to find it

Start from the quadratic DP “best prefix cost when the final repaired value is
`x`.” Its value as a function of `x` is convex and piecewise linear. Storing
all values is unnecessary: a convex piecewise-linear function is determined by
the ordered positions where its derivative changes.

## Correctness

The max-heap stores the left breakpoints of the prefix value function. Adding
`|x-a[i]|` introduces two unit slope changes at `a[i]`. The monotonicity
transition takes a prefix minimum over legal previous final values; in the
derivative representation this removes the largest left breakpoint. If that
breakpoint is `y`, moving it to `a[i]` increases the minimum by `y-a[i]`.
These are exactly the two pushes, one pop, and cost update in the code.
Induction over prefixes therefore proves that the accumulated minimum equals
the isotonic L1 optimum.

## Complexity and tests

Each item performs three heap operations, so time is `O(n log n)` and memory
is `O(n)`. Test already sorted, strictly decreasing, repeated values, negative
values, and prefixes whose optimal medians are not unique.""",
    "mst": """## How to find it

The difficult condition is the exact red count; everything else is an MST.
Move that condition into the objective by charging `lambda` for each red edge.
For a fixed charge the solver remains Kruskal, while increasing the charge can
only decrease the red count of an optimum.

## Correctness

Kruskal minimizes `weight + lambda*red`. Among equal modified weights, the two
tie orders return the largest and smallest red counts of modified-optimal
trees. The basis-exchange property of the graphic matroid connects optimal
spanning trees by equal-cost exchanges, changing the red count one step at a
time; consequently every count between those extremes is attainable at the
same modified value. Binary search finds the last integer price whose
red-preferring optimum still uses at least `k` reds. At that boundary `k` is
in the optimal count interval, so subtracting `lambda*k` gives exactly the
minimum original weight with `k` reds.

## Complexity and tests

Each price evaluation sorts `m` edges, and `O(log W)` prices are tested, giving
`O(m log m log W)` here. Test impossible extreme counts, many equal modified
weights, negative weights, all-one-color graphs, and cases with several MSTs.""",
    "allocation": """## How to find it

Expanding `K` units is impossible, but convexity makes the units ordered. The
`j`-th unit on machine `i` costs `a[i](2j-1)+b[i]`; the problem is exactly to
select the globally smallest `K` values from capped arithmetic progressions.

## Correctness

Within one machine, selecting a later marginal without every earlier marginal
can only increase cost, so every optimal selection is a prefix on each
machine. Binary search finds the smallest threshold `T` with at least `K`
available marginals at most `T`. All marginals below `T` must be selected:
replacing one by a larger value cannot improve an optimum. Every remaining
selected marginal can be chosen among values equal to `T`. The construction
therefore selects exactly the global `K` smallest marginals, whose telescoping
sum is the original quadratic objective.

## Complexity and tests

One threshold count is `O(n)` and 128-bit binary search uses `O(log C)` counts;
memory is `O(n)`. Test `K=0`, insufficient capacity, negative first marginals,
many ties at the threshold, and products beyond signed 64-bit range.""",
    "matrix": """## How to find it

Rows and columns are two sides of a bipartite unit-flow model. Row demands are
fixed source-edge flows, room limits are lower/upper sink-edge bounds, and an
allowed pair is a unit middle edge. Fixing the return edge to the total demand
turns the whole construction into a circulation.

## Correctness

A valid selection sends one unit through exactly each selected pair; row and
column constraints become the stated edge bounds, so it produces a feasible
circulation. Conversely, integral max flow makes every middle edge zero or
one. Reading its unit edges gives distinct allowed choices, with exact row
degrees and bounded column degrees. The bounded-circulation equivalence then
decides the instance exactly.

## Complexity and tests

The graph has `R+C+4` vertices and `E+R+C+O(1)` edges. Test duplicate-looking
constraints, a room minimum unreachable from enough groups, zero row demands,
and feasible totals whose allowed-pair structure is nevertheless impossible.""",
    "convex_quota": """## How to find it

This is assignment flow except the price of a team depends on its final load.
Convexity makes the dependence separable: the `k`-th member costs the marginal
`a[j](2k-1)`. Replace one nonlinear team edge by ordered unit slot edges, and
use the lower-quota reward from the quota problem on its first slots.

## Correctness

An integral value-`n` flow chooses one eligible team per specialist. Since a
team's marginal slot costs are nondecreasing, any cheapest flow using `x`
slots uses precisely the first `x`; their sum is `a[j]x^2`. The `-BIG` reward,
chosen larger than the full real-objective range, makes saturation of every
lower-quota slot lexicographically prior to profit and congestion. After the
explicit saturation check, feasible flows and valid assignments correspond
bijectively and have equal real objective, so the returned maximum is exact.

## Complexity and tests

There are `O(n+p)` vertices and `O(m+n+sum high)` edges, with at most `n`
augmentations. Test zero congestion, tight project sizes, a quota forcing an
unprofitable assignment, equal marginal slots, and infeasible eligibility.""",
}


def front(subtitle: str) -> str:
    return f"""---
title: "Competitive Programming"
subtitle: "{subtitle}"
author: "Competitive Programming Course"
format:
  pdf:
    pdf-engine: xelatex
    documentclass: scrreprt
    papersize: a4
    toc: true
    number-sections: true
    colorlinks: true
    geometry: [margin=25mm]
execute: {{enabled: false}}
---

"""


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n")


def build() -> None:
    for section, problems in PROBLEMS.items():
        base = ROOT / "sections" / SECTION_DIRS[section]
        base.mkdir(parents=True, exist_ok=True)
        rows = "\n".join(
            f"- [{title}](problems/{slug}/README.md)" for slug, title, *_ in problems
        )
        write(
            base / "README.md",
            f"# Section {section}: {SECTION_NAMES[section]}\n\n{rows}",
        )
        write(
            base / "PRACTICE.md",
            f"# Section {section} Practice\n\nAll required practice is self-contained:\n\n{rows}",
        )
        names = ", ".join(f'"{p[0]}"' for p in problems)
        check = f'''"""Friendly checker for Section {section}."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from tools.section_checker import run_section_checks
SECTION = Path(__file__).resolve().parent
PROBLEMS = [SECTION / "problems" / name for name in ({names},)]
if __name__ == "__main__":
    raise SystemExit(run_section_checks({section}, PROBLEMS, ROOT))
'''
        write(base / "check.py", check)
        write(
            base / "lesson.qmd",
            front(f"Section {section}: {SECTION_NAMES[section]}") + LESSONS[section],
        )
        editorial = [front(f"Section {section} Editorial: {SECTION_NAMES[section]}")]
        editorial.append(
            "# How to use this editorial\n\nFor each problem, identify the reduction before reading the code. The proof paragraph names the invariant that should have appeared in your own derivation.\n"
        )
        for slug, title, kind, *_ in problems:
            editorial.append(
                f"# {title}\n\n{EDITORIAL_NOTES[kind]}\n\n{EDITORIAL_DETAILS[kind]}\n\n## C++\n\n```cpp\n{{{{< include problems/{slug}/solution.cpp >}}}}\n```\n\n## Python\n\n```python\n{{{{< include problems/{slug}/solution.py >}}}}\n```\n"
            )
        write(base / "editorial.qmd", "\n".join(editorial))
        for slug, title, kind, cpp, py in problems:
            pdir = base / "problems" / slug
            write(pdir / "README.md", f"# {title}\n\n{STATEMENTS[kind]}")
            write(
                pdir / "manifest.json",
                json.dumps(
                    {"title": title, "checker": "tokens", "time_limit_seconds": 6.0},
                    separators=(",", ":"),
                ),
            )
            write(pdir / "solve.cpp", CPP_STUB)
            write(pdir / "solve.py", PY_STUB)
            write(pdir / "solution.cpp", cpp)
            write(pdir / "solution.py", py)
            sample_in, sample_out = SAMPLES[kind]
            write(pdir / "tests" / "sample1.in", sample_in)
            write(pdir / "tests" / "sample1.out", sample_out)
            random = f"""import subprocess
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[5]
raise SystemExit(subprocess.call([sys.executable, str(ROOT / "tools" / "flow_convex_random.py"), "{kind}", *sys.argv[1:]]))
"""
            write(pdir / "tests" / "random_cases.py", random)


if __name__ == "__main__":
    build()
