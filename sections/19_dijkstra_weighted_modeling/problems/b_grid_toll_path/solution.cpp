#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<long long>> cost(n, vector<long long>(m));
    for (auto &row : cost) for (long long &x : row) cin >> x;
    const long long INF = (1LL << 62);
    vector<vector<long long>> dist(n, vector<long long>(m, INF));
    using State = tuple<long long,int,int>;
    priority_queue<State, vector<State>, greater<State>> pq;
    dist[0][0] = cost[0][0];
    pq.push({dist[0][0], 0, 0});
    int dr[4] = {1, -1, 0, 0};
    int dc[4] = {0, 0, 1, -1};
    while (!pq.empty()) {
        auto [d, r, c] = pq.top(); pq.pop();
        if (d != dist[r][c]) continue;
        if (r == n - 1 && c == m - 1) break;
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            long long nd = d + cost[nr][nc];
            if (nd < dist[nr][nc]) {
                dist[nr][nc] = nd;
                pq.push({nd, nr, nc});
            }
        }
    }
    cout << dist[n - 1][m - 1] << '\n';
    return 0;
}

