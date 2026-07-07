#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, target;
        cin >> n >> target;
        unordered_map<int, long long> seen;
        seen.reserve(2 * n + 1);
        long long answer = 0;
        for (int i = 0; i < n; ++i) {
            int value;
            cin >> value;
            auto it = seen.find(target - value);
            if (it != seen.end()) {
                answer += it->second;
            }
            ++seen[value];
        }
        cout << answer << '\n';
    }

    return 0;
}

