#include <bits/stdc++.h>
using namespace std;

int solve_case(const vector<long long> &a, long long target) {
    vector<long long> pref(a.size() + 1, 0);
    for (int i = 0; i < (int)a.size(); ++i) {
        pref[i + 1] = pref[i] + a[i];
    }

    int ans = (int)a.size() + 1;
    deque<int> dq;
    for (int i = 0; i < (int)pref.size(); ++i) {
        while (!dq.empty() && pref[i] - pref[dq.front()] >= target) {
            ans = min(ans, i - dq.front());
            dq.pop_front();
        }
        while (!dq.empty() && pref[dq.back()] >= pref[i]) {
            dq.pop_back();
        }
        dq.push_back(i);
    }
    return ans == (int)a.size() + 1 ? -1 : ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        long long target;
        cin >> n >> target;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        cout << solve_case(a, target) << '\n';
    }

    return 0;
}

