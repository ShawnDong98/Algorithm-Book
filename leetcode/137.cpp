#include <iostream>
#include <unordered_map>
#include <vector>
 
typedef long long ll;
 
using namespace std;


class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> hashmap;
        for(auto num : nums) {
            hashmap[num]++;
        }
        for(auto num : nums) {
            // cout << "num: " << num << endl;
            // cout << "hashmap[num]: " << hashmap[num] << endl;
            if(hashmap[num] == 1) return num;
        }
    }
};


/*----------------------------------------------
状态机：

              ones twos
inital     :   0    0
one    1   :   1    0
two    1   :   0    1
three  1   :   0    0
-----------------------------------------------*/
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones = 0, twos = 0;
        for (auto x : nums) {
            ones = (ones ^ x) & ~twos;
            twos = (twos ^ x) & ~ones;
        }
        return ones;
    }
};
 
int main() {
    vector<int> nums = {2,2,3,2};
    // vector<int> nums = {0, 1, 0, 1, 0, 1, 99};


    Solution S;

    cout << S.singleNumber(nums) << endl;
    return 0;
}