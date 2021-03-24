#include <iostream>
#include <vector>
#include <unordered_map>

typedef long long ll;
 
using namespace std;

class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        vector<int> res;
        for(auto num : nums) {
            hashmap[num]++;
        }
        for(auto num : nums) {
            if (hashmap[num] == 1) res.push_back(num);
        }
        return res;

    }
};
 
/*----------------------------------------------
s = a ^ b
s2 = a
s ^ s2 = a ^ b ^ a = b
-----------------------------------------------*/
class Solution_ {
public:
    vector<int> singleNumber(vector<int>& nums) {
        //---------- 异或的结果一定至少有一位为1 ------------
        int s = 0;
        for (auto x : nums) s ^= x;

        //---------- 找到最右边的一个1 ------------
        //---------- 用这个1将数分为两堆 ------------
        int k = 0;
        while (!(s >> k & 1)) k++;

        int s2 = 0;
        for (auto x : nums)
            //---------- 找出第k位为1这一堆中只出现一次的数 ------------
            if (x >> k & 1)
                s2 ^= x;

        //---------- s 为两堆中只出现一次的数 的 异或结果 ------------
        //---------- 利用上述性质求解 ------------
        return vector<int>({s2, s^s2});

    }
};



int main() {
    // vector<int> nums = {1,2,1,3,2,5};

    // vector<int> nums = {-1,0};

    vector<int> nums = {0,1};
    Solution S;

    vector<int> res = S.singleNumber(nums);
    for(auto r : res) {
        cout << "r: " << r << endl;
    }
    return 0;
}