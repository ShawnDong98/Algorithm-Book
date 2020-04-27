#include <iostream>

typedef long long ll;
 
using namespace std;

/*---------------------------------------------
样例输入：
    20

样例输出：
    2
    1
    1
    0

思路：
    A， B， C， D四个变量记录甲乙丙丁跳过的次数
    取余判断是否为7倍数， 转字符串判断是否有7
    再对4取余，看是谁报数， 相应的计数器加一
---------------------------------------------*/
class Solution{
public:
    void Problem(){
        ll counter_A=0, counter_B=0, counter_C=0, counter_D=0;
        //记录报数的次数。
        ll counter = 0;
        ll i = 1;
        int n;
        cin >> n;
        while(counter!=n){
            if((i%7==0) || contain7(i)){
                if(i%4==1) ++counter_A;
                if(i%4==2) ++counter_B;
                if(i%4==3) ++counter_C;
                if(i%4==0) ++counter_D;
                i++;
                continue;
            }
            ++counter;
            ++i;
        }
        cout << counter_A << endl;
        cout << counter_B << endl;
        cout << counter_C << endl;
        cout << counter_D << endl;

    }

    bool contain7(ll i){
        while(i!=0){
            if(i%10==7) return 1;
            i = i/10;
        }
        return 0;
    }
};
 
int main(){
    
    Solution S;
    S.Problem();

    system("pause");
    return 0;
}   