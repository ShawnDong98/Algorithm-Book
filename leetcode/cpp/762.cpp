#include <iostream>
#include <unordered_set>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int countPrimeSetBits(int L, int R) {
        unordered_set<int> primes({2, 3, 5, 7, 11, 13, 17, 19});

        int res = 0;
        for (int i = L; i <= R; ++i) {
            int s = 0;
            // 循环右移， 统计i中 1 的个数
            for (int k = i; k; k >>= 1) s += k & 1;
            if (primes.count(s))
                    res ++ ;
        }
        
        return res;
    }
};
 
int main() {

    // int L = 6, R = 10;

    int L = 10, R = 15;

    Solution S;


    cout << S.countPrimeSetBits(L, R) << endl;
    

    return 0;
}