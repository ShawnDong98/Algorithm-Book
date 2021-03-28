#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    struct Node {
        int son[2];
    };
    vector<Node> nodes;

    int findMaximumXOR(vector<int>& nums) {
        nodes.push_back(Node({0, 0}));

        for (auto x : nums) {
            int p = 0;
            for (int i = 30; i >= 0; i--) {
                int t = x >> i & 1;
                //---------- 用线性表构造出了一棵树 ------------
                if (!nodes[p].son[t]) {
                    nodes.push_back(Node({0, 0}));
                    nodes[p].son[t] = nodes.size() - 1;   
                }
                p = nodes[p].son[t];
            }
        }

        int res = 0;
        for (auto x : nums) {
            int p = 0, max_xor = 0;
            for (int i = 30; i >= 0; i--) {
                int t = x >> i & 1;
                if (nodes[p].son[!t]) {
                    p = nodes[p].son[!t];
                    max_xor += 1 << i;
                }
                else {
                    p = nodes[p].son[t];
                }
            }
            res = max(res, max_xor);
        }

        return res;
        
    }
};
 
int main() {
    vector<int> nums = {3, 10, 5, 25, 2, 8};

    Solution S;

    cout << S.findMaximumXOR(nums) << endl;
    return 0;
}