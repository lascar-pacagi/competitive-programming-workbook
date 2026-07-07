#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        long long x, y;
        cin >> x >> y;
        int steps = 0;
        while (x < y) {
            x = 2 * x + 1;
            ++steps;
        }
        cout << steps << '\n';
    }

    return 0;
}

