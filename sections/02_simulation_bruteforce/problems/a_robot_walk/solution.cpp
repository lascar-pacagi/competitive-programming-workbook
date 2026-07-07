#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        string s;
        cin >> s;
        int x = 0;
        int y = 0;
        int best = 0;
        for (char ch : s) {
            if (ch == 'U') {
                ++y;
            } else if (ch == 'D') {
                --y;
            } else if (ch == 'L') {
                --x;
            } else {
                ++x;
            }
            best = max(best, abs(x) + abs(y));
        }
        cout << x << ' ' << y << ' ' << best << '\n';
    }

    return 0;
}

