#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        long long limit;
        cin >> n >> limit;
        vector<long long> values(n);
        for (long long &value : values) cin >> value;

        int left = 0;
        long long total = 0;
        int best_len = 0;
        int best_start = 0;
        for (int right = 0; right < n; ++right) {
            total += values[right];
            while (left <= right && total > limit) {
                total -= values[left];
                ++left;
            }
            int length = right - left + 1;
            int start = left + 1;
            if (length > best_len || (length == best_len && length > 0 && start < best_start)) {
                best_len = length;
                best_start = start;
            }
        }
        cout << best_len << ' ' << best_start << '\n';
    }

    return 0;
}

