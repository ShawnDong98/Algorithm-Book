#include <iostream>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    bool ifEqual(string s1, string s2) {
        if(s1 == s2) return true;
        for (int i = 0; i < s1.size(); ++i) {
            for (int j = i+1; j < s1.size(); ++j) {
                string s1_tmp = s1;
                char tmp = s1_tmp[j];
                s1_tmp[j] = s1_tmp[i];
                s1_tmp[i] = tmp;
                if (s1_tmp == s2) return true;
            }
        }
        return false;
    }
    bool areAlmostEqual(string s1, string s2) {
        return ifEqual(s2, s1) || ifEqual(s1, s2);
    }
};

class Solution_ {
public:
    bool areAlmostEqual(string s1, string s2) {
        if (s1 == s2) return true;
        for (int i = 0; i < s1.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                swap(s1[i], s1[j]);
                if (s1 == s2) return true;
                swap(s1[i], s1[j]);
            }
        }
        return false;
    }
};
 
int main() {
    string s1 = "bank";
    string s2 = "kanb";

    // string s1 = "attack";
    // string s2 = "defend";

    // string s1 = "kelb";
    // string s2 = "kelb";

    // string s1 = "abcd";
    // string s2 = "dcba";

    Solution_ S;

    cout << S.areAlmostEqual(s1, s2) << endl;

    return 0;
}