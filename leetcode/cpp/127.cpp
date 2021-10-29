#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <queue>
 
typedef long long ll;
 
using namespace std;

/*----------------------------------------------
(最短路,BFS) O(n^2 L)

我们对问题进行抽象：
将单词看做点，如果两个单词可以相互转化，则在相应的点之间连一条无向边。那问题就变成了求从起点到终点的最短路。

然后考虑如何建图，有两种方式：

- 枚举所有单词对，然后判断是否可以通过改变一个字母相互转化，时间复杂度 O(n^2 L)；
- 枚举每个单词，然后枚举该单词的每一位字母，再枚举这一位的所有备选字母，然后再判断改变后的字符串是否存在，时间复杂度 O(26n L^2)。

我们要根据数据范围选择使用哪种建图方式，如果 26L>n，则用第二种，否则用第一种。经测试，早先leetcode上两种方式都是可以AC的，但后来增加了 n 的大小，但并未增加 L 的大小，所以第二种建图方式会超时，于是我们选择第一种建图方式即可。

由于边权都相等，所以可以用BFS求最短路。

时间复杂度分析：
- 建图，通过上述分析可知，时间复杂度是 O(26n L^2)；
- 求最短路用的是BFS，每个节点仅会遍历一次，每个点遍历时需要O(L)的计算量，所以时间复杂度是 O(nL)；

所以总时间复杂度是 O(26n L^2)。
-----------------------------------------------*/
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> S;
        //--- 存储距离 ---
        unordered_map<string, int> dist;
        queue<string> q;
        //--- 第一个单词到原点的距离为1 ---
        dist[beginWord] = 1;
        //--- 第一个单词入队 ---
        q.push(beginWord);
        for (auto word: wordList) S.insert(word);

        while(q.size()) {
            //--- 第一个单词出队 ---
            auto t = q.front();
            q.pop();
            string r = t;
            //--- 遍历单词中的每个字母 ---
            for (char i = 0; i <= t.size(); ++i) {
                t = r;
                for (char j = 'a'; j<='z'; ++j) {
                    //--- 如果第i位的字母和第j位的字母不同，就把该字母换掉 ---
                    //--- 新单词用 t 缓存---
                    if (r[i] != j) {   
                        t[i] = j;
                        //--- 如果节点中有该单词 且 该单词到原点的距离为0 ---
                        if (S.count(t) && dist.count(t) == 0) {
                            //--- 新单词的距离为旧单词加一 ---
                            dist[t] = dist[r] + 1;
                            //--- 如果新单词等于目标单词， 返回新单词到原点的距离 ---
                            if (t == endWord) return dist[t];
                            //--- 新单词入队 ---
                            q.push(t);
                        }
                    }
                }
            }
        }
        return 0;
    }
};
 
int main() {
    string beginWord = "hit";
    string endWord = "cog";

    vector<string> wordList = {"hot", "dot", "dog", "lot", "log", "cog"};

    Solution S;

    cout << S.ladderLength(beginWord, endWord, wordList) << endl;
  
    return 0;
}