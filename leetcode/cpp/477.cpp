#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

//---------- 超出时间限制 ------------
class Solution {
public:
    int HammingDistance(int num1, int num2) {
        int res = num1 ^ num2;
        int s = 0;
        for (int k = res; k; k >>= 1) s += k & 1;
        return s;
    }
    int totalHammingDistance(vector<int>& nums) {
        int sum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i; j < nums.size(); ++j) {
                sum += HammingDistance(nums[i], nums[j]);
            }
        }
        return sum;
    }
};


/*----------------------------------------------
我们发现汉明距离只和每一位中0和1的个数有关， 我们按位来做， 

以 4, 14, 2 为例

在二进制表示中，4表示为0100，14表示为1110，2表示为0010。

它们的倒数第二位分别为 0 1 1， 把它分为 0 和 1的两组

它们 组间组合 结果为 1， 总共有 1 x 2 

它们 组内组合 结果为 0

因此， 最终的结果就为 31位 x 每位1的个数 x 每位0的个数
-----------------------------------------------*/
class Solution_ {
public:
    int totalHammingDistance(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i <= 30; ++i) {
            int ones = 0;
            for (auto x : nums)
                if (x >> i & 1)
                    ones ++;
            res += ones * (nums.size() - ones);
        }
        return res;
    }
};
 
int main() {
    vector<int> nums = {4, 14, 2};
    Solution_ S;

    cout << S.totalHammingDistance(nums) << endl;
    return 0;
}