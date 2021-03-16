#include <iostream>
#include <vector>
#include <numeric>



 
using namespace std;

/*----------------------------------------------------------------
添加若干元素 使得 数组和 sum -> goal

添加元素的取值范围 -limit ~ limit

最后添加元素的个数就是 ceil(abs(sum - goal) / limit) = floor((abs(sum - goal) + limit - 1) / limit)
----------------------------------------------------------------*/
class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        long long sum = accumulate(nums.begin(), nums.end(), 0ll);
        return (abs(sum - goal) + limit - 1) / limit;
    }
};
 
int main() {
    vector<int> nums = {1, -1, 1};
    int limit = 3;
    int goal = -4;

    // vector<int> nums = {1, -10, 9, 1};
    // int limit = 100;
    // int goal = 0;

    Solution S;
    
    cout << "Sum: " << S.minElements(nums, limit, goal) << endl;

    return 0;
}