#include <iostream>
#include <string>
 
typedef long long ll;
 
using namespace std;


class Solution {
public:
    string reformatNumber(string number) {
        string new_number;
        string temp;
        string temp_number;
        for(int i=number.length()-1; i>=0; i--){
            if(number[i]!='-' && number[i]!=' '){
                // cout << number[i] << endl;
                char c = number[i];
                temp_number.insert(0, 1, c);
                // cout << temp_number << endl;
            }
            
        }
        // cout << temp_number << endl;
        while(1){
            if(temp_number.length() <= 4){
                if(temp_number.length()==2){
                    temp = temp_number.substr(0, 2);
                    temp_number.erase(0, 2);
                    new_number.append(temp);
                }
                if(temp_number.length()==3){
                    temp = temp_number.substr(0, 3);
                    temp_number.erase(0, 3);
                    new_number.append(temp);
                }
                if(temp_number.length()==4){
                    // cout << "I'm in 4" << endl;
                    temp = temp_number.substr(0, 2);
                    temp_number.erase(0, 2);
                    new_number.append(temp);
                    new_number.append("-");
                    temp = temp_number.substr(0, 2);
                    temp_number.erase(0, 2);
                    new_number.append(temp);
                }
            }
            else{
                temp = temp_number.substr(0, 3);
                temp_number.erase(0, 3);
                new_number.append(temp);
                new_number.append("-");
            }
            
            if(temp_number.length() == 0) break;

            continue;
        }

        return new_number;
        
    }
   
};
 
int main(){

    Solution S;
    
    // string a = "adasdasdasda";
    
    // string b = a.substr(0, 3);

    // b.erase(0, 3);

    // cout << b << endl;

    // string number = "12 3-4";

    // string number = "1-23-45 6";

    // string number = "123 4-567";

    // string number = "123 4-5678";

    string number = "--17-5 229 35-39475 ";


    cout << S.reformatNumber(number) << endl;

    return 0;
}