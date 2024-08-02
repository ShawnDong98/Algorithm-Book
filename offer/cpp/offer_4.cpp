/*--------------------------------------------------
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉
树。假设输入的前序遍历和中序遍历的结果中都不含重复的数
字。例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列
{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
---------------------------------------------------*/
#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int find(vector<int> vec, int target){
        for(int i=0; i<vec.size(); ++i){
            if(vec[i] == target) return i;
        }
        return -1;
    }

    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        if(pre.size()==0||vin.size()==0){
            return NULL;
        }
        TreeNode* p = (TreeNode*)malloc(sizeof(TreeNode));
        p->val = pre[0];
        int pos = find(vin, pre[0]);
        if(pre.begin() > pre.begin() + pos){
            p->left = NULL;
        }else{

            p->left = reConstructBinaryTree(vector<int>(pre.begin()+1, pre.begin()+pos+1),
                                            vector<int>(vin.begin(), vin.begin()+pos));
        }
        if(pre.begin() + pos + 1 > pre.end()){
            p->right = NULL;
        }else{
            p->right = reConstructBinaryTree(vector<int>(pre.begin()+pos+1, pre.end()),
                                             vector<int>(vin.begin()+pos+1, vin.end()));
        }
        return p;
    }


    void printTree(TreeNode* root){
        if(root==NULL) return;
        cout << root->val << ' ';
        printTree(root->left);
        printTree(root->right);
    }
};

int main(){
    int a[7]={1,2,4,5,3,6,7};
    int b[7]={4,2,5,1,6,3,7};
    vector<int> pre(a, a+7);
    vector<int> vin(b, b+7);

    Solution S;

    TreeNode *newRoot = S.reConstructBinaryTree(pre, vin);

//    // 这种方式得到的是两个地址之间截到的的变量
//    vector<int> test = vector<int>(vin.begin(), vin.begin()+1);
//
//    for(vector<int>::iterator it=test.begin(); it!=test.end(); ++it){
//        cout << *it << ' ';
//    }

    S.printTree(newRoot);

    return 0;
}
