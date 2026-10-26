#include <bits/stdc++.h>
using namespace std;
using ll = long long;

struct Line {
    ll slope = 0, intercept = 0;
    ll value(ll x) const { return slope * x + intercept; }
};

struct LiChao {
    vector<ll> x;
    vector<Line> tree;
    vector<bool> occupied;
    explicit LiChao(vector<ll> coordinates) : x(move(coordinates)) {
        sort(x.begin(), x.end());
        x.erase(unique(x.begin(), x.end()), x.end());
        tree.resize(4 * x.size());
        occupied.assign(4 * x.size(), false);
    }
    void add(Line line, int node, int left, int right) {
        if (!occupied[node]) {
            occupied[node] = true;
            tree[node] = line;
            return;
        }
        int middle = (left + right) / 2;
        if (line.value(x[middle]) < tree[node].value(x[middle]))
            swap(line, tree[node]);
        if (left == right) return;
        if (line.value(x[left]) < tree[node].value(x[left]))
            add(line, 2 * node, left, middle);
        else if (line.value(x[right]) < tree[node].value(x[right]))
            add(line, 2 * node + 1, middle + 1, right);
    }
    void add(Line line) { add(line, 1, 0, int(x.size()) - 1); }
    ll query(ll at) const {
        ll answer = 1LL << 62;
        int node = 1, left = 0, right = int(x.size()) - 1;
        while (true) {
            if (occupied[node]) answer = min(answer, tree[node].value(at));
            if (left == right) return answer;
            int middle = (left + right) / 2;
            if (at <= x[middle]) { node *= 2; right = middle; }
            else { node = 2 * node + 1; left = middle + 1; }
        }
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<pair<ll, ll>> stations(n);
    for (auto& [position, power] : stations) cin >> position >> power;
    vector<ll> queries(q);
    for (ll& x : queries) cin >> x;
    LiChao hull(queries);
    for (auto [position, power] : stations)
        hull.add({-2 * position, position * position - power});
    for (ll x : queries) cout << -hull.query(x) - x * x << '\n';
}
