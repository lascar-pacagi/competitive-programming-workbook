#include <bits/stdc++.h>
using namespace std;

struct Edge { int u, v, weight; };
struct PersistentNode { int left = 0, right = 0, count = 0; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, q;
    cin >> n >> m >> q;
    vector<int> value(n), coordinates;
    for (int &x : value) cin >> x;
    coordinates = value;
    sort(coordinates.begin(), coordinates.end());
    coordinates.erase(unique(coordinates.begin(), coordinates.end()), coordinates.end());

    vector<Edge> edges(m);
    for (Edge &edge : edges) {
        cin >> edge.u >> edge.v >> edge.weight;
        --edge.u;
        --edge.v;
    }
    sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {
        return a.weight < b.weight;
    });

    int capacity = 2 * n + 1;
    vector<int> dsu(capacity), tree_parent(capacity, -1), merge_weight(capacity, INT_MIN);
    vector<array<int, 2>> children(capacity, array<int, 2>{-1, -1});
    iota(dsu.begin(), dsu.end(), 0);
    auto find = [&](auto &&self, int x) -> int {
        return dsu[x] == x ? x : dsu[x] = self(self, dsu[x]);
    };
    int nodes = n;
    for (Edge edge : edges) {
        int first = find(find, edge.u);
        int second = find(find, edge.v);
        if (first == second) continue;
        int parent = nodes++;
        merge_weight[parent] = edge.weight;
        children[parent] = {first, second};
        tree_parent[first] = tree_parent[second] = parent;
        dsu[first] = dsu[second] = parent;
        dsu[parent] = parent;
    }

    vector<int> roots;
    for (int node = 0; node < nodes; ++node)
        if (tree_parent[node] == -1) roots.push_back(node);
    vector<int> left(nodes), right(nodes), leaf_order;
    leaf_order.reserve(n);
    int timer = 0;
    for (int root : roots) {
        vector<pair<int, bool>> stack{{root, false}};
        while (!stack.empty()) {
            auto [node, exit] = stack.back();
            stack.pop_back();
            if (exit) {
                right[node] = timer;
                continue;
            }
            left[node] = timer;
            stack.push_back({node, true});
            if (node < n) {
                leaf_order.push_back(node);
                ++timer;
            } else {
                stack.push_back({children[node][1], false});
                stack.push_back({children[node][0], false});
            }
        }
    }

    int log = max(1, static_cast<int>(bit_width(static_cast<unsigned>(nodes))));
    vector<vector<int>> up(log, vector<int>(nodes));
    for (int node = 0; node < nodes; ++node)
        up[0][node] = tree_parent[node] == -1 ? node : tree_parent[node];
    for (int bit = 1; bit < log; ++bit)
        for (int node = 0; node < nodes; ++node)
            up[bit][node] = up[bit - 1][up[bit - 1][node]];

    vector<PersistentNode> segment(1);
    segment.reserve(static_cast<size_t>(n) * (bit_width(static_cast<unsigned>(n)) + 2));
    auto insert = [&](auto &&self, int previous, int low, int high, int position) -> int {
        int current = segment.size();
        segment.push_back(segment[previous]);
        ++segment[current].count;
        if (high - low == 1) return current;
        int middle = (low + high) / 2;
        if (position < middle)
            segment[current].left = self(self, segment[previous].left, low, middle, position);
        else
            segment[current].right = self(self, segment[previous].right, middle, high, position);
        return current;
    };
    vector<int> prefix_root(n + 1);
    for (int i = 0; i < n; ++i) {
        int compressed = lower_bound(coordinates.begin(), coordinates.end(),
                                     value[leaf_order[i]]) - coordinates.begin();
        prefix_root[i + 1] = insert(insert, prefix_root[i], 0, coordinates.size(), compressed);
    }

    while (q--) {
        int vertex, threshold, k;
        cin >> vertex >> threshold >> k;
        int component = --vertex;
        for (int bit = log - 1; bit >= 0; --bit) {
            int ancestor = up[bit][component];
            if (ancestor != component && merge_weight[ancestor] <= threshold)
                component = ancestor;
        }
        int a = prefix_root[right[component]], b = prefix_root[left[component]];
        int low = 0, high = coordinates.size();
        while (high - low > 1) {
            int count_left = segment[segment[a].left].count
                           - segment[segment[b].left].count;
            int middle = (low + high) / 2;
            if (k <= count_left) {
                a = segment[a].left;
                b = segment[b].left;
                high = middle;
            } else {
                k -= count_left;
                a = segment[a].right;
                b = segment[b].right;
                low = middle;
            }
        }
        cout << coordinates[low] << '\n';
    }
}
