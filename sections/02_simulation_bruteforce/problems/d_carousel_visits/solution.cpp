#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    if (!(cin >> t)) return 0;
    while (t--) {
        int n, pos;
        string s;
        cin >> n >> pos >> s;
        vector<int> visits(n + 1);
        ++visits[pos];
        for (char move : s) {
            if (move == 'R') {
                pos = pos == n ? 1 : pos + 1;
            } else {
                pos = pos == 1 ? n : pos - 1;
            }
            ++visits[pos];
        }
        int best = 1;
        for (int i = 2; i <= n; ++i) {
            if (visits[i] > visits[best]) best = i;
        }
        cout << pos << ' ' << best << '\n';
    }
}
