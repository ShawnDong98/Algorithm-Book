#include <iostream>
#include <vector>
#include <string>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string keysPressed) {
        vector<int>a(26, 0);
        releaseTimes.insert(releaseTimes.begin(), 0);
        for(int i=0; i<keysPressed.size(); ++i){
            if(releaseTimes[i+1] - releaseTimes[i] > a[keysPressed[i] - 'a']){
                a[keysPressed[i] - 'a'] = releaseTimes[i+1] - releaseTimes[i];
            }
            cout <<  keysPressed[i] << ": " << a[keysPressed[i] - 'a'] << endl;
        }
        // for(int i=0; i<a.size(); ++i){
        //     cout << a[i] << endl;
        // }
        int loc = find_max(a);
        // cout << loc << endl;

        return 'a'+loc;
    }
    int find_max(vector<int> a){
        int max = 0;
        int loc = 0;
        for(int i=a.size()-1; i>=0; --i){
            if(a[i] > max){
                max = a[i];
                loc = i;
            }
        }
        return loc;
    }
};
 
int main(){
    
    Solution S;
    // int a[4] = {9, 29, 49, 50};
    // vector<int> releaseTimes(a, a+4);
    // string keysPressed = "cbcd";

    // int a[5] = {12,23,36,46,62};
    // vector<int> releaseTimes(a, a+5);
    // string keysPressed = "spuda";

    int a[8] = {19,22,28,29,66,81,93,97};
    vector<int> releaseTimes(a, a+8);
    string keysPressed = "fnfaaxha";
    cout << S.slowestKey(releaseTimes, keysPressed) << endl;

    return 0;
}