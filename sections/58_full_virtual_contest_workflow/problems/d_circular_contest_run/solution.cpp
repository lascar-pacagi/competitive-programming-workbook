#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    ll budget;
    cin >> n >> budget;
    vector<ll> time(n);
    for (ll& value : time)
        cin >> value;

    ll total = 0;
    int left = 0;
    int answer = 0;
    for (int right = 0; right < 2 * n; ++right) {
        total += time[right % n];
        while (left <= right
               && (total > budget || right - left + 1 > n)) {
            total -= time[left % n];
            ++left;
        }
        answer = max(answer, right - left + 1);
    }

    cout << answer << '\n';
}
