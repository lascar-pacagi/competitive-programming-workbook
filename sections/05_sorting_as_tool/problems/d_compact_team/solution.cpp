#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<long long> a(n);
        for (long long& x : a) cin >> x;
        sort(a.begin(), a.end());
        long long answer = a[k - 1] - a[0];
        for (int left = 1; left + k <= n; ++left) {
            answer = min(answer, a[left + k - 1] - a[left]);
        }
        cout << answer << '\n';
    }
}
