#include <bits/stdc++.h>
using namespace std;

long long egcd(long long a, long long b, long long &x, long long &y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    long long x1, y1;
    long long g = egcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return g;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        long long a, b, c;
        cin >> a >> b >> c;
        long long x, y;
        long long g = egcd(a, b, x, y);
        if (c % g != 0) {
            cout << "IMPOSSIBLE\n";
        } else {
            long long scale = c / g;
            cout << x * scale << ' ' << y * scale << '\n';
        }
    }
    return 0;
}
