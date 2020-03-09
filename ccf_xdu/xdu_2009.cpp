#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <string>
#include <stack>
#include <queue>

using namespace std;

typedef long long ll;


/*----------------------------------------------
Problems A
请写一个程序， 给出指定整数范围[a, b]内所有的完数，
一个数如果恰好等于除它本身以外的所有因子之和，这个
数就称为完数，例如6是完数，因为6=1+2+3.

输入说明：共一组数据为两个正整数，分别表示a和b
(1<a<b<10^5).

输出说明：指定范围内的所有完数， 每个数占一行。
------------------------------------------------*/
class SolutionA{
public:
    vector<int> find_all_perfect_numbers(int a, int b){
        vector<int> perfect_numbers;
        int c = a;
        while(c!=b){
            if(if_perfect_number(c)) perfect_numbers.push_back(c);
            c++;
        }
        return perfect_numbers;

    }
    bool if_perfect_number(int n){
        int factor_sum = 0;
        vector<int> factors;
        factors = find_factors(n);
        for(int i=0; i<factors.size(); ++i){
            factor_sum += factors[i];
        }
        if(factor_sum == n) return 1;
        return 0;
    }
    vector<int> find_factors(int n){
        int c=1;
        vector<int> factors;
        while(c!=n){
            if(n%c==0) factors.push_back(c);
            c++;
        }
        return factors;
    }

};

/*----------------------------------------------------------------
Problems B:
请写-一个程序，对于一个m行m列的(1<m<10)的方阵，求其每一行,
每一列及主对角线元素之和，最后按照从大到小的顺序一次输出。

输入说明:共一组数据，输入的一行为一个正整数，表示m, 接下来的m行，
每行m个整数表示方阵元素。

输出说明: 从大到小排列的一行整数，每个整数后跟一个空格，最后换行。
------------------------------------------------------------------*/
class SolutionB{
public:
    void sum_sort(vector<vector<int> > M){
        int Trace = trace(M);
        vector<int> Sum_row = sum_row(M);
        vector<int> Sum_col = sum_col(M);
        vector<int> sum;
        sum.push_back(Trace);
        for(int i=0; i<Sum_row.size(); ++i){
            sum.push_back(Sum_row[i]);
        }
        for(int i=0; i<Sum_col.size(); ++i){
            sum.push_back(Sum_col[i]);
        }
        sort(sum.begin(), sum.end());
        for(int i=sum.size()-1; i>=0; --i){
            cout << sum[i] << " ";
        }
        cout << endl;
    }
    vector<int> sum_row(vector<vector<int> > M){
        int sum = 0;
        vector<int> Sum_row;
        for(int i=0; i<M.size(); ++i){
            for(int j=0; j<M.size(); ++j){
                    sum += M[i][j];
            }
            Sum_row.push_back(sum);
            sum = 0;
        }
        return Sum_row;
    }
    vector<int> sum_col(vector<vector<int> > M){
        int sum = 0;
        vector<int> Sum_col;
        for(int i=0; i<M.size(); ++i){
            for(int j=0; j<M.size(); ++j){
                    sum += M[j][i];
            }
            Sum_col.push_back(sum);
            sum = 0;
        }
        return Sum_col;
    }
    int trace(vector<vector<int> > M){
        int sum = 0;
        for(int i=0; i<M.size(); ++i){
            for(int j=0; j<M.size(); ++j){
                if(i==j) sum += M[i][j];
            }
        }
        return sum;
    }
    vector<vector<int> > CreateMatrix(int n){
        vector<vector<int> > M;
        vector<int> N;
        srand(time(NULL));
        for(int i=0; i<n; ++i){
            for(int j=0; j<n; ++j){
                N.push_back(rand()%10);
            }
            M.push_back(N);
            N.erase(N.begin(), N.end());
        }
        return M;
    }
    void printMatrix(vector<vector<int> > M){
        for(int i=0; i<M.size(); ++i){
            for(int j=0; j<M.size(); ++j){
                    cout << M[i][j] << " ";
            }
            cout << endl;
        }
    }
};

/*-------------------------------------------------------------
Problems C:
对于给定的字符序列，从左至右将所有的数字字符取出来拼接成个无符号
整数(字符序列长度小于100，拼接出整数小于2^31)，计算并输出该整数
的一个最大因子(如果是素数，则其最大因子为自身)

输入说明:有多组数据，输入数据的第一行为一个正整数，表示字符序
列的数目，每组数据为一行字符序列。

输出说明:对每个字符序列，取出所得整数的最大因子，若字符序列中
没有数字或者找出的

输入:
    3
    sdf0ejg3.f?9f
    ?4afd0s&2d79*(g
    abcde

输出：
    13
    857
    0

-------------------------------------------------------------*/
class SolutionC{
public:
    ll str2num(string str){
        ll num = 0;
        for(int i=0; i<str.size(); ++i){
            if(str[i]>='0' && str[i] <='9'){
                num = num * 10 + str[i] - '0';
            }
        }
        cout << num << endl;
        if(num == 0) return 0;
        if(if_prime_number(num)) return num;
        ll factor = num - 1;
        while(1){
            if(num%factor==0 && if_prime_number(factor)) return factor;
            factor--;
        }
        return -1;
    }
    bool if_prime_number(ll num){
        ll i = 2;
        while(i!=num){
            if(num%i == 0) return 0;
            ++i;
        }
        return 1;
    }
};

