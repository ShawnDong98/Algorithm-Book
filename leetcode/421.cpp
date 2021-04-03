#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;


/*----------------------------------------------
我们把每个数的二进制表示看成字符串，然后用Trie树给这些数建立索引。

左儿子为1的分支，右儿子为0的分支。

然后依次枚举每个数，在Trie树中找到与它异或结果最大的数。

这一步可以贪心来做：
从高位到低位，依次在Trie树中遍历，每次尽量走到与当前位不同的分支，这样可以使得找到的数与当前数在当前二进制位的异或结果是1，从而可以得到尽量大的结果。
-----------------------------------------------*/
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
                //--- 用线性表构造出了一棵Trie树 ---
                //--- 将所有的数都存在了这颗树中 ---
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
                //--- 找到第i位是0还是1 ---
                int t = x >> i & 1;
                //--- 如果 ---
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