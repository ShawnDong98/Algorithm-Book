#include <iostream>
#include <string>
 
typedef long long ll;
 
using namespace std;

// 类似与合并两个链表
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int ptr1 = 0, ptr2 = 0;
        string res;
        while(ptr1 < word1.length() && ptr2 < word2.length()) {
            res.push_back(word1[ptr1++]);
            res.push_back(word2[ptr2++]);
        }
        while(ptr1 < word1.length()) res.push_back(word1[ptr1++]);
        while(ptr2 < word2.length()) res.push_back(word2[ptr2++]);

        return res;
    }
    
};
 
int main() {

    // string word1 = "abc";
    // string word2 = "pqr";

    // string word1 = "ab";
    // string word2 = "pqrs";

    string word1 = "abcd";
    string word2 = "pq";
    
    Solution S;

    cout << S.mergeAlternately(word1, word2) << endl;

    
    return 0;
}