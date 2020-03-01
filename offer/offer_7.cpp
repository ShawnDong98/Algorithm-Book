/*---------------------------------------------
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

斐波那契数列：
F(1)=1，F(2)=1,
F(n)=F(n - 1)+F(n - 2)（n ≥ 3，n ∈ N*）
---------------------------------------------*/

#include <iostream>

using namespace std;

class Solution {
public:
    int Fibonacci(int n){
        if(n==0) return 0;
        int F, F_pre, F_pre_pre;
        F_pre = 1;
        F_pre_pre = 0;
        F = F_pre + F_pre_pre;
        for(int i=2; i<=n; ++i){
            F = F_pre + F_pre_pre;
            F_pre_pre = F_pre;
            F_pre = F;
        }
        return F;
    }

    // 递归， 超出内存限制
    int Fibonacci_1(int n) {
        if(n==1 || n == 2){
            return 1;
        }
        return Fibonacci(n-1) + Fibonacci(n-2);

    }
};

int main(){
    int n = 1;
    Solution S;
    cout << S.Fibonacci(n) << endl;

    return 0;
}
