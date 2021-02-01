#include <iostream>
#include <string>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    string maximumTime(string time) {
        for (int i = 23; i >= 0; --i) {
            for (int j = 59; j >= 0; --j) {
                char str[20];
                sprintf(str, "%02d:%02d", i, j);
                if (check(time, str))
                    return str;
            }
        }
        return "";
    }

    bool check(string time, char str[]) {
        for (int i=0; i < 5; i ++) {
            if (time[i] == str[i] || time[i] == '?') continue;
            return false;
        }
        return true;
    }
};
 
int main() {
    // string time = "2?:?0";
    // string time = "0?:3?";
    string time = "1?:22";

    Solution S;

    cout << S.maximumTime(time) << endl;

    return 0;
}