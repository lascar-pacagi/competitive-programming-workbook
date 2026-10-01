#include <bits/stdc++.h>
using namespace std;

// Subdivide every link u->v into u->x->v.  Removing the link cuts exactly the
// vertices dominated by x, so the answer is the number of original stations in
// x's subtree of the dominator tree (Lengauer--Tarjan, path compression).

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    int total = n + m;
    vector<int> head(total, -1), nxt(2 * m), to(2 * m);
    int edgeCount = 0;
    auto addEdge = [&](int a, int b) {
        to[edgeCount] = b;
        nxt[edgeCount] = head[a];
        head[a] = edgeCount++;
    };
    vector<pair<int, int>> links(m);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        --u;
        --v;
        links[i] = {u, v};
        addEdge(u, n + i);
        addEdge(n + i, v);
    }

    // Iterative DFS from station 1; vertices are renamed to preorder indices.
    vector<int> dfn(total, -1), vertexAt, parent;
    vertexAt.reserve(total);
    parent.reserve(total);
    {
        vector<pair<int, int>> stack;
        dfn[0] = 0;
        vertexAt.push_back(0);
        parent.push_back(-1);
        stack.push_back({0, head[0]});
        while (!stack.empty()) {
            auto& [v, e] = stack.back();
            if (e < 0) {
                stack.pop_back();
                continue;
            }
            int w = to[e];
            e = nxt[e];
            if (dfn[w] < 0) {
                dfn[w] = vertexAt.size();
                vertexAt.push_back(w);
                parent.push_back(dfn[v]);
                stack.push_back({w, head[w]});
            }
        }
    }
    int T = vertexAt.size();
    // Predecessor lists in preorder numbering.
    vector<int> predStart(T + 1, 0), predList;
    for (int a = 0; a < total; a++)
        if (dfn[a] >= 0)
            for (int e = head[a]; e >= 0; e = nxt[e]) predStart[dfn[to[e]] + 1]++;
    for (int i = 0; i < T; i++) predStart[i + 1] += predStart[i];
    predList.resize(predStart[T]);
    {
        vector<int> fill(predStart.begin(), predStart.end() - 1);
        for (int a = 0; a < total; a++)
            if (dfn[a] >= 0)
                for (int e = head[a]; e >= 0; e = nxt[e])
                    predList[fill[dfn[to[e]]]++] = dfn[a];
    }

    vector<int> sdom(T), idom(T, 0), anc(T, -1), best(T), bucketHead(T, -1), bucketNext(T, -1);
    iota(sdom.begin(), sdom.end(), 0);
    iota(best.begin(), best.end(), 0);
    vector<int> path;
    auto eval = [&](int v) {
        if (anc[v] < 0) return v;
        path.clear();
        int x = v;
        while (anc[anc[x]] >= 0) {
            path.push_back(x);
            x = anc[x];
        }
        for (int i = (int)path.size() - 1; i >= 0; i--) {
            int y = path[i];
            if (sdom[best[anc[y]]] < sdom[best[y]]) best[y] = best[anc[y]];
            anc[y] = anc[anc[y]];
        }
        return best[v];
    };
    for (int w = T - 1; w >= 1; w--) {
        for (int i = predStart[w]; i < predStart[w + 1]; i++) {
            int u = eval(predList[i]);
            if (sdom[u] < sdom[w]) sdom[w] = sdom[u];
        }
        bucketNext[w] = bucketHead[sdom[w]];
        bucketHead[sdom[w]] = w;
        int p = parent[w];
        anc[w] = p;
        for (int v = bucketHead[p]; v >= 0; v = bucketNext[v]) {
            int u = eval(v);
            idom[v] = sdom[u] < sdom[v] ? u : p;
        }
        bucketHead[p] = -1;
    }
    for (int w = 1; w < T; w++)
        if (idom[w] != sdom[w]) idom[w] = idom[idom[w]];

    vector<long long> below(T, 0);
    for (int w = T - 1; w >= 0; w--) {
        if (vertexAt[w] < n) below[w]++;
        if (w) below[idom[w]] += below[w];
    }
    string out;
    for (int i = 0; i < m; i++) {
        int x = dfn[n + i];
        out += to_string(x < 0 ? 0 : below[x]);
        out += '\n';
    }
    cout << out;
}
