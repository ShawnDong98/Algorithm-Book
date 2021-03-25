#include <iostream>
 

 
using namespace std;

/*----------------------------------------------
1. 求[m, n]的按位与，首先对于n和m这两个数在第i位前面都相同，由于n > m，因此n的第i位是1，m的第i位是0,即n = xxx1...，m = xxx0...，(...表示后面是什么未知)，因此一定会存在一个数是t = xxx1000的形式，即这个数的第i位是1，且后面的都是0的形式，并且这个数t一定在[m,n]内
2、这样的话[m,n]中的所有数与t按位与后再第i位以至后面全是0，因此只需求两个数的公共前缀即可。
-----------------------------------------------*/
class Solution {
public:
    typedef long long ll;
    int rangeBitwiseAnd(int left, int right) {
        int res = 0;
        for(int i = 30; i >= 0; i--) {
            if((left >> i & 1) != (right >> i & 1)) break;
            if((left >> i & 1) == 1) res += 1 << i;
        }
        return res;
    }
};
 
int main() {
    // int left = 5, right = 7;

    // int left = 0, right = 0;

    int left = 1, right = 2147483647;
    Solution S;

    cout << S.rangeBitwiseAnd(left, right) << endl;

    return 0;
}