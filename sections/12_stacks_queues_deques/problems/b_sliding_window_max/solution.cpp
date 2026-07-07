#include <bits/stdc++.h>
using namespace std;

vector<long long> solve_case(const vector<long long> &a, int k) {
    deque<int> dq;
    vector<long long> ans;
    for (int i = 0; i < (int)a.size(); ++i) {
        while (!dq.empty() && dq.front() <= i - k) {
            dq.pop_front();
        }
        while (!dq.empty() && a[dq.back()] <= a[i]) {
            dq.pop_back();
        }
        dq.push_back(i);
        if (i + 1 >= k) {
            ans.push_back(a[dq.front()]);
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, k;
        cin >> n >> k;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        vector<long long> ans = solve_case(a, k);
        for (int i = 0; i < (int)ans.size(); ++i) {
            if (i) cout << ' ';
            cout << ans[i];
        }
        cout << '\n';
    }

    return 0;
}

