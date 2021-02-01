#include <iostream>
#include <string>
#include <vector>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int minCharacters(string a, string b) {
        vector<int> s1(26), s2(26);
        // 制作哈希表， 统计 a 和 b 中每个字符出现的次数
        for (auto c: a) s1[c - 'a'] ++;
        for (auto c: b) s2[c - 'a'] ++;

        int n = a.size(), m = b.size();
        int res = INT32_MAX;
        // 条件3
        for (int i = 0; i < 26; ++i) {
            res = min(res, n + m - (s1[i] + s2[i]));
        } 
        return min(res, min(work(s1, s2), work(s2, s1)));
    }

    // 令 s1 中所有字符小于 s2 中所有字符
    int work(vector<int> s1, vector<int> s2) {
        int res = INT32_MAX;
        for (int i = 1; i < 26; ++i) {
            int cnt = 0;
            // 计数 s1 中比某个字符大的字符数量
            for (int j = i; j < 26; ++j) cnt += s1[j];
            // 计数 s2 中比某个字符小的字符数量
            for (int j = 0; j < i; ++j) cnt += s2[j];
            res = min(res, cnt);
        }
        return res;
    }
};
 
int main() {

    string a = "aba", b = "caa";

    Solution S;
    
    cout << S.minCharacters(a, b) << endl;
    
    return 0;
}