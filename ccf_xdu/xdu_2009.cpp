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
��дһ������ ����ָ��������Χ[a, b]�����е�������
һ�������ǡ�õ��ڳ��������������������֮�ͣ����
���ͳ�Ϊ����������6����������Ϊ6=1+2+3.

����˵������һ������Ϊ�������������ֱ��ʾa��b
(1<a<b<10^5).

���˵����ָ����Χ�ڵ����������� ÿ����ռһ�С�
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
��д-һ�����򣬶���һ��m��m�е�(1<m<10)�ķ�������ÿһ��,
ÿһ�м����Խ���Ԫ��֮�ͣ�����մӴ�С��˳��һ�������

����˵��:��һ�����ݣ������һ��Ϊһ������������ʾm, ��������m�У�
ÿ��m��������ʾ����Ԫ�ء�

���˵��: �Ӵ�С���е�һ��������ÿ���������һ���ո�����С�
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
���ڸ������ַ����У��������ҽ����е������ַ�ȡ����ƴ�ӳɸ��޷���
����(�ַ����г���С��100��ƴ�ӳ�����С��2^31)�����㲢���������
��һ���������(����������������������Ϊ����)

����˵��:�ж������ݣ��������ݵĵ�һ��Ϊһ������������ʾ�ַ���
�е���Ŀ��ÿ������Ϊһ���ַ����С�

���˵��:��ÿ���ַ����У�ȡ������������������ӣ����ַ�������
û�����ֻ����ҳ���

����:
    3
    sdf0ejg3.f?9f
    ?4afd0s&2d79*(g
    abcde

�����
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
��֪ĳ���������������к���������,��̼��㲢����ö������ĺ������С�

��˵��:��һ������,��Ϊ��������,��һ�б�ʾָ������������������,
�ڶ��б�ʾ�� ����������������,����Ԫ�ؾ�Ϊ��дӢ���ַ�,��ʾ�������Ľ�㡣

���˵��:��һ��������ö������ĺ������С�

��������:
ABDGCEFH
DGBAECHF

�������:
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
// ����ľ��飺vector���÷��󲿷ֶ�����Ǩ�Ƶ�string��
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
��дһ�������ж��������ʽ�е������Ƿ�ƥ�䣬 ���ʽ�еĺϷ�����Ϊ
"(", ")", "[", "]", "{", "}"�� ���������ŵİ�������˳��Ƕ��ʹ�á�

����˵�����ж�����ʽ���������ݵĵ�һ���Ǳ��ʽ����Ŀ��ÿ�����ʽռ
һ�С�

���˵������ÿ�����ʽ�������е�������ƥ��ģ��������yes���� �������
��no����

��������
4
[(d+f)*{}]
[(2+3)]
()}
[4(6]7)9

�������:
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
