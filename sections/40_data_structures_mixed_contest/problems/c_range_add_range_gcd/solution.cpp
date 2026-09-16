#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Fenwick {
    int n;
    vector<ll> bit;

    explicit Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void add(int index, ll delta) {
        for (; index <= n; index += index & -index)
            bit[index] += delta;
    }

    ll prefix_sum(int index) const {
        ll result = 0;
        for (; index > 0; index -= index & -index)
            result += bit[index];
        return result;
    }
};

struct GcdTree {
    int size = 1;
    vector<ll> tree;

    explicit GcdTree(const vector<ll>& values) {
        while (size < static_cast<int>(values.size()))
            size *= 2;
        tree.assign(2 * size, 0);
        for (int i = 0; i < static_cast<int>(values.size()); ++i)
            tree[size + i] = values[i];
        for (int node = size - 1; node > 0; --node)
            pull(node);
    }

    void pull(int node) {
        tree[node] = gcd(tree[2 * node], tree[2 * node + 1]);
    }

    void add(int position, ll delta) {
        int node = size + position;
        tree[node] += delta;
        for (node /= 2; node > 0; node /= 2)
            pull(node);
    }

    ll query(int left, int right) const {
        ll answer = 0;
        for (left += size, right += size;
             left < right;
             left /= 2, right /= 2) {
            if (left & 1)
                answer = gcd(answer, tree[left++]);
            if (right & 1)
                answer = gcd(answer, tree[--right]);
        }
        return answer;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    cin >> n >> q;

    vector<ll> difference(n);
    Fenwick values(n);
    ll previous = 0;
    for (int i = 0; i < n; ++i) {
        ll current;
        cin >> current;
        difference[i] = current - previous;
        previous = current;
        values.add(i + 1, difference[i]);
    }

    GcdTree differences(difference);

    while (q--) {
        int type, left, right;
        cin >> type >> left >> right;
        --left;

        if (type == 1) {
            ll delta;
            cin >> delta;

            differences.add(left, delta);
            values.add(left + 1, delta);
            if (right < n) {
                differences.add(right, -delta);
                values.add(right + 1, -delta);
            }
        } else {
            ll first_value = values.prefix_sum(left + 1);
            ll inside_differences = differences.query(left + 1, right);
            cout << gcd(abs(first_value), abs(inside_differences)) << '\n';
        }
    }
}
