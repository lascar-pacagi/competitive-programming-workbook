#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int teams, problems, submissions;
    if (!(cin >> teams >> problems >> submissions)) return 0;
    vector<vector<char>> solved(teams + 1, vector<char>(problems + 1));
    vector<vector<int>> wrong(teams + 1, vector<int>(problems + 1));
    vector<int> solved_count(teams + 1);
    vector<long long> penalty(teams + 1);

    while (submissions--) {
        int minute, team, problem;
        char verdict;
        cin >> minute >> team >> problem >> verdict;
        if (solved[team][problem]) continue;
        if (verdict == 'W') {
            ++wrong[team][problem];
        } else {
            solved[team][problem] = true;
            ++solved_count[team];
            penalty[team] += minute + 20LL * wrong[team][problem];
        }
    }

    vector<int> order(teams);
    iota(order.begin(), order.end(), 1);
    sort(order.begin(), order.end(), [&](int a, int b) {
        return tuple{-solved_count[a], penalty[a], a} <
               tuple{-solved_count[b], penalty[b], b};
    });
    for (int team : order) {
        cout << team << ' ' << solved_count[team] << ' ' << penalty[team] << '\n';
    }
}
