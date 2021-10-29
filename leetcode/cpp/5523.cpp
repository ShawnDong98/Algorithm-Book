
#include <iostream>
#include <vector>
#include <string>
 
typedef long long ll;
 
using namespace std;

/*
给了一个字符串logs， 其中logs[i]是用户在i^{th}步执行的操作。

首先得计算得到整个操作之后处于哪一级的文件夹。可以用一个counter来记数第几层文件夹。

如果是'../'， counter - 1

如果是'./', counter 不变

否则counter+1

*/
class Solution {
public:
    int minOperations(vector<string>& logs) {
        int counterM = 0, counterP = 0;
        int flag = 1;
        for(int i=0; i<logs.size(); ++i){
            if(logs[i] == "../") {
                // cout << "I'm in 1..." << endl;
                counterP--;
            }
            else if(logs[i] == "./"){
                // cout << "I'm in 2..." << endl;
                continue;
            }
            // if(find_first_num(logs[i]) == counterM){
            //     // cout << "I'm in 3..." << endl;
            //     continue;
            // }
            // if(find_first_num(logs[i]) > counterM){
            //     // cout << "I'm in 4..." << endl;
            //     counterP++;
            // }
            else{
                // cout << "I'm in 3..." << endl;
                counterP++;
            }
            counterM = counterP;
            // cout << counterM << endl;
            if(counterM < 0){
                counterM=0;
                counterP = 0;
            }
        }
        return counterM;
    }
    // int find_first_num(string str){
    //     for(int i=0; i<str.size(); i++){
    //         if(str[i]>='0' && str[i]<='9') return str[i]-'0';
    //     }
    //     return -1;
    // }
};
 
int main(){
    Solution S;
    // string strs[5] = {"d1/","d2/","../","d21/","./"};
    // vector<string> logs(strs, strs+5);

    // string strs[6] = {"d1/","d2/","./","d3/","../","d31/"};
    // vector<string> logs(strs, strs+6);

    // string strs[4] = {"d1/","../","../","../"};
    // vector<string> logs(strs, strs+4);

    string strs[8] = {"./","wz4/","../","mj2/","../","../","ik0/","il7/"};
    vector<string> logs(strs, strs+8);

    for(int i=0; i<logs.size(); ++i){
        cout << logs[i] << endl;
    }

    cout << S.minOperations(logs) << endl;

    
    system("pause");
    return 0;
}