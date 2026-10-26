#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string source, target;
    cin >> source >> target;
    int n = target.size();
    vector<int> prefix(n);
    for (int i = 1; i < n; ++i) {
        int j = prefix[i - 1];
        while (j && target[i] != target[j]) j = prefix[j - 1];
        if (target[i] == target[j]) ++j;
        prefix[i] = j;
    }
    string doubled = source + source;
    int answer = 0, matched = 0;
    for (int i = 0; i < 2 * n - 1; ++i) {
        char ch = doubled[i];
        while (matched && ch != target[matched])
            matched = prefix[matched - 1];
        if (ch == target[matched]) ++matched;
        if (matched == n) {
            ++answer;
            matched = prefix[matched - 1];
        }
    }
    cout << answer << '\n';
}
