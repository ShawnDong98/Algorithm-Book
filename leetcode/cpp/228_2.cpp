#include <iostream>
#include <string>
 

 
using namespace std;

// 将字符串分为字母相同的若干段： 使用双指针法求每一段
// 使用公式计算每段内的子串的数目： 长度为1的子串个数有k个， 长度为2的子串个数有k-1个， 长度为k的子串个数有1个
// 将每段的子串数目求和
class Solution {
    typedef long long ll;
    const int MOD = 1e9 + 7;
public:
    int countHomogenous(string s) {
        int res = 0;
        for (int i = 0; i < s.size(); ++i) {
            int j = i + 1;
            while(j < s.size() && s[j] == s[i]) j++;
            int k = j - i;
            res = (res + (ll)k * (k+1) / 2) % MOD;
            i = j - 1;
        }
        return res;
    }
};
 
int main() {
    string s = "abbcccaa";
    Solution S;

    cout << S.countHomogenous(s) << endl;
    return 0;
}