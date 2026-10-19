#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, k;
    if (!(cin >> n >> k))
        return 0;
    vector<int> a(n), coordinates;
    for (int &x : a)
        cin >> x;
    coordinates = a;
    sort(coordinates.begin(), coordinates.end());
    coordinates.erase(unique(coordinates.begin(), coordinates.end()),
                      coordinates.end());
    for (int &x : a)
        x = lower_bound(coordinates.begin(), coordinates.end(), x) -
            coordinates.begin() + 1;
    int m = coordinates.size();
    vector<int> bit(m + 1);
    auto add = [&](int x, int delta) {
        for (; x <= m; x += x & -x)
            bit[x] += delta;
    };
    auto prefix = [&](int x) {
        int sum = 0;
        for (; x > 0; x -= x & -x)
            sum += bit[x];
        return sum;
    };
    long long inversions = 0;
    for (int i = 0; i < n; i++) {
        if (i >= k) {
            int old = a[i - k];
            inversions -= prefix(old - 1);
            add(old, -1);
        }
        inversions += min(i, k - 1) - prefix(a[i]);
        add(a[i], 1);
        if (i >= k - 1)
            cout << inversions << (i == n - 1 ? '\n' : ' ');
    }
}
