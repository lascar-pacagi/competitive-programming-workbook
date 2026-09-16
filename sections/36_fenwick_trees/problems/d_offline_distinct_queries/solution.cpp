#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    int n;
    vector<int> bit;

    explicit Fenwick(int size) : n(size), bit(size + 1, 0) {}

    void add(int index, int delta) {
        for (; index <= n; index += index & -index) {
            bit[index] += delta;
        }
    }

    int sum(int index) const {
        int result = 0;
        for (; index > 0; index -= index & -index) {
            result += bit[index];
        }
        return result;
    }

    int range_sum(int left, int right) const {
        return sum(right) - sum(left - 1);
    }
};

struct Query {
    int left;
    int right;
    int index;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> values(n + 1);
    for (int i = 1; i <= n; ++i) cin >> values[i];

    vector<Query> queries(q);
    for (int i = 0; i < q; ++i) {
        cin >> queries[i].left >> queries[i].right;
        queries[i].index = i;
    }
    sort(
        queries.begin(),
        queries.end(),
        [](const Query& a, const Query& b) {
            return a.right < b.right;
        }
    );

    Fenwick active(n);
    unordered_map<long long, int> last_position;
    last_position.reserve(2 * n);
    vector<int> answer(q);
    int processed_right = 0;

    for (const Query& query : queries) {
        while (processed_right < query.right) {
            ++processed_right;
            long long value = values[processed_right];
            auto previous = last_position.find(value);
            if (previous != last_position.end()) {
                active.add(previous->second, -1);
            }
            active.add(processed_right, 1);
            last_position[value] = processed_right;
        }
        answer[query.index] = active.range_sum(
            query.left,
            query.right
        );
    }

    for (int value : answer) cout << value << '\n';
    return 0;
}
