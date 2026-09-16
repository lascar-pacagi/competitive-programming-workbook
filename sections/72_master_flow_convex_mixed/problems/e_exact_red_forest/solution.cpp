#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct DSU {
    vector<int> parent, size;
    explicit DSU(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int value) {
        while (value != parent[value]) value = parent[value];
        return value;
    }
    bool unite(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return false;
        if (size[a] < size[b]) swap(a, b);
        parent[b] = a;
        size[a] += size[b];
        return true;
    }
};

struct Edge { int u, v, red; ll weight; };

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, components, wanted;
    cin >> n >> m >> components >> wanted;
    int edge_count = n - components;
    vector<Edge> edges(m);
    for (Edge& edge : edges) {
        char color;
        cin >> edge.u >> edge.v >> edge.weight >> color;
        --edge.u;
        --edge.v;
        edge.red = color == 'R';
    }
    if (edge_count == 0) {
        cout << (wanted == 0 ? "0\n" : "IMPOSSIBLE\n");
        return 0;
    }

    auto run = [&](ll penalty, bool prefer_red) {
        vector<int> order(m);
        iota(order.begin(), order.end(), 0);
        sort(order.begin(), order.end(), [&](int i, int j) {
            ll first = edges[i].weight + penalty * edges[i].red;
            ll second = edges[j].weight + penalty * edges[j].red;
            if (first != second) return first < second;
            return prefer_red ? edges[i].red > edges[j].red
                              : edges[i].red < edges[j].red;
        });
        DSU dsu(n);
        int used = 0;
        int red = 0;
        ll value = 0;
        for (int index : order) {
            const Edge& edge = edges[index];
            if (!dsu.unite(edge.u, edge.v)) continue;
            ++used;
            red += edge.red;
            value += edge.weight + penalty * edge.red;
            if (used == edge_count) break;
        }
        return tuple<int, int, ll>{used, red, value};
    };

    const ll BOUND = 400'000'000'000'000LL;
    auto [minimum_used, minimum_red, ignored1] = run(BOUND, false);
    auto [maximum_used, maximum_red, ignored2] = run(-BOUND, true);
    if (minimum_used != edge_count || maximum_used != edge_count
        || wanted < minimum_red || wanted > maximum_red) {
        cout << "IMPOSSIBLE\n";
        return 0;
    }

    ll low = -BOUND;
    ll high = BOUND;
    while (low < high) {
        ll middle = low + (high - low + 1) / 2;
        auto [used, red, value] = run(middle, true);
        if (red >= wanted)
            low = middle;
        else
            high = middle - 1;
    }
    auto [used, red, modified] = run(low, true);
    cout << modified - low * wanted << '\n';
}
