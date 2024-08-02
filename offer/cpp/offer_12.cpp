/*-------------------------------------------------------
给定一个double类型的浮点数base和int类型的整数exponent。
求base的exponent次方。

保证base和exponent不同时为0
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
