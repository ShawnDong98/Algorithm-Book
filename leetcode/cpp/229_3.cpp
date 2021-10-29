#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int maximumScore(vector<int>& w, vector<int>& c) {
        int n = w.size(), m = c.size();
        if (n >= m * 2) {
            int x = m, y = n - m;
            while(y < n) w[x++] = w[y++];
            n = x;
        }

        vector<vector<int>> f(n + 2, vector<int>(n + 2));
        for (int len = n - m + 1; len <= n; len++) {
            for (int i = 1; i + len - 1 <= n; i++) {
                int j = i + len - 1;
                f[i][j] = max(f[i + 1][j] + w[i - 1] * c[n - len], f[i][j - 1] + w[j - 1] * c[n - len]);
            }
        }

        return f[1][n];
    }
};
 
int main() {
    vector<int> nums = {1, 2, 3};
    vector<int> multipliers = {3, 2, 1};

    Solution S;

    cout << S.maximumScore(nums, multipliers) << endl;
    
    
    return 0;
}