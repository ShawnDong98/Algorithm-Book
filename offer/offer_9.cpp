/*------------------------------------------------------
һֻ����һ�ο�������1��̨�ף�Ҳ��������2��������Ҳ��������n����
�����������һ��n����̨���ܹ��ж�����������
-------------------------------------------------------*/
#include <iostream>

using namespace std;

class Solution {
public:
    int jumpFloorII(int number) {
        if(number == 1) return 1;
        return 2*jumpFloorII(number-1);
    }
};

int main(){
    Solution S;
    cout << S.jumpFloorII(4) << endl;
    return 0;
}
