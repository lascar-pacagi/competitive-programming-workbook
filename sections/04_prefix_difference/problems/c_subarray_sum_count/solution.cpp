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
        unordered_map<long long, long long> freq;
        freq.reserve(2 * n + 1);
        freq[0] = 1;
        long long prefix = 0;
        long long answer = 0;
        for (int i = 0; i < n; ++i) {
            long long x;
            cin >> x;
            prefix += x;
            auto it = freq.find(prefix - target);
            if (it != freq.end()) {
                answer += it->second;
            }
            ++freq[prefix];
        }
        cout << answer << '\n';
    }

    return 0;
}

