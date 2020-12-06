#include <iostream>
#include <string>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    string interpret(string command) {
        string result;
        for(int i=0; i<command.size(); ++i){
            if(command[i]=='G'){
                result.push_back('G');
            }
            if(command[i]=='(' && command[i+1] == ')'){
                result.push_back('o');
                i += 1;
            }
            if(command[i]=='(' && command[i+1] == 'a'){
                result += "al";
                i += 3;
            }
        }
        return result;
    }
};
 
int main(){
    // string s = "G()(al)";
    // string s = "G()()()()(al)";
    string s = "(al)G(al)()()G";

    Solution S;

    cout << S.interpret(s) << endl;
    
    return 0;
}