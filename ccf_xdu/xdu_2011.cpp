#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
/*----------------------------------------------------------------------
Problems A:
��дһ������,�Ӽ�������n������������0<n<1000��,����n������ÿ������
��λ����ȡ�������, �����մ�С����Ĵ���һ�������Щ���ֺ͡�
����,497�ĸ�λ���ֺ�Ϊ20(4+9+7),1069�ĸ�λ���ֺ�Ϊ16��1+0+6+9)

�����ʽ˵��:��������֮���Կո�ָ�,����0ʱ������

�����ʽ˵��:��һ���ϴ�С�������������,����֮����1���ո�ָ�,����С�

����ʾ��:
497 1069 68 71 137 0
-----------------------------------------------------------------------*/
class SolutionA{
public:
    void sum_sort(vector<ll> numbers){
        vector<ll> sums;
        for(int i=0; i<numbers.size(); ++i){
            sums.push_back(sum_bits(numbers[i]));
        }
        sort(sums.begin(), sums.end());
        for(int i=0; i<numbers.size(); ++i){
            cout << sums[i] << ' ';
        }
    }
    ll sum_bits(ll n){
        vector<ll> cache;
        while(n!=0){
            cache.push_back(n%10);
            n /= 10;
        }
        ll sum = 0;
        for(int i=0; i<cache.size(); ++i){
            sum += cache[i];
        }
        return sum;
    }
};

/*--------------------------------------------------------------------
Problems B:
дһ������,�ҳ�������������㣬 ��һ�������е�ĳԪ��������������С����
�����������,���Ԫ��Ϊ�����һ�����㡣

����˵��:����������m+1�й��ɣ� ��һ��ֻ����������m��n(0<m<100.0<n<100��,
�ֱ��ʾ���������������, ����������m�С�ÿ��n��������ʾ����Ԫ�أ�������
��Ԫ�ز�ͬ��������֮���Կո�����

���˵��:��һ�������������кš��к�(�кź��кŴ�0��ʼ����)��Ԫ�ص�ֵ
����һ���ո�ָ���,֮���У�������������,�����һ���ַ���"no"���С�

����ʾ��:(ע��:������л���͵�����ݵĵ�һ��������һ����4��3��
4 3
11 13 121
407 72 88
25 58 1
134 30 62


���ʾ��:
1 1 72
----------------------------------------------------------------------*/
class SolutionB{
public:
    void find_Saddle_point(vector<vector<ll> > M){
        ll min = 0, max = 0;
        ll row = 0, col = 0;
        ll flag = 0;
        for(int i=0; i<M.size(); ++i){
            min = M[i][0];
            col = 0;
            for(int j=0; j<M[i].size(); ++j){
                if(M[i][j]<min){
                    min = M[i][j];
                    col = j;
                }
            }
            max = min;
            for(int k=0; k<M.size(); ++k){
                if(M[k][col]>max){
                    max = M[k][col];
                    row = k;
                }
            }
            if(max == min){
                cout << row << ' ' << col << ' ' << M[row][col] << endl;
                flag = 1;
            }
        }
        if(flag==0) cout << "no" << endl;
    }
};

/*-------------------------------------------------------------------
Problems C:
��һ�ּ򵥵��ַ���ѹ���㷨,�����ַ������������ֵ�ͬһ���ַ�,�ø��ַ���
�����������ֵĴ�������ʾ���������ִ���С��3ʱ��ѹ���������磬 �ַ���
aaabbbabaaaaaaaaabbb��ѹ��Ϊa5b3aba13b4�������һ������,�����ø�ѹ����
���õ����ַ�����ѹ��,��ԭ��ԭ�ַ����������

�����ʽ˵��:��һ��������һ���ַ�����(���಻����50)

����ʽ˵��:��һ���������ѹ������ַ��������Ȳ�����100��,�����

����ʾ��:
a5b3aba13b4

���ʾ��:
aaaaabbbabaaaaaaaaaaaabbbb
--------------------------------------------------------------------*/
class SolutionC{
public:
    void unzip_str(string str){
        ll pre = 0;
        string str_num;
        for(int i=1;i<str.size();++i){
            // Ҫ��֤preָ����iָ��ǰ��
            pre = i-1;
            if(str[i]>='0'&&str[i]<='9'){
                ll j = i;
                while(str[j]>='0'&&str[j]<='9'){
                    str_num.append(1, str[j]);
                    ++j;
                }
                ll num = str2num(str_num);
                cout << num << endl;
                str.erase(str.begin()+i, str.begin()+j);
                str.insert(i, num-1, str[pre]);
                str_num.erase(str_num.begin(), str_num.end());
                cout << str << endl;
                i = i + num - 1;
                pre = i;
            }

        }
        cout << str << endl;
    }
    ll str2num(string str_num){
        ll num = 0;
        for(int i=0; i<str_num.size();++i){
            num = 10 * num + (str_num[i] - '0');
        }
        return num;
    }
};

