#include <iostream>
 
typedef long long ll;
 
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

/*----------------------------------------------
(递归遍历) O(n)

1. 递归函数的返回值定义为从当前结点到叶子结点的最大长度，当前结点为空返回 -1。

2. 递归时，分别得到左右子树递归的返回值，则可以更新答案 ans = max(ans, d1 + d2 + 2)；然后返回 max(d1, d2) + 1。

时间复杂度

- 每个结点最多仅被遍历一次，故时间复杂度为 O(n)。
-----------------------------------------------*/
class Solution {
public:
    TreeNode* TreeStructor() {
        TreeNode* C31 = new TreeNode(4);
        TreeNode* C32 = new TreeNode(5);
        TreeNode* C21 = new TreeNode(2, C31, C32);
        TreeNode* C22 = new TreeNode(3);
        TreeNode* root = new TreeNode(1, C21, C22);
        return root;
    }


    int dfs(TreeNode *r, int &ans) {
        if(r == NULL)   return -1;
        int d1 = dfs(r->left, ans);
        int d2 = dfs(r->right, ans);
        //--- root==NULL的时候返回了-1，所以+2 ---
        ans = max(ans, d1 + d2 + 2);
        return max(d1, d2) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int ans = 0;
        dfs(root, ans);
        return ans;
    }
};
 
int main() {
    Solution S;

    TreeNode* root = S.TreeStructor();

    cout << S.diameterOfBinaryTree(root) << endl;
    
    return 0;
}