#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<string> grid(n);
    vector<vector<int>> portals(26);
    int start = -1, goal = -1;

    for (int r = 0; r < n; ++r) {
        cin >> grid[r];
        for (int c = 0; c < m; ++c) {
            int id = r * m + c;
            char cell = grid[r][c];
            if (cell == 'S') start = id;
            if (cell == 'G') goal = id;
            if ('a' <= cell && cell <= 'z') {
                portals[cell - 'a'].push_back(id);
            }
        }
    }

    const int INF = 1e9;
    vector<int> dist(n * m, INF);
    vector<char> expanded(26, false);
    deque<int> dq;
    dist[start] = 0;
    dq.push_back(start);
    const int dr[4] = {1, -1, 0, 0};
    const int dc[4] = {0, 0, 1, -1};

    while (!dq.empty()) {
        int id = dq.front();
        dq.pop_front();
        int r = id / m;
        int c = id % m;
        int current = dist[id];

        char cell = grid[r][c];
        if ('a' <= cell && cell <= 'z' && !expanded[cell - 'a']) {
            expanded[cell - 'a'] = true;
            for (int other : portals[cell - 'a']) {
                if (current < dist[other]) {
                    dist[other] = current;
                    dq.push_front(other);
                }
            }
        }

        for (int direction = 0; direction < 4; ++direction) {
            int nr = r + dr[direction];
            int nc = c + dc[direction];
            if (nr < 0 || nr >= n || nc < 0 || nc >= m || grid[nr][nc] == '#') {
                continue;
            }
            int next = nr * m + nc;
            if (current + 1 < dist[next]) {
                dist[next] = current + 1;
                dq.push_back(next);
            }
        }
    }

    cout << (dist[goal] == INF ? -1 : dist[goal]) << '\n';
}
