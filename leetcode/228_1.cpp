#include <iostream>
#include <string>


typedef long long ll;
 
using namespace std;


// 计算变成第一种交替字符串需要多少步
// 计算变成第二种交替字符串需要多少步
// 两者取min
class Solution {
public:
    int work(char c, string s) {
        int res = 0;
        for (auto x: s) {
            if (c == x) res ++;
            c ^= 1;
        }
        return res;
    }
    int minOperations(string s) {
        return min(work('0', s), work('1', s));
    }
};
 
int main() {
    string s = "1111";
    Solution S;

    cout << S.minOperations(s) << endl;
    
    return 0;
}