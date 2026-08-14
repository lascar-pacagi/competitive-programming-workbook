#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    priority_queue<int, vector<int>, greater<int>> ending[2];
    vector<int> answer;
    int groups = 0;

    for (char character : s) {
        int bit = character - '0';
        int opposite = 1 - bit;
        int group;

        if (!ending[opposite].empty()) {
            group = ending[opposite].top();
            ending[opposite].pop();
        } else {
            group = ++groups;
        }

        ending[bit].push(group);
        answer.push_back(group);
    }

    cout << groups << '\n';
    for (int i = 0; i < static_cast<int>(answer.size()); ++i)
        cout << answer[i] << " \n"[i + 1 == static_cast<int>(answer.size())];
}
