#include <bits/stdc++.h>
using namespace std;

// Root the tree at 1 and let vertex v own the edge to its parent.  Sweep r
// upward and paint the root path of r with colour r.  The union of the root
// paths of labels l..r is exactly the set of edges whose current colour is
// >= l; subtracting the root path of LCA(l..r) leaves the Steiner tree.
// With heavy-light decomposition every root path is a sequence of chain
// prefixes, so each chain keeps a stack of equally coloured blocks and a
// Fenwick tree over colours stores the total edge length of each colour.
// LCA(l..r) is the LCA of the labels with smallest and largest DFS entry time.

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<vector<pair<int, ll>>> adj(n + 1);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        ll w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }
    vector<int> parent(n + 1, 0), order, heavy(n + 1, 0), sz(n + 1, 1);
    vector<ll> up(n + 1, 0), depth(n + 1, 0);
    vector<int> level(n + 1, 0);
    order.reserve(n);
    {
        vector<int> stack = {1};
        parent[1] = 0;
        vector<char> seen(n + 1, 0);
        seen[1] = 1;
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            order.push_back(v);
            for (auto [w, len] : adj[v])
                if (!seen[w]) {
                    seen[w] = 1;
                    parent[w] = v;
                    up[w] = len;
                    depth[w] = depth[v] + len;
                    level[w] = level[v] + 1;
                    stack.push_back(w);
                }
        }
    }
    for (int i = n - 1; i > 0; i--) sz[parent[order[i]]] += sz[order[i]];
    for (int i = n - 1; i > 0; i--) {
        int v = order[i], p = parent[v];
        if (!heavy[p] || sz[v] > sz[heavy[p]]) heavy[p] = v;
    }
    // Positions: each heavy chain occupies a contiguous block, head first.
    vector<int> head(n + 1), pos(n + 1), tin(n + 1), tout(n + 1);
    {
        int cur = 0;
        vector<int> stack = {1};
        head[1] = 1;
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            for (int x = v; x; x = heavy[x]) {
                if (x != v) head[x] = head[v];
                pos[x] = cur++;
                for (auto [w, len] : adj[x])
                    if (w != parent[x] && w != heavy[x]) {
                        head[w] = w;
                        stack.push_back(w);
                    }
            }
        }
    }
    // Euler entry times for the range-LCA trick.
    {
        int timer = 0;
        vector<pair<int, int>> stack = {{1, 0}};
        while (!stack.empty()) {
            auto& [v, i] = stack.back();
            if (i == 0) tin[v] = timer++;
            if (i < (int)adj[v].size()) {
                int w = adj[v][i++].first;
                if (w != parent[v]) stack.push_back({w, 0});
            } else {
                tout[v] = timer;
                stack.pop_back();
            }
        }
    }
    auto lca = [&](int a, int b) {
        while (head[a] != head[b]) {
            if (level[head[a]] < level[head[b]]) swap(a, b);
            a = parent[head[a]];
        }
        return pos[a] < pos[b] ? a : b;
    };
    vector<ll> prefix(n + 1, 0);  // prefix[k] = sum of up[] over positions < k
    {
        vector<ll> byPos(n);
        for (int v = 1; v <= n; v++) byPos[pos[v]] = up[v];
        for (int k = 0; k < n; k++) prefix[k + 1] = prefix[k] + byPos[k];
    }
    // Sparse tables over labels for min / max entry time.
    int LOG = 1;
    while ((1 << LOG) <= n) LOG++;
    vector<vector<int>> mnT(LOG, vector<int>(n + 1)), mxT(LOG, vector<int>(n + 1));
    for (int v = 1; v <= n; v++) mnT[0][v] = mxT[0][v] = v;
    for (int k = 1; k < LOG; k++)
        for (int v = 1; v + (1 << k) - 1 <= n; v++) {
            int a = mnT[k - 1][v], b = mnT[k - 1][v + (1 << (k - 1))];
            mnT[k][v] = tin[a] < tin[b] ? a : b;
            a = mxT[k - 1][v];
            b = mxT[k - 1][v + (1 << (k - 1))];
            mxT[k][v] = tin[a] > tin[b] ? a : b;
        }
    auto rangeLca = [&](int l, int r) {
        int k = 31 - __builtin_clz(r - l + 1);
        int a = mnT[k][l], b = mnT[k][r - (1 << k) + 1];
        int lo = tin[a] < tin[b] ? a : b;
        a = mxT[k][l];
        b = mxT[k][r - (1 << k) + 1];
        int hi = tin[a] > tin[b] ? a : b;
        return lca(lo, hi);
    };

    vector<ll> bit(n + 1, 0);
    auto bitAdd = [&](int i, ll x) {
        for (; i <= n; i += i & -i) bit[i] += x;
    };
    auto bitSum = [&](int i) {
        ll s = 0;
        for (; i > 0; i -= i & -i) s += bit[i];
        return s;
    };
    struct Block {
        int from, to, colour;  // positions [from, to] on one chain
    };
    vector<vector<Block>> blocks(n + 1);  // per chain head; top block = back()
    auto paint = [&](int v, int colour) {
        while (v) {
            int h = head[v], a = pos[h], b = pos[v];
            auto& st = blocks[h];
            while (!st.empty() && st.back().to <= b) {
                Block& blk = st.back();
                bitAdd(blk.colour, -(prefix[blk.to + 1] - prefix[blk.from]));
                st.pop_back();
            }
            if (!st.empty() && st.back().from <= b) {
                Block& blk = st.back();
                bitAdd(blk.colour, -(prefix[b + 1] - prefix[blk.from]));
                blk.from = b + 1;
            }
            st.push_back({a, b, colour});
            bitAdd(colour, prefix[b + 1] - prefix[a]);
            v = parent[h];
        }
    };

    vector<int> ql(q), qr(q), byR(q);
    for (int i = 0; i < q; i++) cin >> ql[i] >> qr[i];
    iota(byR.begin(), byR.end(), 0);
    sort(byR.begin(), byR.end(), [&](int a, int b) { return qr[a] < qr[b]; });
    vector<ll> answer(q);
    int painted = 0;
    for (int id : byR) {
        while (painted < qr[id]) {
            painted++;
            paint(painted, painted);
        }
        ll covered = bitSum(n) - bitSum(ql[id] - 1);
        answer[id] = covered - depth[rangeLca(ql[id], qr[id])];
    }
    string out;
    for (ll x : answer) out += to_string(x) + '\n';
    cout << out;
}
