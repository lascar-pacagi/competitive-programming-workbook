#include <bits/stdc++.h>
using namespace std;

// Every path is a point (A, B) = (sum a, sum b) and has length A t + B on day
// t, so the answers are the upper envelope of all path points.  Only O(n log n)
// candidate points are needed.  After splitting high-degree vertices with
// zero-cost dummy vertices (degree <= 3), pick an edge that splits the current
// component evenly.  Paths through that edge are Minkowski sums of the two
// sides' upper hulls of root-to-vertex points, shifted by the edge itself;
// paths not through it are handled recursively.

typedef long long ll;
typedef pair<ll, ll> P;

__int128 cross(P o, P a, P b) {
    return (__int128)(a.first - o.first) * (b.second - o.second) -
           (__int128)(a.second - o.second) * (b.first - o.first);
}

// Upper hull restricted to the part useful for t >= 0: A increasing, B
// decreasing, slopes strictly decreasing.
vector<P> usefulHull(vector<P> pts) {
    sort(pts.begin(), pts.end());
    vector<P> h;
    for (const P& p : pts) {
        while (!h.empty() && h.back().first == p.first) h.pop_back();  // same A, larger B wins
        while (h.size() >= 2 && cross(h[h.size() - 2], h.back(), p) >= 0) h.pop_back();
        h.push_back(p);
    }
    size_t best = 0;
    for (size_t i = 1; i < h.size(); i++)
        if (h[i].second >= h[best].second) best = i;
    return vector<P>(h.begin() + best, h.end());
}

vector<P> minkowski(const vector<P>& a, const vector<P>& b) {
    vector<P> out = {{a[0].first + b[0].first, a[0].second + b[0].second}};
    size_t i = 0, j = 0;
    while (i + 1 < a.size() || j + 1 < b.size()) {
        bool takeA;
        if (i + 1 == a.size()) takeA = false;
        else if (j + 1 == b.size()) takeA = true;
        else {
            P da = {a[i + 1].first - a[i].first, a[i + 1].second - a[i].second};
            P db = {b[j + 1].first - b[j].first, b[j + 1].second - b[j].second};
            // larger slope dB/dA first
            takeA = (__int128)da.second * db.first >= (__int128)db.second * da.first;
        }
        if (takeA) {
            out.push_back({out.back().first + a[i + 1].first - a[i].first, out.back().second + a[i + 1].second - a[i].second});
            i++;
        } else {
            out.push_back({out.back().first + b[j + 1].first - b[j].first, out.back().second + b[j + 1].second - b[j].second});
            j++;
        }
    }
    return out;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<array<ll, 3>>> raw(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v;
        ll a, b;
        cin >> u >> v >> a >> b;
        --u;
        --v;
        raw[u].push_back({v, a, b});
        raw[v].push_back({u, a, b});
    }
    // Binarize: rooted at 0, give each vertex at most two children.
    vector<int> eu, ev;
    vector<ll> ea, eb;
    int V = n;
    auto addEdge = [&](int u, int v, ll a, ll b) {
        eu.push_back(u);
        ev.push_back(v);
        ea.push_back(a);
        eb.push_back(b);
    };
    {
        vector<int> parent(n, -1), stack = {0};
        parent[0] = 0;
        while (!stack.empty()) {
            int v = stack.back();
            stack.pop_back();
            vector<array<ll, 3>> kids;
            for (auto& e : raw[v])
                if (parent[e[0]] < 0) {
                    parent[e[0]] = v;
                    kids.push_back(e);
                    stack.push_back(e[0]);
                }
            int cur = v;
            int k = kids.size();
            for (int i = 0; i < k; i++) {
                addEdge(cur, kids[i][0], kids[i][1], kids[i][2]);
                if (k - i > 2) {  // keep at most two children per vertex
                    int d = V++;
                    addEdge(cur, d, 0, 0);
                    cur = d;
                }
            }
        }
    }
    int E = eu.size();
    vector<vector<int>> adj(V);
    for (int e = 0; e < E; e++) {
        adj[eu[e]].push_back(e);
        adj[ev[e]].push_back(e);
    }
    vector<char> removed(E, 0);
    vector<P> candidates = {{0, 0}};
    vector<int> sz(V), parentEdge(V), order;
    vector<ll> accA(V), accB(V);

    auto collect = [&](int root, vector<int>& out) {  // vertices of component
        out.clear();
        out.push_back(root);
        parentEdge[root] = -1;
        for (size_t i = 0; i < out.size(); i++) {
            int v = out[i];
            for (int e : adj[v]) {
                if (removed[e] || e == parentEdge[v]) continue;
                int w = eu[e] ^ ev[e] ^ v;
                parentEdge[w] = e;
                out.push_back(w);
            }
        }
    };
    auto sidePoints = [&](int root) {
        vector<int> vs;
        collect(root, vs);
        vector<P> pts;
        pts.reserve(vs.size());
        accA[root] = accB[root] = 0;
        for (int v : vs) {
            if (v != root) {
                int e = parentEdge[v], p = eu[e] ^ ev[e] ^ v;
                accA[v] = accA[p] + ea[e];
                accB[v] = accB[p] + eb[e];
            }
            pts.push_back({accA[v], accB[v]});
        }
        return usefulHull(pts);
    };

    vector<int> work = {0}, vs;
    while (!work.empty()) {
        int root = work.back();
        work.pop_back();
        collect(root, vs);
        int total = vs.size();
        if (total == 1) continue;
        for (int i = total - 1; i >= 0; i--) {
            int v = vs[i];
            sz[v] = 1;
            for (int e : adj[v])
                if (!removed[e] && e != parentEdge[v]) sz[v] += sz[eu[e] ^ ev[e] ^ v];
        }
        int bestEdge = -1, bestVal = INT_MAX, child = -1;
        for (int i = 1; i < total; i++) {
            int v = vs[i];
            int value = max(sz[v], total - sz[v]);
            if (value < bestVal) bestVal = value, bestEdge = parentEdge[v], child = v;
        }
        int other = eu[bestEdge] ^ ev[bestEdge] ^ child;
        removed[bestEdge] = 1;
        vector<P> h1 = sidePoints(child), h2 = sidePoints(other);
        vector<P> sum = minkowski(h1, h2);
        for (auto& p : sum) candidates.push_back({p.first + ea[bestEdge], p.second + eb[bestEdge]});
        work.push_back(child);
        work.push_back(other);
    }
    vector<P> hull = usefulHull(candidates);
    string out;
    size_t k = 0;
    for (ll t = 0; t < m; t++) {
        while (k + 1 < hull.size() && hull[k + 1].first * t + hull[k + 1].second >= hull[k].first * t + hull[k].second) k++;
        out += to_string(hull[k].first * t + hull[k].second);
        out += t + 1 < m ? ' ' : '\n';
    }
    cout << out;
}
