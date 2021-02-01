#include <iostream>
#include <vector>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;

const int N = 1000010;
int q[N];

class Solution {
public:
    int kthLargestValue(vector<vector<int>>& matrix, int k) {
        int n = matrix.size(), m = matrix[0].size();
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (i) matrix[i][j] ^= matrix[i - 1][j];
                if (j) matrix[i][j] ^= matrix[i][j - 1];
                if (i && j) matrix[i][j] ^= matrix[i - 1][j - 1];
                q[cnt ++] = matrix[i][j];
            }
        }
        k = cnt - k;
        nth_element(q, q + k, q + cnt);
        return q[k];
    }
};
 
int main() {
    vector<int> a = {5, 2};
    vector<int> b = {1, 6};
    vector<vector<int> > matrix;
    matrix.push_back(a);
    matrix.push_back(b);

    Solution S;

    cout << S.kthLargestValue(matrix, 1) << endl;

    return 0;
}