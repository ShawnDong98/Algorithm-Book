/*-------------------------------------------------------
����һ��double���͵ĸ�����base��int���͵�����exponent��
��base��exponent�η���

��֤base��exponent��ͬʱΪ0
-------------------------------------------------------*/
#include <iostream>

using namespace std;

class Solution {
public:
    double Power(double base, int exponent) {
        double out = base;
        if(exponent==0) return 1;
        if(exponent>0){
            for(int i=1; i<exponent; ++i){
                out *= base;
            }
        }
        if(exponent<0){
            base = 1.0 / base;
            out = base;
            for(int i=1; i<-exponent; ++i){
                out *= base;
            }
        }
        return out;

    }
};

int main(){
    Solution S;
    cout << S.Power(2, -3) << endl;
    return 0;
}
