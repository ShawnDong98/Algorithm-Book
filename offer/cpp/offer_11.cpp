/*----------------------------------------------------
����һ��������������������Ʊ�ʾ��1�ĸ�����
���и����ò����ʾ��
-----------------------------------------------------*/
#include <iostream>

using namespace std;

class Solution {
public:
     int  NumberOf1(int n) {
         unsigned int a = n;
         int count = 0;
         while(a != 0){
            a = a & (a - 1);
            ++count;
         }
         return count;
     }
};


class Solution_1 {
public:
     int  NumberOf1(int n) {
         unsigned int flag = 1;
         int count = 0;
         while(flag >= 1){
            if((n&flag) > 0){
                ++count;
            }
            flag  = flag << 1;
         }
         return count;
     }
};

int main(){
    Solution S;
    cout << S.NumberOf1(-6) << endl;
    return 0;
}
