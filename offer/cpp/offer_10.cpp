/*--------------------------------------------------
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
---------------------------------------------------*/
#include <iostream>

using namespace std;

class Solution {
public:
    // 斐波那契数列
    int rectCover(int number) {
        if(number==1) return 1;
        if(number==2) return 2;
        int F, F_pre, F_pre_pre;
        F_pre_pre = 1;
        F_pre = 2;
        F = 0;
        for(int i=3; i<=number; ++i){
            F = F_pre + F_pre_pre;
            F_pre_pre = F_pre;
            F_pre = F;
        }
        return F;
    }
};

int main(){
    Solution S;
    cout << S.rectCover(0) << endl;
    return 0;
}
