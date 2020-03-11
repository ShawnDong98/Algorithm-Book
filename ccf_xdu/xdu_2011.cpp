#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
/*----------------------------------------------------------------------
Problems A:
编写一个程序,从键盘输入n个非零整数（0<n<1000）,将这n个数中每个数的
各位数字取出来相加, 并按照从小到大的次序一次输出这些数字和。
例如,497的各位数字和为20(4+9+7),1069的各位数字和为16（1+0+6+9)

输入格式说明:输入整数之间以空格分隔,输入0时结束。

输出格式说明:在一行上从小到大输出计算结果,整数之间用1个空格分隔,最后换行。

输入示例:
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
写一个程序,找出给定矩阵的马鞍点， 若一个矩阵中的某元素在其所在行最小而在
其所在列最大,则该元素为矩阵的一个马鞍点。

输入说明:输入数据由m+1行构成， 第一行只有两个整数m和n(0<m<100.0<n<100）,
分别表示矩阵的行数和列数, 接下来来的m行、每行n个整数表示矩阵元素（矩阵中
的元素不同）。整数之间以空格间隔。

输出说明:在一行上输出马鞍点的行号、列号(行号和列号从0开始记数)及元素的值
（用一个空格分隔）,之后换行；若不存在马鞍点,则输出一个字符串"no"后换行。

输入示例:(注意:本题裁判机上偷入数据的第一有整数不一定是4和3）
4 3
11 13 121
407 72 88
25 58 1
134 30 62


输出示例:
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
有一种简单的字符串压缩算法,对于字符串中连续出现的同一个字符,用该字符串
加上连续出现的次数来表示（连续出现次数小于3时不压缩），例如， 字符串
aaabbbabaaaaaaaaabbb可压缩为a5b3aba13b4、请设计一个程序,将采用该压缩方
法得到的字符串解压缩,还原出原字符串并输出。

输入格式说明:在一行上输入一个字符串。(长多不超过50)

出格式说明:在一行上输出解压缩后的字符串（长度不超过100）,最后换行

输入示例:
a5b3aba13b4

输出示例:
aaaaabbbabaaaaaaaaaaaabbbb
--------------------------------------------------------------------*/
class SolutionC{
public:
    void unzip_str(string str){
        ll pre = 0;
        string str_num;
        for(int i=1;i<str.size();++i){
            // 要保证pre指针在i指针前面
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
用于通信的电文由n(4<n<30)个字符组成， 字符在电文中出现的频度（权值）为
w1，w2,,,,wn,试根据该权值序列构成哈大蔓树,并计算该树的带权路径长度。

输入说明:
仅一组数据,为两行输入:
第一行为n的值,第二行为n 个整数,表示字符出现的频度

输出说明:一个整数,表示所构造哈夫曼树的带圈路径长度（输出整数后换行）。
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
