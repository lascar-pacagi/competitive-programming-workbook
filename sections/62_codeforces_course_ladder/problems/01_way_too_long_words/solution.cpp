#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    if (!(cin >> q)) return 0;
    while (q--) {
        long long n, k;
        cin >> n >> k;
        if (n == 0) {
            cout << "0 0\n";
            continue;
        }
        long long pages = (n - 1) / k + 1;
        long long empty = pages * k - n;
        cout << pages << ' ' << empty << '\n';
    }
}
