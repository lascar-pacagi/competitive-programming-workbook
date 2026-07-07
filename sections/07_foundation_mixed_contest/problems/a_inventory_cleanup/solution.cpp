#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        unordered_map<int, int> freq;
        freq.reserve(2 * n + 1);
        for (int i = 0; i < n; ++i) {
            int color;
            cin >> color;
            ++freq[color];
        }
        vector<int> counts;
        counts.reserve(freq.size());
        for (auto [color, count] : freq) {
            counts.push_back(count);
        }
        sort(counts.begin(), counts.end());
        int remove_groups = max(0, static_cast<int>(counts.size()) - k);
        int answer = 0;
        for (int i = 0; i < remove_groups; ++i) {
            answer += counts[i];
        }
        cout << answer << '\n';
    }

    return 0;
}

