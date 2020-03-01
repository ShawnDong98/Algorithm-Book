/*------------------------------------------------------
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上
一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
------------------------------------------------------*/
#include <iostream>

using namespace std;

class Solution {
public:
    int jumpFloor(int number){
        if(number==2) return 2;
        if(number==1) return 1;
        int F, F_pre, F_pre_pre;
        F_pre = 2;
        F_pre_pre = 1;
        for(int i=3; i<=number; ++i){
            F = F_pre + F_pre_pre;
            F_pre_pre =F_pre;
            F_pre = F;
        }
        return F;
    }
    // 时间超限
    int jumpFloor_1(int number) {
        if(number==0) return 1;
        if(number<0) return 0;
        return jumpFloor(number-1) + jumpFloor(number-2);
    }
};

int main(){
    Solution S;
    cout << S.jumpFloor(4) << endl;
    return 0;
}
