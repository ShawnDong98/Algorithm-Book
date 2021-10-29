#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

/*----------------------------------------------
遇到1一个1， 就把和它连同的1全部赋成0

这样就每个连通块只记一次
-----------------------------------------------*/
class Solution {
public:
    int n, m;
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        n = grid.size(), m = grid[0].size();
        int res = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (grid[i][j] == '1') {
                    res ++;
                    //--- dfs只是用来将连通块置0 ---
                    dfs(grid, i, j);
                }
            }
        }
        return res;
    }

    void dfs(vector<vector<char>> &grid, int x, int y) {
        int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
        grid[x][y] = '0';
        for (int i = 0; i < 4; ++i) {
            int a = x + dx[i], b = y + dy[i];
            grid[x][y] = '0';
            if (a >= 0 && a < n && b >= 0 && b < m && grid[a][b] == '1')
                dfs(grid, a, b);
        }

    }
};
 
int main() {
    vector<vector<char>> grid;
    vector<char> row1 = {'1','1','1','1','0'};
    vector<char> row2 = {'1','1','0','1','0'};
    vector<char> row3 = {'1','1','0','0','0'};
    vector<char> row4 = {'0','0','0','0','0'};
    grid.push_back(row1);
    grid.push_back(row2);
    grid.push_back(row3);
    grid.push_back(row4);

    Solution S;

    cout << S.numIslands(grid) << endl;
 
    return 0;
}