/*----------------------------------------------------------------
Problems D:
����ͨ�ŵĵ�����n(4<n<30)���ַ���ɣ� �ַ��ڵ����г��ֵ�Ƶ�ȣ�Ȩֵ��Ϊ
w1��w2,,,,wn,�Ը��ݸ�Ȩֵ���й��ɹ�������,����������Ĵ�Ȩ·�����ȡ�

����˵��:
��һ������,Ϊ��������:
��һ��Ϊn��ֵ,�ڶ���Ϊn ������,��ʾ�ַ����ֵ�Ƶ��

���˵��:һ������,��ʾ��������������Ĵ�Ȧ·�����ȣ�����������У���
-----------------------------------------------------------------*/
struct Node{
    ll weight;
    ll lchild, rchild, parent;
};

class SolutionD{
public:
     void Huffman_Tree_Structor(vector<Node> Tree){
        vector<Node> A = Tree;
        Node T;
//        ll min = find_min(A);
//        ll second_min = find_min(A);
//        printTree(A);
        ll t = Tree.size();
        for(int i=0; i<t-1; ++i){
            ll min = find_min(A);
            ll second_min = find_min(A);
            T.weight = Tree[min].weight + Tree[second_min].weight;
            T.lchild = min;
            T.rchild = second_min;
            A.push_back(T);
            Tree.push_back(T);
        }
        printTree(Tree);

    }
    vector<Node> Init_Huffman_Tree(vector<ll> A){
        Node T;
        vector<Node> Tree;
        for(int i=0; i<A.size(); ++i){
            T.weight = A[i];
            T.parent = -1;
            Tree.push_back(T);
        }
        return Tree;
    }
    ll find_min(vector<Node> &A){
        ll min_mark = 0;
        //for(min_mark=0; A[min_mark].weight!=-1; ++min_mark);
        while(A[min_mark].weight==-1){
            min_mark++;
        }

        ll Min = A[min_mark].weight;

        for(int i=0; i<A.size(); ++i){
            if(A[i].weight<Min&&A[i].weight!=-1){
                Min = A[i].weight;
                min_mark = i;
            }
        }
        A[min_mark].weight = -1;
        return min_mark;
    }
    void printTree(vector<Node> Tree){
        for(int i=0; i<Tree.size(); ++i){
            cout << Tree[i].weight << " ";
        }
        cout << endl;
    }
};

int main(){
//    vector<ll> numbers;
//    ll n;
//    SolutionA S;
//    while(1){
//        cin >> n;
//        if(n==0) break;
//        numbers.push_back(n);
//    }
//    S.sum_sort(numbers);

//    ll m, n;
//    ll temp;
//    cin >> m;
//    cin >> n;
//    vector<vector<ll> > M;
//    vector<ll> N;
//    for(int i=0; i<m; ++i){
//        for(int j=0; j<n; ++j){
//            cin >> temp;
//            N.push_back(temp);
//        }
//        M.push_back(N);
//        N.erase(N.begin(), N.end());
//    }
//    SolutionB S;
//
//    S.find_Saddle_point(M);

//    string str;
//    getline(cin, str);
//    SolutionC S;
//    S.unzip_str(str);

    SolutionD S;
    vector<Node> Tree;
    vector<ll> A;
    ll n, m;
    cin >> n;
    for(int i=0; i<n; ++i){
        cin >> m;
        A.push_back(m);
    }

    Tree = S.Init_Huffman_Tree(A);
    S.printTree(Tree);
    S.Huffman_Tree_Structor(Tree);
    return 0;
}
