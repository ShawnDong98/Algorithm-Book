#include <iostream>
 
typedef long long ll;
 
using namespace std;


/*-------------------------------------------------------------
找到第一个1和最后一个1， 判断中间有没有0
如果有， 返回False
如果没有， 返回True
---------------------------------------------------------------*/
class Solution {
public:
    bool checkOnesSegment(string s) {
        int i = 0, j = s.size() - 1;
        while(i <= j && s[i] == '0') i++;
        while(i <= j && s[j] == '0') j--;
        for(int k = i; k<=j; k++) {
            if (s[k] == '0') {
                return false;
            }
        }
        return true;
       
    }
};
 
int main() {
    string s = "110";
    Solution S;

    cout << S.checkOnesSegment(s) <<endl;
    return 0;
}