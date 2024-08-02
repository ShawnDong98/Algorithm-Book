/*------------------------------------------------------
һֻ����һ�ο�������1��̨�ף�Ҳ��������2���������������
һ��n����̨���ܹ��ж������������Ⱥ����ͬ�㲻ͬ�Ľ������
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
    // ʱ�䳬��
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
