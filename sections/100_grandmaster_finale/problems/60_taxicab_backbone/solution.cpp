#include <bits/stdc++.h>
using namespace std;

// The bottleneck between two beacons equals the largest edge on their path in
// a minimum spanning tree of the complete Manhattan graph.  Only O(n)
// candidate edges are needed: for each of the eight octants around a point,
// its nearest neighbour in that octant.  Four coordinate transforms plus a
// Fenwick tree of prefix minima find them.  Queries are answered while
// Kruskal merges components, moving the smaller query list each time.

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<long long> x(n), y(n);
    for (int i = 0; i < n; i++) cin >> x[i] >> y[i];

    vector<tuple<long long, int, int>> edges;
    edges.reserve(4 * (size_t)n);
    vector<long long> px = x, py = y;
    vector<int> order(n);
    for (int dir = 0; dir < 4; dir++) {
        if (dir == 1 || dir == 3)
            for (int i = 0; i < n; i++) swap(px[i], py[i]);
        else if (dir == 2)
            for (int i = 0; i < n; i++) px[i] = -px[i];
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int a, int b) {
            return px[a] != px[b] ? px[a] < px[b] : py[a] < py[b];
        });
        vector<long long> keys(n);
        for (int i = 0; i < n; i++) keys[i] = py[i] - px[i];
        vector<long long> sortedKeys = keys;
        sort(sortedKeys.begin(), sortedKeys.end());
        sortedKeys.erase(unique(sortedKeys.begin(), sortedKeys.end()), sortedKeys.end());
        int K = sortedKeys.size();
        // Fenwick over reversed key order: prefix = all keys >= given key.
        vector<long long> bestValue(K + 1, LLONG_MAX);
        vector<int> bestId(K + 1, -1);
        for (int t = n - 1; t >= 0; t--) {
            int i = order[t];
            int pos = lower_bound(sortedKeys.begin(), sortedKeys.end(), keys[i]) - sortedKeys.begin();
            int r = K - pos;  // 1-based index in reversed order
            long long value = LLONG_MAX;
            int id = -1;
            for (int k = r; k > 0; k -= k & -k)
                if (bestValue[k] < value) value = bestValue[k], id = bestId[k];
            if (id >= 0) edges.emplace_back(llabs(x[i] - x[id]) + llabs(y[i] - y[id]), i, id);
            long long mine = px[i] + py[i];
            for (int k = r; k <= K; k += k & -k)
                if (mine < bestValue[k]) bestValue[k] = mine, bestId[k] = i;
        }
    }
    sort(edges.begin(), edges.end());

    vector<long long> answer(q, -1);
    vector<vector<int>> pending(n);
    vector<int> qa(q), qb(q);
    for (int i = 0; i < q; i++) {
        cin >> qa[i] >> qb[i];
        --qa[i];
        --qb[i];
        if (qa[i] == qb[i]) {
            answer[i] = 0;
        } else {
            pending[qa[i]].push_back(i);
            pending[qb[i]].push_back(i);
        }
    }
    vector<int> parent(n);
    iota(parent.begin(), parent.end(), 0);
    auto find = [&](int v) {
        while (parent[v] != v) v = parent[v] = parent[parent[v]];
        return v;
    };
    for (auto& [w, a, b] : edges) {
        a = find(a);
        b = find(b);
        if (a == b) continue;
        if (pending[a].size() > pending[b].size()) swap(a, b);
        // Queries of the smaller side either finish now or move to b.
        for (int id : pending[a]) {
            if (answer[id] >= 0) continue;
            int other = find(qa[id]) == a ? find(qb[id]) : find(qa[id]);
            if (other == b) answer[id] = w;
            else pending[b].push_back(id);
        }
        vector<int>().swap(pending[a]);
        parent[a] = b;
    }
    string out;
    for (long long v : answer) out += to_string(v) + '\n';
    cout << out;
}
