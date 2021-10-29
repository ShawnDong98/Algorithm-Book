#include <iostream>
#include <vector>
#include <unordered_map>
 
typedef long long ll;
 
using namespace std;


/*
使用哈希映射freq 统计每个整数出现的次数

如果 x 和 k-x 分别出现了 freq[x] 和 freq[k-x]次， 那么(x, k-x)这两个数最多可以被移出min{freq[x], feq[k-x]}次。

如果2x = k， 那么西药进行特殊判断， 移出的次数为 freq[x]除以2并向下取整。

如何避免重复计数？ 比如(x, k-x)两个数会在遍历整个哈希映射时，被计数两次。

我们在遍历哈希映射时， 只处理x < k/2 或者 x = k/2这两种情况，这样(x, k-x)就只会被计数一次
*/
class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for(int num:nums){
            ++freq[num];
        }
        int ans = 0;
        for(auto [key, value] : freq){
            // cout << key << ": " << value << endl;
            if(key * 2 == k){
                ans += value / 2;
            } 
            else if(key * 2 < k && freq.count(k - key)){
                ans += min(value, freq[k - key]);
            }
        }
        return ans;
    }
};
 
int main(){
    Solution S;
    // int a[4] = {1, 2, 3, 4};
    // int k = 5;
    // vector<int> nums(a, a+4);

    int a[5] = {3, 1, 3, 4, 3};
    int k = 6;
    vector<int> nums(a, a+5);

    cout << S.maxOperations(nums, k) << endl;
    return 0;
}