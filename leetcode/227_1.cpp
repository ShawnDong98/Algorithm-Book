#include <iostream>
#include <vector>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    bool check(vector<int>& nums) {
        vector<int> nums_1 = nums;
        sort(nums_1.begin(), nums_1.end());
        for (int x = 0; x < nums.size(); ++x) {
            int i = 0;
            for (i = 0; i < nums.size(); ++i) {
                if(nums[i] != nums_1[(i + x) % nums.size()]) break;
            }
            if (i == nums.size()) return true;
            
        }
        return false;

    }
};

class Solution_ {
public:
    bool check(vector<int>& a) {
        auto b = a;
        sort(b.begin(), b.end());
        int n = a.size();
        for (int i = 0; i < n; i ++) {
            if (a == b) return true;
            int t = a[0];
            for (int j = 1; j < n; j ++)
                a[j - 1] = a[j];
            a.back() = t;
        }
        return false;
    }
};
 
int main() {
    vector<int> nums = {2, 1, 3, 4};
    // vector<int> nums = {3, 4, 5, 1, 2};
    // vector<int> nums = {1, 1, 1};
    // vector<int> nums = {2, 1};
    Solution_ S;

    cout << S.check(nums) << endl;
    return 0;
}