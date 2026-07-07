#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<int> lg(n + 1);
    for (int i = 2; i <= n; i++) lg[i] = lg[i / 2] + 1;
    int K = lg[n] + 1;
    vector<vector<long long>> st(K, vector<long long>(n));
    for (int i = 0; i < n; i++) cin >> st[0][i];
    for (int k = 1; k < K; k++) {
        for (int i = 0; i + (1 << k) <= n; i++) {
            st[k][i] = min(st[k - 1][i], st[k - 1][i + (1 << (k - 1))]);
        }
    }
    while (q--) {
        int l, r;
        cin >> l >> r;
        --l; --r;
        int k = lg[r - l + 1];
        cout << min(st[k][l], st[k][r - (1 << k) + 1]) << '\n';
    }
    return 0;
}
