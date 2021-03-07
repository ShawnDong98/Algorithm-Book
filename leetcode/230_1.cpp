#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

// 先定义一个计数器cnt
// 根据ruleKey检索
// 模式匹配， 计数
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int cnt = 0;
        int flag = 0;
        if (ruleKey == "type") flag = 1;
        if (ruleKey == "color") flag = 2;
        if (ruleKey == "name") flag = 3;
        for (int i = 0; i < items.size(); ++i) {
            switch(flag) {
                case 1: 
                    if(items[i][0] == ruleValue) cnt += 1;
                    break;

                case 2:
                    if(items[i][1] == ruleValue) cnt += 1;
                    break;
                
                case 3: 
                    if(items[i][2] == ruleValue) cnt += 1;
                    break;
               
            }
        }

        return cnt;

    }
};
 
int main() {
    vector<vector<string>> items;

    // vector<string> item1 = {"phone","blue","pixel"};
    // vector<string> item2 = {"computer","silver","lenovo"};
    // vector<string> item3 = {"phone","gold","iphone"};

    vector<string> item1 = {"phone","blue","pixel"};
    vector<string> item2 = {"computer","silver","phone"};
    vector<string> item3 = {"phone","gold","iphone"};



    items.push_back(item1);
    items.push_back(item2);
    items.push_back(item3);

    // string ruleKey = "color";
    // string ruleValue = "silver";

    string ruleKey = "type";
    string ruleValue = "phone";


    Solution S;

    cout << S.countMatches(items, ruleKey, ruleValue) << endl;

    
    return 0;
}