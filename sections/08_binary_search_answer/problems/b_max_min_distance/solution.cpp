#include <bits/stdc++.h>
using namespace std;

bool can_place(const vector<long long> &pos, int k, long long dist) {
    int count = 1;
    long long last = pos[0];
    for (int i = 1; i < (int)pos.size(); ++i) {
        if (pos[i] - last >= dist) {
            ++count;
            last = pos[i];
            if (count >= k) return true;
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        vector<long long> pos(n);
        for (long long &x : pos) cin >> x;
        long long lo = 0;
        long long hi = pos.back() - pos.front() + 1;
        while (lo + 1 < hi) {
            long long mid = lo + (hi - lo) / 2;
            if (can_place(pos, k, mid)) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        cout << lo << '\n';
    }

    return 0;
}
