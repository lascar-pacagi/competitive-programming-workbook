#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        long long target;
        cin >> n >> target;
        vector<long long> values(n);
        for (long long &value : values) cin >> value;

        int left = 0;
        int right = n - 1;
        bool ok = false;
        while (left < right) {
            long long total = values[left] + values[right];
            if (total == target) {
                ok = true;
                break;
            }
            if (total < target) {
                ++left;
            } else {
                --right;
            }
        }
        cout << (ok ? "YES" : "NO") << '\n';
    }

    return 0;
}

