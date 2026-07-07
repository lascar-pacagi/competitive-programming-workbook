#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, s, a, b, c;
        cin >> n >> s >> a >> b >> c;
        bool found = false;
        for (int x = 0; x <= n && !found; ++x) {
            for (int y = 0; y + x <= n; ++y) {
                int z = n - x - y;
                if (a * x + b * y + c * z == s) {
                    cout << x << ' ' << y << ' ' << z << '\n';
                    found = true;
                    break;
                }
            }
        }
        if (!found) {
            cout << "-1\n";
        }
    }

    return 0;
}

