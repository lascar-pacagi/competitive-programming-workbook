#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<ll>> a(n, vector<ll>(m));
    for (auto& row : a) for (ll& x : row) cin >> x;
    const ll NEG = -(1LL << 62);
    vector<array<ll, 2>> previous(m, {NEG, NEG});
    for (int r = 0; r < n; ++r) {
        vector<array<ll, 2>> current(m, {NEG, NEG});
        for (int c = 0; c < m; ++c) {
                if (r == 0 && c == 0) current[c][0] = a[r][c];
                for (int used = 0; used < 2; ++used) {
                    ll best = current[c][used];
                    if (r && previous[c][used] != NEG) {
                        best = max(best, previous[c][used] + a[r][c]);
                    }
                    if (c && current[c - 1][used] != NEG) {
                        best = max(best, current[c - 1][used] + a[r][c]);
                    }
                current[c][used] = best;
            }
            if (r && c && previous[c - 1][0] != NEG) {
                current[c][1] = max(current[c][1], previous[c - 1][0] + a[r][c]);
            }
        }
        previous.swap(current);
    }
    cout << (previous[m - 1][1] == NEG ? -1 : previous[m - 1][1]) << '\n';
}
