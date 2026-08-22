#include <bits/stdc++.h>
using namespace std;
using int64 = long long;

struct Event {
    int64 x, y1, y2;
    int delta;
};

struct CoverTree {
    int intervals;
    const vector<int64>& coordinate;
    vector<int> cover, components;
    vector<int64> length;
    vector<char> left_covered, right_covered;

    explicit CoverTree(const vector<int64>& ys)
        : intervals((int)ys.size() - 1), coordinate(ys),
          cover(4 * max(1, intervals)), components(cover.size()),
          length(cover.size()), left_covered(cover.size()),
          right_covered(cover.size()) {}

    void pull(int node, int low, int high) {
        if (cover[node] > 0) {
            length[node] = coordinate[high] - coordinate[low];
            components[node] = 1;
            left_covered[node] = right_covered[node] = true;
        } else if (high - low == 1) {
            length[node] = 0;
            components[node] = 0;
            left_covered[node] = right_covered[node] = false;
        } else {
            int left = 2 * node;
            int right = left + 1;
            length[node] = length[left] + length[right];
            components[node] = components[left] + components[right]
                             - (right_covered[left] && left_covered[right]);
            left_covered[node] = left_covered[left];
            right_covered[node] = right_covered[right];
        }
    }

    void update(int from, int to, int delta, int node, int low, int high) {
        if (to <= low || high <= from) return;
        if (from <= low && high <= to) {
            cover[node] += delta;
            pull(node, low, high);
            return;
        }
        int middle = (low + high) / 2;
        update(from, to, delta, 2 * node, low, middle);
        update(from, to, delta, 2 * node + 1, middle, high);
        pull(node, low, high);
    }

    void update(int from, int to, int delta) {
        update(from, to, delta, 1, 0, intervals);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Event> events;
    vector<int64> ys;
    for (int i = 0; i < n; ++i) {
        int64 x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        events.push_back({x1, y1, y2, +1});
        events.push_back({x2, y1, y2, -1});
        ys.push_back(y1);
        ys.push_back(y2);
    }
    sort(ys.begin(), ys.end());
    ys.erase(unique(ys.begin(), ys.end()), ys.end());
    sort(events.begin(), events.end(), [](const Event& a, const Event& b) {
        if (a.x != b.x) return a.x < b.x;
        return a.delta > b.delta;  // additions before removals
    });

    CoverTree tree(ys);
    int64 area = 0;
    int64 perimeter = 0;
    int64 previous_x = events.front().x;
    int index = 0;
    while (index < (int)events.size()) {
        int64 x = events[index].x;
        int64 width = x - previous_x;
        area += tree.length[1] * width;
        perimeter += int64(2) * tree.components[1] * width;

        while (index < (int)events.size() && events[index].x == x) {
            int from = lower_bound(ys.begin(), ys.end(), events[index].y1)
                     - ys.begin();
            int to = lower_bound(ys.begin(), ys.end(), events[index].y2)
                   - ys.begin();
            int64 before = tree.length[1];
            tree.update(from, to, events[index].delta);
            perimeter += llabs(tree.length[1] - before);
            ++index;
        }
        previous_x = x;
    }

    cout << area << ' ' << perimeter << '\n';
}
