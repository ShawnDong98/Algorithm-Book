/*---------------------------------------------
操作给定的二叉树，将其变换为源二叉树的镜像。
---------------------------------------------*/
#include <iostream>
#include <stdlib.h>

using namespace std;

struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};

class Solution {
public:
    void Mirror(TreeNode *pRoot) {
        if(pRoot==NULL) return;
        TreeNode* p = (TreeNode*)malloc(sizeof(TreeNode));
        p->left = pRoot->left;
        p->right = pRoot->right;
        pRoot->left = p->right;
        pRoot->right = p->left;
        delete p;
        Mirror(pRoot->left);
        Mirror(pRoot->right);
    }
    void Tree_Structor(TreeNode* &T, int n){
        if(n<=0){T = NULL; return;}
        T = (TreeNode*)malloc(sizeof(TreeNode));
        T->val = n;
        Tree_Structor(T->left, n-1);
        Tree_Structor(T->right, n-2);
    }
    void print_Tree(TreeNode* T){
        if(T==NULL) return;
        cout << T->val << ' ';
        print_Tree(T->left);
        print_Tree(T->right);
    }
};

int main(){
    TreeNode* T;
    Solution S;

    S.Tree_Structor(T, 5);

    S.print_Tree(T);
    cout << endl;

    S.Mirror(T);

    S.print_Tree(T);
    cout << endl;

    return 0;
}
