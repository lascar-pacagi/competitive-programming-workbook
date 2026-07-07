#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> grid(n);
    for (auto &row : grid) cin >> row;
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(m, INF));
    deque<pair<int,int>> dq;
    dist[0][0] = 0;
    dq.push_back({0, 0});
    int dr[4] = {1, -1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    char ch[4] = {'D', 'U', 'L', 'R'};
    while (!dq.empty()) {
        auto [r, c] = dq.front(); dq.pop_front();
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            int w = (grid[r][c] == ch[i] ? 0 : 1);
            int nd = dist[r][c] + w;
            if (nd < dist[nr][nc]) {
                dist[nr][nc] = nd;
                if (w == 0) dq.push_front({nr, nc});
                else dq.push_back({nr, nc});
            }
        }
    }
    cout << dist[n - 1][m - 1] << '\n';
    return 0;
}

