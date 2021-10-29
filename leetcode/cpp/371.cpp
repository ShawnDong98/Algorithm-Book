#include <iostream>
 
typedef long long ll;
 
using namespace std;

/*----------------------------------------------
LeetCode增强了这道题的数据。

1. 两个数均为负数时，RE。eg. [-2, -3]
2. 当负数的绝对值小于正数时，RE。eg. [-2, 3]
3. 极限数据，RE。eg. [2147483647, -2147483648]

进行如下强转后可AC。
carry = uint(a & b) << 1;
-----------------------------------------------*/
class Solution {
public:
    typedef unsigned int uint;
    int getSum(int a, int b) {
        if (!b) return a;
        //---------- 先进行不进位加法， 然后再将进位加上 ------------
        int sum = a ^ b, carry = uint(a & b) << 1;
        return getSum(sum, carry);
    }
};
 
int main() {
    int a = 1;
    int b = 2;

    Solution S;

    cout << S.getSum(a, b) << endl;
    
    return 0;
}