/*------------------------------------------------------------------------
Problems D:
己知某二义树的先序序列和中序序列,编程计算并输出该二义树的后序序列。

入说明:仅一组数据,分为两行输入,第一行表示指定二叉树的先序序列,
第二行表示该 二义树的中序序列,序列元素均为大写英文字符,表示二义树的结点。

输出说明:第一行上输出该二又树的后序序列。

输入样本:
ABDGCEFH
DGBAECHF

输出样本:
GDBEHFCA
------------------------------------------------------------------------*/
struct TreeNode{
    char val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(ll x):
        val(x), left(NULL), right(NULL){
        }
};
// 本题的经验：vector的用法大部分都可以迁移到string上
class SolutionD{
public:
    TreeNode* reconstruct_Tree(string preOrder, string inOrder){
        if(preOrder.size()==0||inOrder.size()==0) return NULL;
        TreeNode *p = (TreeNode*)malloc(sizeof(TreeNode));
        p->val = preOrder[0];
        char root = preOrder[0];
        ll pos = inOrder.find(root);
        if(preOrder.begin()+ pos + 1 < preOrder.begin()+1){
            p->left = NULL;
        }else{
            p->left = reconstruct_Tree(string(preOrder.begin()+1, preOrder.begin()+pos+1),
                                       string(inOrder.begin(), inOrder.begin()+pos));
        }
        if(preOrder.begin()+pos+1>preOrder.end()){
            p->right = NULL;
        }else{
            p->right = reconstruct_Tree(string(preOrder.begin()+pos+1, preOrder.end()),
                                        string(inOrder.begin()+pos+1, inOrder.end()));
        }
        return p;
    }
    void print_Tree_preOrder(TreeNode* T){
        if(T==NULL) return;
        cout << T->val << ' ';
        print_Tree_preOrder(T->left);
        print_Tree_preOrder(T->right);
    }
    void print_Tree_inOrder(TreeNode* T){
        if(T==NULL) return;
        print_Tree_inOrder(T->left);
        cout << T->val << ' ';
        print_Tree_inOrder(T->right);
    }
    void print_Tree_postOrder(TreeNode* T){
        if(T==NULL) return;
        print_Tree_postOrder(T->left);
        print_Tree_postOrder(T->right);
        cout << T->val << ' ';
    }

};

/*-------------------------------------------------------------------
Problems E:
请写一个程序，判定给定表达式中的括号是否匹配， 表达式中的合法括号为
"(", ")", "[", "]", "{", "}"， 这三个括号的按照任意顺序嵌套使用。

输入说明：有多个表达式，输入数据的第一行是表达式的数目，每个表达式占
一行。

输出说明：对每个表达式，若其中的括号是匹配的，则输出“yes”， 否则输出
“no”。

输入样本
4
[(d+f)*{}]
[(2+3)]
()}
[4(6]7)9

输出样本:
yes
yes
no
no
-------------------------------------------------------------------*/
class SolutionE{
public:
    bool Parentheses_Matching(string str){
        stack<char> S;
        for(int i=0; i<str.size(); ++i){
            if(str[i]=='('||str[i]=='['||str[i]=='{') S.push(str[i]);
            if(str[i]==')'||str[i]==']'||str[i]=='}'){
                if(S.empty()) return 0;

                if(str[i]==')'){
                    if(S.top()!='('){
                        return 0;
                    }else{
                        S.pop();
                    }
                }
                if(str[i]==']'){
                    if(S.top()!='['){
                        return 0;
                    }else{
                        S.pop();
                    }
                }
                if(str[i]=='}'){
                    if(S.top()!='{'){
                        return 0;
                    }else{
                        S.pop();
                    }
                }
            }

        }

        if(!S.empty()) return 0;

        return 1;
    }
};

int main(){
//    int a, b;
//    cin >> a >> b;
//    vector<int> perfect_numbers;
//    SolutionA S;
//    perfect_numbers = S.find_all_perfect_numbers(a, b);
//    for(int i=0; i<perfect_numbers.size(); ++i){
//        cout << perfect_numbers[i] << ' ';
//    }
//    cout << endl;
//    return 0;

//    vector<vector<int> > M;
//    SolutionB S;
//    M = S.CreateMatrix(2);
//    S.printMatrix(M);
//    S.sum_sort(M);


//    int n;
//    string str;
//    SolutionC S;
//    cin >> n;
//    cin.ignore();
//    for(int i=0; i<n; ++i){
//        getline(cin, str);
//        cout << S.str2num(str) << endl;
//    }
//    return 0;

//    SolutionD S;
//    TreeNode *T;
//    string preOrder = "ABDGCEFH";
//    string inOrder = "DGBAECHF";
//    T = S.reconstruct_Tree(preOrder, inOrder);
//    S.print_Tree_postOrder(T);

    int n;
    string str;
    SolutionE S;
    cin >> n;
    cin.ignore();
    while(n--){
        getline(cin, str);
        cout << S.Parentheses_Matching(str) << endl;
    }
}
