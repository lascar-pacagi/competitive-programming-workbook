#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, q;
        cin >> n >> q;
        unordered_map<int, int> freq;
        freq.reserve(2 * n + 1);
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            ++freq[x];
        }
        while (q--) {
            int x;
            cin >> x;
            auto it = freq.find(x);
            cout << (it == freq.end() ? 0 : it->second) << '\n';
        }
    }

    return 0;
}

