#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;


//Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/*----------------------------------------------
2^n

BFS： 2^n

1. 空间是指数级别的， 大
2. 不会有爆栈的风险
3. 最短、最小

DFS: n

1. 空间和深度成正比， 小
2. 有爆栈的风险， 比如树的深度最坏可能有100000层
3. 不能搜最短、最小


-----------------------------------------------*/

/*----------------------------------------------
搞清楚什么是leaf node, leaf node 是没有 children 的node

递归往回传的层数一定要是来自于leaf node 的

这个题的难点在于， 会误把不是leaf node 的结果传上去。 比如左子树存在，右子树不存在。
-----------------------------------------------*/
class Solution {
public:

    // awful code
    TreeNode* TreeStructor() {
        TreeNode* L_1 = new TreeNode(9);
        TreeNode* L_2 = new TreeNode(15);
        TreeNode* R_2 = new TreeNode(7);
        TreeNode* R_1 = new TreeNode(15, L_2, R_2);
        TreeNode* root = new TreeNode(15, L_1, R_1);

        return root;
    }

    int minDepth(TreeNode* root) {
        if (!root) return 0;
        int left = minDepth(root->left);
        int right = minDepth(root->right);
        if(!left || !right) return left + right + 1;
        return min(left, right) + 1;
    }
};
 
int main() {

    Solution S;

    TreeNode* root = S.TreeStructor();

    cout << S.minDepth(root) << endl;
    
    return 0;
}