#include <iostream>
#include <vector>
#include <unordered_map>
#include <math.h>
 
typedef long long ll;
 
using namespace std;


// 根据 0 <= deliciousness[i] <= 2^20
// target的值可以是[2^0， 2^21], 一共有22中取法， 对target的加一层循环， 此层循环是常数规模的， 时间复杂度O(1)
class Solution {
    const int MOD = 1e9 + 7;
    using LL = long long;
public:
    int countPairs(vector<int>& deliciousness) {
        // 建立一个哈希映射，默认key为0
        unordered_map<int,int> memo;
        cout << memo.size() << endl;
        LL ans = 0;
        for (int i = 0;i < deliciousness.size();++i){
            for (int j = 0;j < 22;++j){
                int target = pow(2,j);
                if (target - deliciousness[i] < 0) continue;
                if (memo.count(target - deliciousness[i])){
                    ans += memo[target - deliciousness[i]];
                }
            }
            // deliciousness中每个元素都插入map映射， key为deliciousness的值， value是该deliciousness餐品的数量
            ++memo[deliciousness[i]];
        }
        ans %= MOD;
        return ans;
    }
};

 
int main(){
    // vector<int> deliciousness ={1, 3, 5, 7, 9};
    vector<int> deliciousness ={1,1,1,3,3,3,7};
    Solution S;

    cout << S.countPairs(deliciousness) << endl;
    return 0;
}