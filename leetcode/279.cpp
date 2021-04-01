#include <iostream>
#include <queue>
 
typedef long long ll;
 
using namespace std;


/*----------------------------------------------
1. 通过宽搜来优化动态规划的效率，可以将整个过程看做一张图，每个数字都是一个点，两个数字之间差距为平方数时有一条单向边。
2. 使用宽搜来求从 0 到 n 的最短路。

时间复杂度：
- 宽搜的时间复杂度为 O(n+m)，这里的点数，也就是数字个数 n, 边数 是 O(sqrt{i})
- 故总时间复杂度仍然是 O(n sqrt{n})，但由于宽搜可能能快速找到到结点 n 的路径，常数会比较优。

空间复杂度：
- 需要额外 O(n)O(n) 的空间存储队列和距离数组。
-----------------------------------------------*/
class Solution {
public:
    int numSquares(int n) {
        queue<int> q;
        //------- 定义每一点到原点的距离， 长度初始化为正无穷 ---------
        vector<int> dist(n + 1, INT32_MAX);
        q.push(0);
        dist[0] = 0;
        while(q.size()) {
            int t = q.front();
            q.pop();
            if (t == n) return dist[t];
            for (int i = 1; i * i + t <= n; ++i) {
                int j = t + i * i;
                if (dist[j] > dist[t] + 1) {
                    dist[j] = dist[t] + 1;
                    q.push(j);
                }
            }
        }
        return 0;
    }
};
 
int main() {
    int n = 12;

    Solution S;

    cout << S.numSquares(n) << endl;
    
    return 0;
}