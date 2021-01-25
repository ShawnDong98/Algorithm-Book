#include <iostream>
#include <vector>
#include <unordered_map>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        int n = nums.size();
        unordered_map<int, int> hash;
        for (int i = 0; i < n; ++i) {
            for (int j = i+1; j < n; ++j) {
                hash[nums[i] * nums[j]] ++;
            }
        }

        int res = 0;
        for (auto& [key, value]: hash)
            res += value * (value - 1) / 2 * 8;

        return res;

    }
};
 
int main() {
    vector<int> nums = {2, 3, 4, 6};

    // vector<int> nums = {1, 2, 4, 5, 10};

    Solution S;

    cout << S.tupleSameProduct(nums) << endl;
     
    return 0;
}