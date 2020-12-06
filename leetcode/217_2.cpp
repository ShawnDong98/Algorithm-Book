#include <iostream>
#include <vector>


typedef long long ll;
 
using namespace std;


/*
单调栈问题， 也涉及到贪心的思想， 找出特定长度的递增序列。

单调栈就是维护一个栈， 该栈要么是单调递增的， 要么是单调递减。

当遍历到一个新的元素时， 将该元素与栈顶元素比较， 如果该元素小于栈顶元素则弹出栈顶元素， 直到与栈顶元素相等或大于栈顶元素即可。

同时要有一个变量count， 记录我们最多可以删除多少个元素， 所谓删除元素就是从栈内弹出元素， 我们最多能删除n - k个元素
*/
class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        vector<int> ans;
        int n=nums.size(), count = n - k;
        for(int i=0; i<nums.size(); ++i){
            while(ans.size() > 0 && nums[i] < ans.back() && count > 0){
                ans.pop_back();
                count--;
            }
            ans.push_back(nums[i]);
        }
        while(ans.size() > k){
            ans.pop_back();
        }

        return ans;  
    }
};
 
int main(){
    // int k = 2;
    // int a[4] = {3, 5, 2, 6};
    // vector<int> nums(a, a+4);

    int k = 4;
    int a[8] = {2, 4, 3, 3, 5, 4, 9, 6};
    vector<int> nums(a, a+8);



    Solution S;
    

    vector<int> ans;
    ans = S.mostCompetitive(nums, k);
     
    for(int i=0; i<ans.size(); ++i){
        cout << ans[i] << endl;
    }
    return 0;
}