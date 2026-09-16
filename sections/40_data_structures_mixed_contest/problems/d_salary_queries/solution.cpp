#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    vector<int> bit;
    explicit Fenwick(int n) : bit(n + 1, 0) {}

    void add(int index, int delta) {
        int size = static_cast<int>(bit.size());
        for (; index < size; index += index & -index) {
            bit[index] += delta;
        }
    }

    int sum(int index) const {
        int result = 0;
        for (; index > 0; index -= index & -index)
            result += bit[index];
        return result;
    }
};

struct Operation {
    char type;
    int first;
    long long second;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;
    vector<long long> salary(n + 1), coords;
    for (int i = 1; i <= n; i++) {
        cin >> salary[i];
        coords.push_back(salary[i]);
    }

    vector<Operation> operations;
    operations.reserve(q);
    for (int i = 0; i < q; i++) {
        char type;
        long long first, second;
        cin >> type >> first >> second;
        operations.push_back({type, (int)first, second});
        if (type == '!') coords.push_back(second);
    }

    sort(coords.begin(), coords.end());
    auto unique_end = unique(coords.begin(), coords.end());
    coords.erase(unique_end, coords.end());
    auto rank_of = [&](long long value) {
        auto iterator = lower_bound(
            coords.begin(), coords.end(), value
        );
        return int(iterator - coords.begin()) + 1;
    };

    Fenwick bit((int)coords.size());
    for (int i = 1; i <= n; i++) bit.add(rank_of(salary[i]), 1);

    for (const Operation& operation : operations) {
        if (operation.type == '!') {
            int employee = operation.first;
            bit.add(rank_of(salary[employee]), -1);
            salary[employee] = operation.second;
            bit.add(rank_of(salary[employee]), 1);
        } else {
            long long low = operation.first;
            long long high = operation.second;
            auto low_iterator = lower_bound(
                coords.begin(), coords.end(), low
            );
            auto high_iterator = upper_bound(
                coords.begin(), coords.end(), high
            );
            int before_low = int(low_iterator - coords.begin());
            int through_high = int(high_iterator - coords.begin());
            int answer = (
                bit.sum(through_high) - bit.sum(before_low)
            );
            cout << answer << '\n';
        }
    }
    return 0;
}
