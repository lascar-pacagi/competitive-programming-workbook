#include <bits/stdc++.h>
using namespace std;

// Binary search the answer d.  Sort all 2n candidate sites; literal k means
// "the beacon owning site k is placed at site k", and its negation is the
// owner's other site.  Choosing site k forbids every other site closer than d,
// a contiguous block of the sorted order.  A segment tree whose leaves point to
// "the owner uses its other site" turns each block into O(log n) implication
// edges, and Tarjan's SCC algorithm decides the resulting 2-SAT instance.

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    int S = 2 * n;
    vector<pair<long long, int>> sites(S);
    for (int i = 0; i < n; i++) {
        long long a, b;
        cin >> a >> b;
        sites[2 * i] = {a, i};
        sites[2 * i + 1] = {b, i};
    }
    sort(sites.begin(), sites.end());
    vector<long long> pos(S);
    vector<int> partner(S), firstOf(n, -1);
    for (int k = 0; k < S; k++) {
        pos[k] = sites[k].first;
        int owner = sites[k].second;
        if (firstOf[owner] < 0) {
            firstOf[owner] = k;
        } else {
            partner[k] = firstOf[owner];
            partner[firstOf[owner]] = k;
        }
    }
    int size = 1;
    while (size < S) size *= 2;
    int V = S + 2 * size;  // literals, then segment-tree nodes
    auto treeNode = [&](int t) { return S + t; };

    vector<int> head(V), nxt, to;
    auto feasible = [&](long long d) {
        fill(head.begin(), head.end(), -1);
        nxt.clear();
        to.clear();
        auto add = [&](int a, int b) {
            to.push_back(b);
            nxt.push_back(head[a]);
            head[a] = to.size() - 1;
        };
        for (int t = 1; t < size; t++) {
            add(treeNode(t), treeNode(2 * t));
            add(treeNode(t), treeNode(2 * t + 1));
        }
        for (int k = 0; k < S; k++) add(treeNode(size + k), partner[k]);
        auto cover = [&](int k, int l, int r) {  // k -> every leaf in [l, r)
            for (l += size, r += size; l < r; l >>= 1, r >>= 1) {
                if (l & 1) add(k, treeNode(l++));
                if (r & 1) add(k, treeNode(--r));
            }
        };
        for (int k = 0; k < S; k++) {
            int lo = lower_bound(pos.begin(), pos.end(), pos[k] - d + 1) - pos.begin();
            int hi = lower_bound(pos.begin(), pos.end(), pos[k] + d) - pos.begin();
            cover(k, lo, k);
            cover(k, k + 1, hi);
        }
        // Iterative Tarjan.
        vector<int> index(V, -1), low(V), comp(V, -1), stackV, callV, callE;
        vector<char> onStack(V, 0);
        int counter = 0, comps = 0;
        for (int s = 0; s < V; s++) {
            if (index[s] >= 0) continue;
            callV.push_back(s);
            callE.push_back(head[s]);
            index[s] = low[s] = counter++;
            stackV.push_back(s);
            onStack[s] = 1;
            while (!callV.empty()) {
                int v = callV.back();
                int& e = callE.back();
                if (e >= 0) {
                    int w = to[e];
                    e = nxt[e];
                    if (index[w] < 0) {
                        index[w] = low[w] = counter++;
                        stackV.push_back(w);
                        onStack[w] = 1;
                        callV.push_back(w);
                        callE.push_back(head[w]);
                    } else if (onStack[w]) {
                        low[v] = min(low[v], index[w]);
                    }
                    continue;
                }
                callV.pop_back();
                callE.pop_back();
                if (!callV.empty()) low[callV.back()] = min(low[callV.back()], low[v]);
                if (low[v] == index[v]) {
                    while (true) {
                        int w = stackV.back();
                        stackV.pop_back();
                        onStack[w] = 0;
                        comp[w] = comps;
                        if (w == v) break;
                    }
                    comps++;
                }
            }
        }
        for (int k = 0; k < S; k++)
            if (comp[k] == comp[partner[k]]) return false;
        return true;
    };
    long long lo = 0, hi = pos.back() - pos.front() + 1;  // lo feasible, hi not
    while (hi - lo > 1) {
        long long mid = (lo + hi) / 2;
        if (feasible(mid)) lo = mid;
        else hi = mid;
    }
    cout << lo << '\n';
}
