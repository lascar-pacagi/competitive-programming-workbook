#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> graph(n);
    for (int i = 0; i < m; i++) {
        int from, to;
        cin >> from >> to;
        graph[from - 1].push_back(to - 1);
    }

    vector<int> match_right(n, -1);
    function<bool(int, vector<int>&)> augment = [&](int left, vector<int>& seen) {
        for (int right : graph[left]) {
            if (seen[right]) continue;
            seen[right] = true;
            if (match_right[right] == -1 || augment(match_right[right], seen)) {
                match_right[right] = left;
                return true;
            }
        }
        return false;
    };

    int matching = 0;
    for (int left = 0; left < n; left++) {
        vector<int> seen(n, false);
        matching += augment(left, seen);
    }
    cout << n - matching << '\n';
    return 0;
}
