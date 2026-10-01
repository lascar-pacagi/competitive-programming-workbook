#include <bits/stdc++.h>
using namespace std;

// Split the path u -> v at w = lca(u, v) into the upward part u..w and the
// downward part below w.  An occurrence inside the upward part, read upward
// from its lowest vertex x, means that the root-to-x string ends with the
// reversed pattern; one inside the downward part, ending at vertex y, means
// that the root-to-y string ends with the pattern.  Run one Aho--Corasick
// automaton (all patterns and their reversals) down the tree: "ends with" is
// membership of the vertex's state in a fail-tree subtree, so each part is a
// difference of two root-path counts, answered offline by a DFS with a Fenwick
// tree over fail-tree Euler positions.  Occurrences crossing the junction lie
// within |p| - 1 vertices of w on each side and are found by KMP.

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    string label;
    cin >> label;
    vector<vector<int>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    vector<int> qu(q), qv(q);
    vector<string> pats(q);
    for (int i = 0; i < q; i++) cin >> qu[i] >> qv[i] >> pats[i];

    vector<int> parent(n + 1, 0), depth(n + 1, 0), order = {1};
    {
        vector<char> seen(n + 1, 0);
        seen[1] = 1;
        for (size_t i = 0; i < order.size(); i++) {
            int v = order[i];
            for (int w : adj[v])
                if (!seen[w]) {
                    seen[w] = 1;
                    parent[w] = v;
                    depth[w] = depth[v] + 1;
                    order.push_back(w);
                }
        }
    }
    int LOG = 1;
    while ((1 << LOG) <= n) LOG++;
    vector<vector<int>> up(LOG, vector<int>(n + 1));
    up[0] = parent;
    for (int k = 1; k < LOG; k++)
        for (int v = 0; v <= n; v++) up[k][v] = up[k - 1][up[k - 1][v]];
    auto ancestorAtDepth = [&](int v, int d) {
        int diff = depth[v] - d;
        for (int k = 0; diff; k++, diff >>= 1)
            if (diff & 1) v = up[k][v];
        return v;
    };
    auto lca = [&](int a, int b) {
        if (depth[a] < depth[b]) swap(a, b);
        a = ancestorAtDepth(a, depth[b]);
        if (a == b) return a;
        for (int k = LOG - 1; k >= 0; k--)
            if (up[k][a] != up[k][b]) a = up[k][a], b = up[k][b];
        return parent[a];
    };

    // Aho--Corasick with full transition table.
    vector<array<int, 26>> go(1);
    go[0].fill(-1);
    auto insert = [&](const string& w) {
        int s = 0;
        for (char ch : w) {
            int c = ch - 'a';
            if (go[s][c] < 0) {
                go[s][c] = go.size();
                go.emplace_back();
                go.back().fill(-1);
            }
            s = go[s][c];
        }
        return s;
    };
    vector<int> nodeFwd(q), nodeRev(q);
    for (int i = 0; i < q; i++) {
        nodeFwd[i] = insert(pats[i]);
        nodeRev[i] = insert(string(pats[i].rbegin(), pats[i].rend()));
    }
    int T = go.size();
    vector<int> fail(T, 0), bfs = {0};
    for (size_t h = 0; h < bfs.size(); h++) {
        int s = bfs[h];
        for (int c = 0; c < 26; c++) {
            int t = go[s][c];
            if (t >= 0) {
                fail[t] = s ? go[fail[s]][c] : 0;
                bfs.push_back(t);
            } else {
                go[s][c] = s ? go[fail[s]][c] : 0;
            }
        }
    }
    vector<vector<int>> fchildren(T);
    for (int t = 1; t < T; t++) fchildren[fail[t]].push_back(t);
    vector<int> tin(T), tout(T);
    {
        int timer = 0;
        vector<pair<int, int>> stack = {{0, 0}};
        while (!stack.empty()) {
            auto& [s, i] = stack.back();
            if (i == 0) tin[s] = ++timer;
            if (i < (int)fchildren[s].size()) {
                int t = fchildren[s][i++];
                stack.push_back({t, 0});
            } else {
                tout[s] = timer;
                stack.pop_back();
            }
        }
    }

    struct Event {
        int node, sign, id;
    };
    vector<vector<Event>> events(n + 1);
    vector<long long> answer(q, 0);
    for (int i = 0; i < q; i++) {
        int u = qu[i], v = qv[i];
        const string& p = pats[i];
        int L = p.size(), l = lca(u, v), dl = depth[l];
        if (depth[u] >= dl + L - 1) {
            int w = ancestorAtDepth(u, dl + L - 1);
            events[u].push_back({nodeRev[i], 1, i});
            if (parent[w]) events[parent[w]].push_back({nodeRev[i], -1, i});
        }
        if (v != l && depth[v] >= dl + L) {
            int w = ancestorAtDepth(v, dl + L);
            events[v].push_back({nodeFwd[i], 1, i});
            events[parent[w]].push_back({nodeFwd[i], -1, i});
        }
        if (L >= 2 && v != l) {
            int a = min(L - 1, depth[u] - dl + 1), b = min(L - 1, depth[v] - dl);
            if (a + b >= L) {
                string text;
                for (int x = ancestorAtDepth(u, dl + a - 1);; x = parent[x]) {
                    text += label[x - 1];
                    if (x == l) break;
                }
                string right;
                for (int y = ancestorAtDepth(v, dl + b); y != l; y = parent[y]) right += label[y - 1];
                text.append(right.rbegin(), right.rend());
                vector<int> pf(L, 0);
                for (int idx = 1, k = 0; idx < L; idx++) {
                    while (k && p[idx] != p[k]) k = pf[k - 1];
                    if (p[idx] == p[k]) k++;
                    pf[idx] = k;
                }
                int k = 0;
                for (int idx = 0; idx < (int)text.size(); idx++) {
                    while (k && text[idx] != p[k]) k = pf[k - 1];
                    if (text[idx] == p[k]) k++;
                    if (k == L) {
                        int start = idx - L + 1;
                        if (start < a && a <= idx) answer[i]++;
                        k = pf[k - 1];
                    }
                }
            }
        }
    }

    vector<int> bit(T + 1, 0);
    auto bitAdd = [&](int i, int x) {
        for (; i <= T; i += i & -i) bit[i] += x;
    };
    auto bitSum = [&](int i) {
        int s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    };
    vector<int> state(n + 1, 0);
    vector<pair<int, int>> stack = {{1, 0}};
    while (!stack.empty()) {
        auto& [v, i] = stack.back();
        if (i == 0) {
            int from = v == 1 ? 0 : state[parent[v]];
            state[v] = go[from][label[v - 1] - 'a'];
            bitAdd(tin[state[v]], 1);
            for (const Event& e : events[v])
                answer[e.id] += (long long)e.sign * (bitSum(tout[e.node]) - bitSum(tin[e.node] - 1));
        }
        if (i < (int)adj[v].size()) {
            int w = adj[v][i++];
            if (w != parent[v]) stack.push_back({w, 0});
        } else {
            bitAdd(tin[state[v]], -1);
            stack.pop_back();
        }
    }
    string out;
    for (long long x : answer) out += to_string(x) + '\n';
    cout << out;
}
