#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string start, target;
    if (!(cin >> n >> start >> target)) return 0;

    int previous_operation = 0;
    int answer = 0;
    for (int index = 0; index + 1 < n; index++) {
        int mismatch = start[index] != target[index];
        int current_operation = mismatch ^ previous_operation;
        answer += current_operation;
        previous_operation = current_operation;
    }

    if (previous_operation != (start[n - 1] != target[n - 1])) cout << -1 << '\n';
    else cout << answer << '\n';
    return 0;
}
