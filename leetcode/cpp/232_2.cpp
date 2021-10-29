#include <iostream>
#include <vector>
#include <unordered_map>
 
typedef long long ll;
 
using namespace std;

/*----------------------------------------------
统计每个节点的度数， 如果节点的度数大于1， 返回该节点
-----------------------------------------------*/
class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        unordered_map<int, int> d;
        for (auto& e : edges) {
            int a = e[0], b = e[1];
            if (++d[a] > 1) return a;
            if (++d[b] > 1) return b;
        }
        return -1;
    }
};
 
int main() {
    // vector<vector<int>> edges;
    // vector<int> a = {1, 2};
    // vector<int> b = {2, 3};
    // vector<int> c = {4, 2};
    // edges.push_back(a);
    // edges.push_back(b);
    // edges.push_back(c);

    vector<vector<int>> edges;
    vector<int> a = {1, 2};
    vector<int> b = {5, 1};
    vector<int> c = {1, 3};
    vector<int> d = {1, 4};
    edges.push_back(a);
    edges.push_back(b);
    edges.push_back(c);
    edges.push_back(d);

    Solution S;

    cout << S.findCenter(edges) << endl;
    
    return 0;
}