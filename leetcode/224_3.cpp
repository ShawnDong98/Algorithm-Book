#include <iostream>
#include <vector>
#include <algorithm>


typedef long long ll;
 
using namespace std;

class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if(matrix[i][j]) matrix[i][j] += matrix[i-1][j];
            }
        }

        int res = 0;
        vector<int> q(m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                q[j] = matrix[i][j];
            }
            sort(q.begin(), q.end(), greater<int>());
            for (int j = 0; j < m; ++j) {
                res = max(res, q[j] * (j+1));
            }
        }
        return res;
    }
};
 
int main() {
    // vector<int> row1 = {0, 0, 1};
    // vector<int> row2 = {1, 1, 1};
    // vector<int> row3 = {1, 0, 1};
    // vector<vector<int>> matrix(3);
    // matrix[0] = row1;
    // matrix[1] = row2;
    // matrix[2] = row3;

    // vector<int> row1 = {1, 0, 
    1, 0, 1};
    // vector<vector<int>> matrix(1);
    // matrix[0] = row1;


    vector<int> row1 = {0, 0};
    vector<int> row2 = {0, 0};
    vector<vector<int>> matrix(2);
    matrix[0] = row1;
    matrix[1] = row2;

    Solution S;

    cout << S.largestSubmatrix(matrix) << endl;
    
    return 0;
}