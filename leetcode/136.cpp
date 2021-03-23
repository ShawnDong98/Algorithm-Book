#include <iostream>
#include <vector>

 
typedef long long ll;
 
using namespace std;

/*----------------------------------------------
a ^ a = 0
0 ^ a = a

异或运算满足 结合律 和 交换律

[1, 2, 3, 1, 2, 3, 4]
[1, 1, 2, 2, 3, 3, 4]
1 ^ 1 = 0
0 ^ 2 = 2
2 ^ 2 = 0
0 ^ 3 = 3
3 ^ 3 = 0 
0 ^ 4 = 4 
所以 return 4
-----------------------------------------------*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (auto x : nums) res ^= x;
        
        return res;
    }
};
 
int main() {
    // vector<int> nums = {2, 2, 1};

    vector<int> nums = {4, 1, 2, 1, 2};
    Solution S;

    cout << S.singleNumber(nums) << endl;
    return 0;
}