#include <iostream>
 
typedef long long ll;
 
using namespace std;


class Solution {
public:
    int numberOfMatches(int n) {
        int count = 0;
        while(n != 1){
            if(n%2 == 0){
                count += n/2;
                n /= 2;

             }
            else{
                count += (n-1)/2;
                n = (n-1)/2 + 1;
            }
            // cout << "n: " << n << endl;
            // cout << count << endl;
        }
        return count;

    }
};
 
int main(){
    // int n = 7;
    int n = 14;

    Solution S;

    cout << S.numberOfMatches(n) << endl;;

    return 0;
}