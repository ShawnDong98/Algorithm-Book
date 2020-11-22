#include <iostream>
#include <vector>
#include <string>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string s1, s2;
        // cout << concatString(word1) << endl;
        // cout << concatString(word2) << endl;
        s1 = concatString(word1);
        s2 = concatString(word2);
        if(s1 == s2) return true;
        return false;
    }

    string concatString(vector<string>& words) {
        string s;
        for(int i=0; i<words.size(); ++i){
            s.append(words[i]);
        }
        return s;
    }
};
 
int main(){
    vector<string> word1, word2;
    // string word1_s1 = "ab";
    // string word1_s2 = "c";

    // string word1_s1 = "a";
    // string word1_s2 = "cb";

    string word1_s1 = "abc";
    string word1_s2 = "d";
    string word1_s3 = "defg";
    word1.push_back(word1_s1);
    word1.push_back(word1_s2);
    word1.push_back(word1_s3);

    // string word2_s1 = "ab";
    // string word2_s2 = "c";

    string word2_s1 = "abcddefg";
    // string word2_s2 = "c";
    word2.push_back(word2_s1);
    // word2.push_back(word2_s2);

    Solution S;

    cout << S.arrayStringsAreEqual(word1, word2) << endl;

    
    return 0;
}