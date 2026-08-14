#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    vector<int> bit;
    explicit Fenwick(int n) : bit(n + 1, 0) {}

    void add(int index, int delta) {
        for (int n = (int)bit.size(); index < n; index += index & -index) {
            bit[index] += delta;
        }
    }

    int sum(int index) const {
        int result = 0;
        for (; index > 0; index -= index & -index) result += bit[index];
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
    coords.erase(unique(coords.begin(), coords.end()), coords.end());
    auto rank_of = [&](long long value) {
        return int(lower_bound(coords.begin(), coords.end(), value) - coords.begin()) + 1;
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
            int before_low = int(lower_bound(coords.begin(), coords.end(), low) - coords.begin());
            int through_high = int(upper_bound(coords.begin(), coords.end(), high) - coords.begin());
            cout << bit.sum(through_high) - bit.sum(before_low) << '\n';
        }
    }
    return 0;
}
