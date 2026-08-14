#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n, m;
        cin >> n >> m;
        vector<int> values(n);
        for (int &value : values) cin >> value;

        vector<int> count(m + 1, 0);
        int missing = m;
        int left = 0;
        int answer = n + 1;
        for (int right = 0; right < n; ++right) {
            if (count[values[right]]++ == 0) --missing;
            while (missing == 0) {
                answer = min(answer, right - left + 1);
                if (--count[values[left]] == 0) ++missing;
                ++left;
            }
        }
        cout << (answer == n + 1 ? -1 : answer) << '\n';
    }
    return 0;
}
