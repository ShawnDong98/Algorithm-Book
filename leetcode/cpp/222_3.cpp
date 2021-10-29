#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

class Solution {
    const int MOD = 1e9 + 7;
public:
    int waysToSplit(vector<int>& nums) {
        int n = nums.size();
        vector<int> s(n+1);

        // 前缀和
        for(int i=0; i<=n; ++i){
            s[i] = s[i - 1] + nums[i - 1];
        }

        int ret = 0;
        for(int i=3, j=2, k=2; i<=n; ++i){
            while(s[n] - s[i - 1] < s[i - 1] - s[j - 1]) j++;
            while(k+1 < i && s[i-1] - s[k] >= s[k]) k++;
            if(j <= k && s[n] - s[i - 1] >= s[i - 1] - s[j - 1] && s[i-1] - s[k-1] >= s[k - 1])
                // 对每一个i都有k - j种分割方案， 求和
                ret = (ret + k - j + 1) % MOD; 
        }
        return ret;
    }
};
 
int main(){
    Solution S;

    vector<int> nums = {1,2,2,2,5,0};

    cout << S.waysToSplit(nums) << endl;

    return 0;
}