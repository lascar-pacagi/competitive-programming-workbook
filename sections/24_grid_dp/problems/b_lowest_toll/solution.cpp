#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    const long long INF = (1LL << 62);
    vector<long long> prev(m, INF), cur(m, INF);
    for (int r = 0; r < n; r++) {
        fill(cur.begin(), cur.end(), INF);
        for (int c = 0; c < m; c++) {
            long long x;
            cin >> x;
            if (r == 0 && c == 0) {
                cur[c] = x;
            } else {
                long long best = prev[c];
                if (c) best = min(best, cur[c - 1]);
                cur[c] = best + x;
            }
        }
        swap(prev, cur);
    }
    cout << prev[m - 1] << '\n';
    return 0;
}

