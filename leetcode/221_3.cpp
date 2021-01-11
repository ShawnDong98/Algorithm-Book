#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int n = grid.size(), m = grid[0].size();
        vector<int> ret;
        for(int i = 0; i < m; ++i) {
            int x = 0, y = i, z = 0;
            while(x < n) {
                // 横向滚
                if (!z) {
                    // 格子是向右的挡板
                    if(grid[x][y] == 1) {
                        // 如果往右滚到墙 或者 右边的格子是向左的挡板， 卡住
                        if (y + 1 >= m || grid[x][y + 1] == -1) y = -1;
                        // 否则， 球向右滚
                        else y++, z = 1;
                    } 
                    // 格子是向左的挡板
                    else {
                        // 向左滚撞墙 或者 左边的格子是向右的挡板， 卡住
                        if (y - 1 < 0 || grid[x][y - 1] == 1) y = -1;
                        // 否则， 球向左滚
                        else y--, z = 1;
                    }
                }
                // 纵向滚
                else {
                    // 球向下滚
                    x++, z = 0;
                }
                if (y == -1) break;
            }
            ret.push_back(y);
        }
        return ret;
    }   
    
};
 
int main() {
    vector<int> row1 = {1,1,1,-1,-1};
    vector<int> row2 = {1,1,1,-1,-1};
    vector<int> row3 = {-1,-1,-1,1,1};
    vector<int> row4 = {1,1,1,1,-1};
    vector<int> row5 = {-1,-1,-1,-1,-1};

    vector<vector<int> > grid;
    grid.push_back(row1);
    grid.push_back(row2);
    grid.push_back(row3);
    grid.push_back(row4);
    grid.push_back(row5);

    Solution S;

    vector<int> ret = S.findBall(grid);

    // for (int i = 0; i < ret.size(); ++i) {
    //     cout << ret[i] << endl;
    // }
    for (auto x: ret){
        cout << x << endl;
    }
    
    return 0;
}