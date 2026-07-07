#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, k;
    if (!(cin >> n >> m >> k)) return 0;
    vector<long long> a(n), b(m);
    for (auto &x : a) cin >> x;
    for (auto &x : b) cin >> x;
    using State = tuple<long long,int,int>;
    priority_queue<State, vector<State>, greater<State>> pq;
    for (int i = 0; i < n; i++) pq.emplace(a[i] + b[0], i, 0);
    for (int t = 0; t < k; t++) {
        auto [s, i, j] = pq.top();
        pq.pop();
        if (t) cout << ' ';
        cout << s;
        if (j + 1 < m) pq.emplace(a[i] + b[j + 1], i, j + 1);
    }
    cout << '\n';
    return 0;
}
