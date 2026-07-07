#include <bits/stdc++.h>
using namespace std;

struct Parent {
    int r = -1;
    int c = -1;
    char move = '?';
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<string> grid(n);
    pair<int, int> start{-1, -1}, goal{-1, -1};
    for (int r = 0; r < n; r++) {
        cin >> grid[r];
        for (int c = 0; c < m; c++) {
            if (grid[r][c] == 'S') start = {r, c};
            if (grid[r][c] == 'G') goal = {r, c};
        }
    }

    const vector<int> dr = {1, 0, 0, -1};
    const vector<int> dc = {0, -1, 1, 0};
    const vector<char> mv = {'D', 'L', 'R', 'U'};

    vector<vector<int>> dist(n, vector<int>(m, -1));
    vector<vector<Parent>> parent(n, vector<Parent>(m));
    queue<pair<int, int>> q;
    dist[start.first][start.second] = 0;
    q.push(start);
    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m) continue;
            if (grid[nr][nc] == '#' || dist[nr][nc] != -1) continue;
            dist[nr][nc] = dist[r][c] + 1;
            parent[nr][nc] = {r, c, mv[i]};
            q.push({nr, nc});
        }
    }

    auto [gr, gc] = goal;
    if (dist[gr][gc] == -1) {
        cout << "NO\n";
        return 0;
    }

    string path;
    for (pair<int, int> cur = goal; cur != start;) {
        Parent p = parent[cur.first][cur.second];
        path.push_back(p.move);
        cur = {p.r, p.c};
    }
    reverse(path.begin(), path.end());
    cout << "YES\n" << path.size() << '\n' << path << '\n';
    return 0;
}

