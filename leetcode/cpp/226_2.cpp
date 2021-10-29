#include <iostream>
#include <vector>
#include <unordered_map>
 
typedef long long ll;
 
using namespace std;

// 无向树的遍历
class Solution {
public:
    unordered_map<int, vector<int>> g;
    vector<int> path;
    
    void dfs(int u, int father) {
        path.push_back(u);
        for (int x: g[u])
            if (x != father)
                dfs(x, u);
    }


    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {
        unordered_map<int, int> cnt;
        for (auto& e: adjacentPairs) {
            int a = e[0], b = e[1];
            g[a].push_back(b), g[b].push_back(a);
            cnt[a] ++, cnt[b] ++;
        }

        int root = 0;
        for (auto [k, v]: cnt) 
            if (v == 1){
                root = k;
                break;
            }

        dfs(root, -1);
        return path;
    }
};
 
int main() {
    vector<int> a = {2, 1};
    vector<int> b = {3, 4};
    vector<int> c = {3, 2};

    vector<vector<int>> adjacentPairs;
    adjacentPairs.push_back(a);
    adjacentPairs.push_back(b);
    adjacentPairs.push_back(c);

    Solution S;

    vector<int> t = S.restoreArray(adjacentPairs);

    for (auto x: t){
        cout << x << " ";
    }
    cout << endl;
    return 0;
}