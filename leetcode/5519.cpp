/*
给你一个字符串 text
，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证
text 至少包含一个单词 。

请你重新排列空格，使每对相邻单词之间的空格数目都 相等 ，并尽可能 最大化
该数目。如果不能重新平均分配所有空格，请 将多余的空格放置在字符串末尾
，这也意味着返回的字符串应当与原 text 字符串的长度相等。
*/

/*
思路： 首先判断有多少个空格， 再判断有多少个单词，
空格数除以单词书就是每两个单词之间的间隔。

剩下的空格放在字符串的末尾。

怎么判断空格数？ 如果等于' ', 空格计数器+1
怎么判断单词？ 如果前面是' ' 并且 当前 大于'a'小于'z'， 单词计数器+1
怎么保存单词？ 创建一个string类型的vector, 每计算得到一个单词保存进vector
怎样算一个单词？ 前面是空格， 现在是字母， 开始记录单词， 前面是字母，
现在是空格， 单词记录结束， 存入vector， 单词计数器+1.
*/
#include <iostream>
#include <string>
#include <vector>

typedef long long ll;

using namespace std;

class Solution {
   public:
    string reorderSpaces(string text) {
        int WordsCounter = 0;
        int SpacesCounter = 0;
        int flag = 0;
        int indent = 0;
        int stay = 0;
        string cache;
        string restring;
        vector<string> words;
        for (int i = 0; i < text.length(); i++) {
            // cout << text[i];
            if (text[i] == ' ') SpacesCounter++;
            if(text.length()==1){
                flag = 1;
                cache = cache + text[0];
            }
            if (i != text.length() - 1) {
                if (i == 0 && text[i] != ' ') {
                    WordsCounter++;
                    flag = 1;
                    cache = cache + text[i];
                }
                if (text[i] == ' ' &&
                    (text[i + 1] >= 'a' && text[i + 1] <= 'z')) {
                    WordsCounter++;
                    flag = 1;
                }
                if (text[i + 1] == ' ' && (text[i] >= 'a' && text[i] <= 'z')) {
                    // cache = cache + text[i];
                    words.push_back(cache);
                    cache = "";
                    flag = 0;
                }
            }
            if (i == text.length() - 1 && text[i] != ' ') {
                words.push_back(cache);
                cache = "";
                flag = 0;
            }
            if (flag) {
                cache = cache + text[i + 1];
            }
        }
        if (WordsCounter > 2) {
            indent = SpacesCounter / (WordsCounter - 1);
            stay = SpacesCounter % (indent * (WordsCounter - 1));
        } 
        else if(WordsCounter == 2){
            indent = SpacesCounter;
            stay = 0;
        }
        else if(WordsCounter == 1){
            indent = 0;
            stay = SpacesCounter;

        }

        // cout << "indent: " << indent << endl;
        // cout << "stay: " << stay << endl;
        // cout << endl;
        // cout << "WordsCounter:" << WordsCounter << endl;
        // cout << "SpacesCounter" << SpacesCounter << endl;
        for (int i = 0; i < words.size(); i++) {
            // cout << words[i] << " ";
            // cout << endl;
            restring.append(words[i]);
            if (i != words.size() - 1)
                restring.append(indent, ' ');
            else
                restring.append(stay, ' ');
        }
        // cout << "restring: " << restring << endl;
        return restring;
    }
};

int main() {
    string text = " hello";
    Solution S;
    S.reorderSpaces(text);
    system("pause");
    return 0;
}
