/*-----------------------------------------------
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
-----------------------------------------------*/
#include <iostream>
#include <stdlib.h>\

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
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if(pRoot2==NULL || (pRoot1==NULL&&pRoot2!=NULL)) return 0;
        if(Tree_if_same(pRoot1, pRoot2)==1) return 1;
        if(HasSubtree(pRoot1->left, pRoot2)) return 1;
        if(HasSubtree(pRoot1->right, pRoot2)) return 1;
        return 0;
    }
    bool Tree_if_same(TreeNode* pRoot1, TreeNode* pRoot2){
        if(pRoot2==NULL) return 1;
        if((pRoot1==NULL&&pRoot2!=NULL)) return 0;
        if(pRoot1->val!=pRoot2->val) return 0;
        else{
            return Tree_if_same(pRoot1->left, pRoot2->left) & Tree_if_same(pRoot1->right, pRoot2->right);
        }

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
    TreeNode *T_1, *T_2;
    Solution S;

    S.Tree_Structor(T_1, 5);
    //S.print_Tree(T_1);

    S.Tree_Structor(T_2, 4);
    //S.print_Tree(T_2);

    cout << S.HasSubtree(T_1, T_2) << endl;


    return 0;
}
