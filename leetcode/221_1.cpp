#include <iostream>
#include <string>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    bool halvesAreAlike(string s) {
        int counter = 0;
        string str_pre = s.substr(0, s.size()/2);
        string str_post = s.substr(s.size()/2);
        
        transform(str_pre.begin(), str_pre.end(), str_pre.begin(), ::tolower); 
        transform(str_post.begin(), str_post.end(), str_post.begin(), ::tolower); 

        int counter_pre=0, counter_post=0;
        for(int i=0; i<str_pre.size(); ++i){
            if(str_pre[i] == 'a' || str_pre[i] == 'e' || str_pre[i] == 'i' || str_pre[i] == 'o' || str_pre[i] == 'u') counter_pre++;
            if(str_post[i] == 'a' || str_post[i] == 'e' || str_post[i] == 'i' || str_post[i] == 'o' || str_post[i] == 'u') counter_post++;    
        }

        if(counter_pre == counter_post) return 1;
        else return 0;
    }

};
 
int main(){
    // string s = "Book";
    // string s = "textbook";
    // string s = "MerryChristmas";
    string s = "AbCdEfGh";

    Solution S;


    cout << S.halvesAreAlike(s) << endl;
    // S.halvesAreAlike(s);

    return 0;
}