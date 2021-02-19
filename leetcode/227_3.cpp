#include <iostream>
#include <string>
 
typedef long long ll;
 
using namespace std;

// 两个指针， 一个指针指在word1的头， 一个指在word2的头
// 比较两个指针所指元素谁的字典序大， 使用头插法将其插入merge尾端， 同时删除所指元素
class Solution {
public:

    string largestMerge(string word1, string word2) {
        int ptr1 = 0, ptr2 = 0;
        string merge;
        
        while(ptr1<word1.size() && ptr2<word2.size()){
            // 比较两个字符串的字典序
            if(word1.substr(ptr1) >= word2.substr(ptr2)) {
                merge.push_back(word1[ptr1]);
                ptr1++;
               
            }
            else {
                merge.push_back(word2[ptr2]);
                ptr2++;
            }
        }
        while(ptr1<word1.size()) {
            merge.push_back(word1[ptr1]);
            ptr1++;
        }
        while(ptr2<word2.size()) {
            merge.push_back(word2[ptr2]);
            ptr2++;
        }

        return merge;
    }
};


class Solution_ {
public:
    string largestMerge(string word1, string word2) {
        string res;
        int i = 0, j = 0;
        while (i < word1.size() || j < word2.size()) {
            if (word1.substr(i) > word2.substr(j))
                res += word1[i++];
            else
                res += word2[j++];
        }
        return res;
    }
};
 
int main() {
    string word1 = "cabaa"; 
    string word2 = "bcaaa";

    // string word1 = "abcabc"; 
    // string word2 = "abdcaba";

    Solution S;

    cout << S.largestMerge(word1, word2) << endl;
    
    return 0;
}