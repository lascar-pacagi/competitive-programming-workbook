#include <bits/stdc++.h>
using namespace std;

// below[i][j] (x_i < x_j) = points strictly between i and j in x and strictly
// below segment ij.  Around each i, sort the points to its right by slope:
// k lies below segment ij iff slope(i,k) < slope(i,j) and x_k < x_j, a
// dominance count kept with a Fenwick tree over x-ranks.  For a triangle with
// vertices a, b, c sorted by x, the inside count is
//   below(a,b) + below(b,c) - below(a,c)       if b is above segment ac,
//   below(a,c) - below(a,b) - below(b,c) - 1   otherwise (b itself is below).

typedef long long ll;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<ll> x(n), y(n);
    for (int i = 0; i < n; i++) cin >> x[i] >> y[i];
    vector<int> order(n), rank(n);
    iota(order.begin(), order.end(), 0);
    sort(order.begin(), order.end(), [&](int a, int b) { return x[a] < x[b]; });
    for (int r = 0; r < n; r++) rank[order[r]] = r;
    vector<vector<int>> below(n, vector<int>(n, 0));
    vector<int> bit(n + 1);
    for (int i = 0; i < n; i++) {
        vector<int> right;
        for (int j = 0; j < n; j++)
            if (x[j] > x[i]) right.push_back(j);
        sort(right.begin(), right.end(), [&](int a, int b) {
            return (x[a] - x[i]) * (__int128)(y[b] - y[i]) - (__int128)(y[a] - y[i]) * (x[b] - x[i]) > 0;
        });
        fill(bit.begin(), bit.end(), 0);
        for (int j : right) {
            int s = 0;
            for (int k = rank[j]; k > 0; k -= k & -k) s += bit[k];
            below[i][j] = s;
            for (int k = rank[j] + 1; k <= n; k += k & -k) bit[k]++;
        }
    }
    auto under = [&](int a, int b) { return x[a] < x[b] ? below[a][b] : below[b][a]; };
    string out;
    while (q--) {
        int t[3];
        cin >> t[0] >> t[1] >> t[2];
        for (int& v : t) v--;
        sort(t, t + 3, [&](int a, int b) { return x[a] < x[b]; });
        int a = t[0], b = t[1], c = t[2];
        __int128 cr = (__int128)(x[c] - x[a]) * (y[b] - y[a]) - (__int128)(y[c] - y[a]) * (x[b] - x[a]);
        int ans = cr > 0 ? under(a, b) + under(b, c) - under(a, c) : under(a, c) - under(a, b) - under(b, c) - 1;
        out += to_string(ans) + '\n';
    }
    cout << out;
}
