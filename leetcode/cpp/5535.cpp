#include <iostream>
#include <stack>
#include <string>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int maxDepth(string s) {
        stack<char> S;
        int max = 0;
        int counter = 0;
        for(int i=0; i<s.size(); ++i){
            char c = s[i];
            if(c == '('){
                S.push(c);
                counter++;
                if(counter>=max){
                    max = counter;
                }
            }
            if(c == ')'){
                S.pop();
                counter--;
                if(counter>=max){
                    max = counter;
                }

            }
        }
        return max;
    }
};
 
int main(){
    
    Solution S;
    // string s = "(1+(2*3)+((8)/4))+1";

    // string s = "(1)+((2))+(((3)))";

    // string s = "1+(2*3)/(2-1)";

    string s = "1";

    cout << S.maxDepth(s) << endl;

    system("pause");
    return 0;
}