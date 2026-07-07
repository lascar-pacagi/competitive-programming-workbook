#include <bits/stdc++.h>
using namespace std;

struct Fenwick {
    vector<int> bit;

    explicit Fenwick(int n) : bit(n + 1, 0) {}

    void add(int idx, int delta) {
        while (idx < (int)bit.size()) {
            bit[idx] += delta;
            idx += idx & -idx;
        }
    }

    int sum(int idx) const {
        int total = 0;
        while (idx > 0) {
            total += bit[idx];
            idx -= idx & -idx;
        }
        return total;
    }

    int range_sum(int left, int right) const {
        return sum(right) - sum(left - 1);
    }
};

struct Query {
    int l;
    int r;
    int idx;
};

vector<int> solve_case(const vector<long long> &a, vector<Query> queries) {
    sort(queries.begin(), queries.end(), [](const Query &lhs, const Query &rhs) {
        return lhs.r < rhs.r;
    });

    Fenwick bit((int)a.size());
    unordered_map<long long, int> last;
    vector<int> ans(queries.size());
    int ptr = 0;
    for (const Query &query : queries) {
        while (ptr < query.r) {
            ++ptr;
            long long value = a[ptr - 1];
            auto it = last.find(value);
            if (it != last.end()) {
                bit.add(it->second, -1);
            }
            bit.add(ptr, 1);
            last[value] = ptr;
        }
        ans[query.idx] = bit.range_sum(query.l, query.r);
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n, q;
        cin >> n >> q;
        vector<long long> a(n);
        for (long long &x : a) cin >> x;
        vector<Query> queries;
        queries.reserve(q);
        for (int i = 0; i < q; ++i) {
            Query query;
            cin >> query.l >> query.r;
            query.idx = i;
            queries.push_back(query);
        }
        vector<int> ans = solve_case(a, queries);
        for (int value : ans) {
            cout << value << '\n';
        }
    }

    return 0;
}

