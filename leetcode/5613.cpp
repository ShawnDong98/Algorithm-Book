#include <iostream>
#include <vector>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;


class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        vector<int> accounts_sum;
        for(int i=0; i<accounts.size(); ++i){
            int sum = 0;
            for(int j=0; j<accounts[i].size(); ++j){
                sum += accounts[i][j];  
            }
            accounts_sum.push_back(sum);
        }
        // for(int i=0; i<accounts_sum.size(); ++i){
        //     cout << "Accounts: " << accounts_sum[i] << endl;
        // }
        sort(accounts_sum.begin(), accounts_sum.end());
        reverse(accounts_sum.begin(), accounts_sum.end());
        // cout << accounts_sum[0] << endl;
        return accounts_sum[0];
        
    }
};
 
int main(){
    vector<vector<int>> accounts;
    // int b[3] = {1, 2 ,3};
    // int c[3] = {3, 2 ,1};
    // vector<int> d(b, b+3);
    // vector<int> e(c, c+3);

    // accounts.push_back(d);
    // accounts.push_back(e);

    int b[2] = {1, 5};
    int c[2] = {7, 3};
    int d[2] = {3, 5};
    vector<int> e(b, b+2);
    vector<int> f(c, c+2);
    vector<int> g(d, d+2);

    accounts.push_back(e);
    accounts.push_back(f);
    accounts.push_back(g);

    Solution S;

    S.maximumWealth(accounts);




    return 0;
}