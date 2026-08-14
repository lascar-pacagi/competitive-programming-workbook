#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n;
        cin >> n;
        unordered_map<long long, long long> freq;
        freq.reserve(2 * n + 1);
        long long answer = 0;
        for (int i = 0; i < n; ++i) {
            long long value;
            cin >> value;
            answer += freq[value];
            ++freq[value];
        }
        cout << answer << '\n';
    }
    return 0;
}
