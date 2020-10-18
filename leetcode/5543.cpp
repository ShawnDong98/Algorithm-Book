#include <iostream>
#include <string>

typedef long long ll;

using namespace std;

/*

*/
class Solution {
   public:
    int maxLengthBetweenEqualCharacters(string s) {
        int pos, dis;
        int memory = -1;
        for (int i = 0; i < s.size(); ++i) {
            pos = s.rfind(s[i]);
            // cout << "pos: " << pos << endl;
            dis = pos - i - 1;
            // cout << "dis: " << dis << endl;
            if (pos != -1) {
                if(dis > memory) memory = dis;
            }
        }
        // cout << "memory: " << memory << endl;
        return memory;
    }
};

int main() {
    Solution S;
    string s = "aa";
    // string s = "abca";
    // string s = "cbzxy";
    // string s = "cabbac";
    // string s = "mgntdygtxrvxjnwksqhxuxtrv";
    S.maxLengthBetweenEqualCharacters(s);
    return 0;
}