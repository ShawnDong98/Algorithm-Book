#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;


class Solution {
public:
    int closestCost(vector<int>& a, vector<int>& b, int T) {
        int res = INT32_MAX;
        int n = a.size(), m = b.size();
        for (int i = 0; i < n; i++) {
            int s = a[i];
            // 爆搜， 一共有这么多种情况， 2^{m*2}
            for (int j = 0; j < 1 << m * 2; ++j) {
                int r = s;
                bool flag = false;
                for (int k = 0; k < m; k ++) {
                    int t = j >> k * 2 & 3;
                    if (t == 3) {
                        flag = true;
                        break;
                    }

                    r += b[k] * t;
                }
                if (flag) continue;
                if (abs(r - T) < abs(res - T) || abs(r - T) == abs(res - T) && r < res)
                    res = r;
            }
        }
        return res;

    }
};


 
int main() {
    Solution S;

    vector<int> baseCosts = {1, 7};
    vector<int> toppingCosts = {3, 4};

    int target = 10;



    cout << S.closestCost(baseCosts, toppingCosts, target) << endl;
    
    return 0;
}