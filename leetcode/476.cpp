#include <iostream>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int findComplement(int num) {
        int res = 0, t = 0;
        while (num) {
            res += !(num & 1) << t;
            num >>= 1, t++;
        }

        return res;
    }
};
 
int main() {
    int num = 5;
    Solution S;

    cout << S.findComplement(num) << endl;
    return 0;
}