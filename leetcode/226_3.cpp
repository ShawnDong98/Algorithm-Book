#include <iostream>
#include <vector>
 

 
using namespace std;

typedef long long ll;

// 前缀和， 计算可以吃到的糖果 和 想要吃的糖果 有无交集
class Solution {
public:
    bool check(ll a, ll b, ll c, ll d) {
        if (b < c || d < a) return false;
        return true;
    }

    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        int n = candiesCount.size();
        vector<ll> s(n + 1);
        for (int i = 1; i <= n; i++) s[i] = s[i - 1] + candiesCount[i - 1];
        vector<bool> res;
        for (auto& q: queries) {
            int t = q[0], d = q[1], c = q[2];
            res.push_back(check(d + 1, (ll)(d + 1) * c, s[t] + 1, s[t+1]));
        }
        return res;
    }
};
 
int main() {
    vector<int> candiesCount = {7, 4, 5, 3, 8};
    vector<int> queries1 = {0, 2, 2};
    vector<int> queries2 = {4, 2, 4};
    vector<int> queries3 = {2, 13, 1000000000};

    vector<vector<int>> queries;  

    queries.push_back(queries1);
    queries.push_back(queries2);
    queries.push_back(queries3);

    Solution S;

    vector<bool> res = S.canEat(candiesCount, queries);

    for (auto x: res){
        // if(x) cout << "1" << endl;
        // else cout << "0" << endl;
        cout << x << endl;
    }

    return 0;
}