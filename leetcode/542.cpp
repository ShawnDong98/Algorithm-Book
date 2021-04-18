#include <iostream>
#include <vector>
#include <queue>
 
typedef long long ll;
 
using namespace std;

/*----------------------------------------------
(宽度优先搜索) O(nm)

定义一个队列，初始时将所有 0 元素的坐标进队；定义答案数组 dis，0 元素位置的值为 0，其余为 -1。

对这个队列开始进行宽度优先搜索，每次扩展上下左右四个方向，若发现新的位置在 dis 中值为 -1，则更新新位置的答案为当前位置答案加 1。


-----------------------------------------------*/
class Solution {
public:
    int dx[4] = {0, 1, 0, -1};
    int dy[4] = {1, 0, -1, 0};
    vector<vector<int>> updateMatrix(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        queue<pair<int, int>> q;
        //--- 答案数组 dis，0 元素位置的值为 0，其余为 -1 ---
        vector<vector<int>> dis(n, vector<int>(m, -1));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; ++j) {
                if (matrix[i][j] == 0) {
                    dis[i][j] = 0;
                    //--- 所有 0 元素的坐标进队 ---
                    q.push(make_pair(i, j));
                }
            }
        }

        while (!q.empty()) {
            pair<int, int> sta = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int x = sta.first + dx[i], y = sta.second + dy[i];
                if (x < 0 || x>= n || y<0 || y>= m || dis[x][y] != -1) {
                    continue;
                }
                //--- 若发现新的位置在 dis 中值为 -1，则更新新位置的答案为当前位置答案加 1 ---
                dis[x][y] = dis[sta.first][sta.second] + 1;
                q.push(make_pair(x, y));
            }
        }
        return dis;        
    }
};
 
int main() {
    vector<vector<int>> matrix;
    // vector<int> row1 = {0, 0, 0};
    // vector<int> row2 = {0, 1, 0};
    // vector<int> row3 = {0, 0, 0};

    vector<int> row1 = {0, 0, 0};
    vector<int> row2 = {0, 1, 0};
    vector<int> row3 = {1, 1, 1};
    matrix.push_back(row1);
    matrix.push_back(row2);
    matrix.push_back(row3);

    Solution S;

    vector<vector<int>> ret  = S.updateMatrix(matrix);
    for (int i=0; i<ret.size(); ++i) {
        for(int j=0; j<ret[0].size(); ++j) {
            cout << ret[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}