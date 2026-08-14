#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<vector<long long>> grid(n, vector<long long>(m));
    for (auto& row : grid)
        for (long long& value : row)
            cin >> value;

    const long long INF = 1LL << 62;
    vector<long long> need(m, INF);

    for (int row = n - 1; row >= 0; --row) {
        for (int column = m - 1; column >= 0; --column) {
            if (row == n - 1 && column == m - 1) {
                need[column] = max(0LL, -grid[row][column]);
                continue;
            }

            long long after = INF;
            if (row + 1 < n)
                after = min(after, need[column]);
            if (column + 1 < m)
                after = min(after, need[column + 1]);
            need[column] = max(0LL, after - grid[row][column]);
        }
    }

    cout << need[0] << '\n';
}
