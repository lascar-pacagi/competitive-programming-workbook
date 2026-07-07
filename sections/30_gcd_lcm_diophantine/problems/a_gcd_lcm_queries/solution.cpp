#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        long long a, b;
        cin >> a >> b;
        long long g = gcd(a, b);
        cout << g << ' ' << a / g * b << '\n';
    }
    return 0;
}
