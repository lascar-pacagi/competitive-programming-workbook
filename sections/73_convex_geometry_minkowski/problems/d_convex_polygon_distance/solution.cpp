#include <bits/stdc++.h>
using namespace std;
using int64 = long long;
using int128 = __int128_t;

struct Point {
    int64 x, y;
    Point operator+(Point other) const { return {x + other.x, y + other.y}; }
    Point operator-(Point other) const { return {x - other.x, y - other.y}; }
};

int128 cross(Point a, Point b) {
    return int128(a.x) * b.y - int128(a.y) * b.x;
}

vector<Point> normalize(vector<Point> polygon) {
    int start = min_element(polygon.begin(), polygon.end(), [](Point a, Point b) {
        return pair(a.y, a.x) < pair(b.y, b.x);
    }) - polygon.begin();
    rotate(polygon.begin(), polygon.begin() + start, polygon.end());
    return polygon;
}

vector<Point> minkowski(vector<Point> a, vector<Point> b) {
    a = normalize(move(a));
    b = normalize(move(b));
    int n = a.size(), m = b.size();
    vector<Point> edge_a(n), edge_b(m);
    for (int i = 0; i < n; ++i) edge_a[i] = a[(i + 1) % n] - a[i];
    for (int i = 0; i < m; ++i) edge_b[i] = b[(i + 1) % m] - b[i];

    vector<Point> result = {a[0] + b[0]};
    int i = 0, j = 0;
    while (i < n || j < m) {
        Point step;
        if (j == m || (i < n && cross(edge_a[i], edge_b[j]) > 0)) {
            step = edge_a[i++];
        } else if (i == n || cross(edge_a[i], edge_b[j]) < 0) {
            step = edge_b[j++];
        } else {
            step = edge_a[i++] + edge_b[j++];
        }
        result.push_back(result.back() + step);
    }
    result.pop_back();
    return result;
}

long double segment_distance(Point a, Point b) {
    long double dx = b.x - a.x;
    long double dy = b.y - a.y;
    long double denominator = dx * dx + dy * dy;
    long double parameter = -(a.x * dx + a.y * dy) / denominator;
    parameter = max((long double)0, min((long double)1, parameter));
    long double x = a.x + parameter * dx;
    long double y = a.y + parameter * dy;
    return sqrt(x * x + y * y);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n;
    vector<Point> a(n);
    for (auto& point : a) cin >> point.x >> point.y;
    cin >> m;
    vector<Point> negative_b(m);
    for (auto& point : negative_b) {
        cin >> point.x >> point.y;
        point.x = -point.x;
        point.y = -point.y;
    }

    vector<Point> difference = minkowski(move(a), move(negative_b));
    bool contains_origin = true;
    for (int i = 0; i < (int)difference.size(); ++i) {
        Point edge = difference[(i + 1) % difference.size()] - difference[i];
        Point toward_origin{-difference[i].x, -difference[i].y};
        if (cross(edge, toward_origin) < 0) contains_origin = false;
    }

    long double answer = 0;
    if (!contains_origin) {
        answer = numeric_limits<long double>::infinity();
        for (int i = 0; i < (int)difference.size(); ++i) {
            answer = min(answer, segment_distance(
                difference[i], difference[(i + 1) % difference.size()]));
        }
    }
    cout << fixed << setprecision(12) << answer << '\n';
}
