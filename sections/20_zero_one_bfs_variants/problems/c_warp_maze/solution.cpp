#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> grid(n);
    pair<int,int> start{-1,-1}, goal{-1,-1};
    for (int r = 0; r < n; r++) {
        cin >> grid[r];
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == 'S') start = {r,c};
            if (grid[r][c] == 'G') goal = {r,c};
        }
    }
    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(m, INF));
    deque<pair<int,int>> dq;
    dist[start.first][start.second] = 0;
    dq.push_back(start);
    int wr[4] = {1,-1,0,0}, wc[4] = {0,0,1,-1};
    while (!dq.empty()) {
        auto [r,c] = dq.front(); dq.pop_front();
        int d = dist[r][c];
        for (int i = 0; i < 4; i++) {
            int nr = r + wr[i], nc = c + wc[i];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m || grid[nr][nc] == '#') continue;
            if (d < dist[nr][nc]) {
                dist[nr][nc] = d;
                dq.push_front({nr,nc});
            }
        }
        for (int dr = -2; dr <= 2; dr++) {
            for (int dc = -2; dc <= 2; dc++) {
                int nr = r + dr, nc = c + dc;
                if (nr < 0 || nr >= n || nc < 0 || nc >= m || grid[nr][nc] == '#') continue;
                if (d + 1 < dist[nr][nc]) {
                    dist[nr][nc] = d + 1;
                    dq.push_back({nr,nc});
                }
            }
        }
    }
    int ans = dist[goal.first][goal.second];
    cout << (ans == INF ? -1 : ans) << '\n';
    return 0;
}

