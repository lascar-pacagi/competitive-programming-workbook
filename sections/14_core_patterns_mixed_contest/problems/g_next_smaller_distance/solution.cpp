#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> a(n);
    for (auto &value : a) cin >> value;
    vector<int> answer(n), stack;
    for (int i = 0; i < n; ++i) {
        while (!stack.empty() && a[i] < a[stack.back()]) {
            int index = stack.back();
            stack.pop_back();
            answer[index] = i - index;
        }
        stack.push_back(i);
    }
    for (int i = 0; i < n; ++i)
        cout << answer[i] << (i + 1 == n ? '\n' : ' ');
}
