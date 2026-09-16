#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;

    priority_queue<pair<ll, int>> heap;
    unordered_map<int, ll> current;

    while (q--) {
        char operation;
        cin >> operation;

        if (operation == 'A' || operation == 'U') {
            int id;
            ll priority;
            cin >> id >> priority;
            current[id] = priority;
            heap.push({priority, -id});
            continue;
        }

        while (!heap.empty()) {
            auto [priority, negative_id] = heap.top();
            int id = -negative_id;
            auto found = current.find(id);
            if (found != current.end()
                && found->second == priority) {
                break;
            }
            heap.pop();
        }

        if (heap.empty()) {
            cout << -1 << '\n';
        } else {
            int id = -heap.top().second;
            heap.pop();
            current.erase(id);
            cout << id << '\n';
        }
    }
}
