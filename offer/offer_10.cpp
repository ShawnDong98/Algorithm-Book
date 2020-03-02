/*--------------------------------------------------
���ǿ�����2*1��С���κ��Ż�������ȥ���Ǹ���ľ��Ρ�
������n��2*1��С�������ص��ظ���һ��2*n�Ĵ���Σ�
�ܹ��ж����ַ�����
---------------------------------------------------*/
#include <iostream>

using namespace std;

class Solution {
public:
    // 쳲���������
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
