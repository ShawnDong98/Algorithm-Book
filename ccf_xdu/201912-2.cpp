#include <iostream>
#include <map>

typedef long long ll;

using namespace std;

/*----------------------------------------------------
样例输入：
    7
    1 2
    2 1
    0 0
    1 1
    1 0
    2 0
    0 1

    11
    9 10
    10 10
    11 10
    12 10
    13 10
    11 9
    11 8
    12 9
    10 9
    10 11
    12 11



样例输出：
    0
    0
    1
    0
    0

    0
    2
    1
    0
    0

思路：

    结构体+map 可以替代矩阵， 可以解决边缘问题和负数问题

    用一个count来计数周围有几坨垃圾

    结构体内部需要重载小于号才能封装到map中。
-----------------------------------------------------*/
const int N = 1e3 + 1;
struct node {
    int x, y;
    node() {}
    node(int a, int b) : x(a), y(b) {}

    bool operator<(const node &oth) const {
        if (x != oth.x) return x < oth.x;
        return y < oth.y;
    }

} h[N];

class Solution {
   public:
    void Problem() {
        map<node, bool> mp;
        int score[5] = {0};
        int n;
        int x, y;
        cin >> n;
        for (int i = 0; i < n; ++i) {
            cin >> x >> y;
            h[i] = node(x, y);
            mp[h[i]] = 1;
        }
        for (int i = 0; i < n; ++i) {
            int count = 0;
            x = h[i].x;
            y = h[i].y;
            if (mp[node(x + 1, y)] && mp[node(x - 1, y)] &&
                mp[node(x, y + 1)] && mp[node(x, y - 1)]) {
                count = mp[node(x - 1, y - 1)] + mp[node(x - 1, y + 1)] +
                        mp[node(x + 1, y - 1)] + mp[node(x + 1, y + 1)];
                score[count] += 1;
            }
        }
        for (int i = 0; i < 5; ++i) {
            cout << score[i] << endl;
        }
    }
};

int main() {
    Solution S;
    S.Problem();
    // system("pause");
    return 0;
}