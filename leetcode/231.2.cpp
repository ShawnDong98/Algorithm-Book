#include <iostream>
 
typedef long long ll;
 
using namespace std;


/*
-x 的表示是 x 的补码 ~x + 1 

x      = 11010101000
-x     = 00101011000
x & -x = 00000001000

x & -x 表示 二进制最靠右边的第一个1

如果x为2的整数次幂 那么 x & -x == x 
如果x不为2的整数次幂 那么 x & -x < x
*/
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & -n) == n;

    }
};
 
int main() {

    // int n = 1;

    // int n = 16;

    int n = 218;

    Solution S;

    cout << S.isPowerOfTwo(n) << endl;

    return 0;
}