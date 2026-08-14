#include <bits/stdc++.h>
using namespace std;

struct Point {
    long long x, y;
};

void print_int128(__int128 value) {
    if (value == 0) {
        cout << 0;
        return;
    }
    string digits;
    while (value > 0) {
        digits.push_back(char('0' + value % 10));
        value /= 10;
    }
    reverse(digits.begin(), digits.end());
    cout << digits;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<Point> polygon(n);
    for (Point& point : polygon) cin >> point.x >> point.y;

    __int128 signed_double_area = 0;
    __int128 boundary = 0;
    for (int index = 0; index < n; index++) {
        Point a = polygon[index];
        Point b = polygon[(index + 1) % n];
        signed_double_area += (__int128)a.x * b.y - (__int128)a.y * b.x;
        boundary += gcd(llabs(b.x - a.x), llabs(b.y - a.y));
    }
    __int128 double_area = signed_double_area >= 0 ? signed_double_area : -signed_double_area;
    __int128 interior = (double_area - boundary + 2) / 2;
    print_int128(interior);
    cout << '\n';
    return 0;
}
