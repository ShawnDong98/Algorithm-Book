#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;


// 二分查找： 找到一个最小的开销x
// 使得操作数小于 maxOperations
class Solution {
public:
    vector<int> nums;
    int m;

    bool check(int mid) {
        int res = 0;
        for (auto k: nums) {
            res += (k + mid - 1) / mid - 1;
            if (res > m) return false;
        }
        return true;

    }

    int minimumSize(vector<int>& _nums, int maxOperations) {
        nums = _nums, m = maxOperations;
        int l = 1, r = 1e9;
        while(l < r) {
            int mid = l + r >> 1;
            if (check(mid)) r = mid;
            else l = mid + 1;
        }
        return r;
    }
};
 
int main() {
    // vector<int> nums = {9};
    // int m = 2;

    vector<int> nums = {2,4,8,2};
    int m = 4;


    Solution S;

    cout << S.minimumSize(nums, m) << endl;

    return 0;
}