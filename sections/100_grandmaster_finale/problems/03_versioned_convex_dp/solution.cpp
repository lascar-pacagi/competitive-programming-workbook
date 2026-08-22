#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

struct Line {
    int64 slope = 0;
    int64 intercept = 0;
    int identifier = -1;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    vector<int> parent(q + 1);
    vector<char> type(q + 1);
    vector<int64> first(q + 1), second(q + 1);
    vector<vector<int>> children(q + 1);
    vector<int64> coordinates;
    for (int version = 1; version <= q; ++version) {
        cin >> parent[version] >> type[version] >> first[version];
        if (type[version] == 'A') cin >> second[version];
        else coordinates.push_back(first[version]);
        children[parent[version]].push_back(version);
    }
    if (coordinates.empty()) coordinates.push_back(0);
    sort(coordinates.begin(), coordinates.end());
    coordinates.erase(unique(coordinates.begin(), coordinates.end()), coordinates.end());

    vector<Line> tree(4 * coordinates.size() + 4);
    vector<pair<int, Line>> history;
    auto value = [](const Line &line, int64 x) {
        return line.slope * x + line.intercept;
    };
    auto better = [&](const Line &a, const Line &b, int64 x) {
        if (a.identifier == -1) return false;
        if (b.identifier == -1) return true;
        return pair{value(a, x), a.identifier} < pair{value(b, x), b.identifier};
    };
    auto assign = [&](int node, Line line) {
        history.push_back({node, tree[node]});
        tree[node] = line;
    };
    auto insert = [&](auto &&self, int node, int left, int right, Line line) -> void {
        if (tree[node].identifier == -1) {
            assign(node, line);
            return;
        }
        int middle = (left + right) / 2;
        if (better(line, tree[node], coordinates[middle])) {
            Line displaced = tree[node];
            assign(node, line);
            line = displaced;
        }
        if (right - left == 1) return;
        if (better(line, tree[node], coordinates[left]))
            self(self, node * 2, left, middle, line);
        else if (better(line, tree[node], coordinates[right - 1]))
            self(self, node * 2 + 1, middle, right, line);
    };
    auto query = [&](int position) {
        int node = 1, left = 0, right = coordinates.size();
        Line answer;
        while (true) {
            if (better(tree[node], answer, coordinates[position])) answer = tree[node];
            if (right - left == 1) break;
            int middle = (left + right) / 2;
            if (position < middle) {
                node *= 2;
                right = middle;
            } else {
                node = node * 2 + 1;
                left = middle;
            }
        }
        return answer;
    };
    auto rollback = [&](int snapshot) {
        while (static_cast<int>(history.size()) > snapshot) {
            auto [node, old_line] = history.back();
            history.pop_back();
            tree[node] = old_line;
        }
    };

    insert(insert, 1, 0, coordinates.size(), {0, 0, 0});
    history.clear();
    vector<pair<int64, int>> answers(q + 1);
    vector<tuple<int, int, int>> stack;
    for (auto it = children[0].rbegin(); it != children[0].rend(); ++it)
        stack.push_back({*it, 0, 0});
    while (!stack.empty()) {
        auto [version, phase, snapshot] = stack.back();
        stack.pop_back();
        if (phase == 0) {
            snapshot = history.size();
            if (type[version] == 'A') {
                insert(insert, 1, 0, coordinates.size(),
                       {first[version], second[version], version});
            } else {
                int position = lower_bound(coordinates.begin(), coordinates.end(),
                                           first[version]) - coordinates.begin();
                Line line = query(position);
                answers[version] = {value(line, first[version]), line.identifier};
            }
            stack.push_back({version, 1, snapshot});
            for (auto it = children[version].rbegin(); it != children[version].rend(); ++it)
                stack.push_back({*it, 0, 0});
        } else {
            rollback(snapshot);
        }
    }
    for (int version = 1; version <= q; ++version)
        if (type[version] == 'Q')
            cout << answers[version].first << ' ' << answers[version].second << '\n';
}
