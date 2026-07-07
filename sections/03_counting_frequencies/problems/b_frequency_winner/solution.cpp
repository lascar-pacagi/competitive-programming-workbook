#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        unordered_map<int, int> freq;
        freq.reserve(2 * n + 1);
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            ++freq[x];
        }

        int best_value = 0;
        int best_count = -1;
        for (auto [value, count] : freq) {
            if (count > best_count || (count == best_count && value < best_value)) {
                best_value = value;
                best_count = count;
            }
        }
        cout << best_value << ' ' << best_count << '\n';
    }

    return 0;
}

