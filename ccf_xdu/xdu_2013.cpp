#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef long long ll;

/*-------------------------------------------------------------------
Problems A:
问题描述:
定义一个新的斐波那契数列
F(O)=7:
F(1)=11;
F(n)=F(n-1)+F(n-2];{n>=2)

输入:
输入有多组:首先输入一个 N（N<=100),代表要输入的测试用例的个数:接下来输入N个
数字 ni(ni<=100),数字间用空格隔开。

输出:
求F(n)能否被3整除,若能整除输出'yes',否则而出'no'

样例输入:
3
0 1 2

样例输出:
no
no
yes
--------------------------------------------------------------------*/
class SolutionA{
public:
    void if_divided(ll n){
        if(n%3 == 0) cout << "yes" << endl;
        else cout << "no" << endl;
    }
    ll Fibonaci(ll n){
        if(n==0) return 7;
        if(n==1) return 11;
        ll pre, pre_pre, cur;
        pre_pre = 7;
        pre = 7;
        for(int i=2; i<=n; ++i){
            cur = pre + pre_pre;
            pre_pre = pre;
            pre = cur;
        }
    }
};


/*---------------------------------------------------------------------
Problems B:
题目描述:
输入一组数据,统计每个数出现的次数,并按照数字的大小进行排序输出。

输入:
输入20个数字,数字之间用空格隔开。

输出:
统计每个数字出现的次数,并按数字的大小输出数字及其出现的次数。

样例输入:
9 8 5 1 7 2 8 2 9 10 1 7 8 9 5 6 9 0 1 9

样例输出：
0:1
1:3
2:2
5:2
6:1
7:2
8:3
9:5
10:1
---------------------------------------------------------------------*/
class SolutionB{
public:
    void number_times(ll a[]){
        for(int i=0; i<100; ++i){
            if(a[i]!=0){
                cout << i << ":" << a[i] << endl;
            }
        }
    }
};

/*---------------------------------------------------------------------
Problems C:
题目描述:
每个英文字母出现的频率对其进行哈弗曼编码、其中‘#’代表空格,其编码方式如下
（此处略去编码方式(因为比较多不易记忆）

输入:
从文件（ecode.txt）中读入要输入的测试用例,测试用例总长度不超过 1000。

输出:
输出解码后的测试用例,包含其中的空格
---------------------------------------------------------------------*/
//因为没有文件，所以就练习一下文件读写和哈夫曼树
struct Node{
    ll weight;
    ll lchild, rchild, parent, length;
};
class SolutionC{
public:
    vector<Node> HuffmanTree_Structor(vector<Node> Tree){
        vector<Node> B = Tree;
        Node T;
        ll Min, Second_Min;
        ll times = Tree.size();
        for(int i=0; i<(times-1); ++i){
            Min = find_min(B);
            Second_Min = find_min(B);
            T.weight = Tree[Min].weight + Tree[Second_Min].weight;
            T.lchild = Min;
            T.rchild = Second_Min;
            T.parent = -1;
            B.push_back(T);
            Tree.push_back(T);
            Tree[Min].parent = B.size()-1;
            Tree[Second_Min].parent = B.size()-1;
        }
        return Tree;

    }

    vector<Node> Init_HuffmanTree(vector<ll> A){
        vector<Node> Tree;
        Node T;
        for(int i=0; i<A.size(); ++i){
            T.weight = A[i];
            T.length = 0;
            T.parent = -1;
            Tree.push_back(T);
        }
        return Tree;
    }
    ll find_min(vector<Node> &Tree){
        ll pos = 0;
        while(Tree[pos].weight == -1) ++pos;
        ll Min = Tree[pos].weight;

        for(int i=0; i<Tree.size(); ++i){
            if(Tree[i].weight<Min && Tree[i].weight != -1){
                Min = Tree[i].weight;
                pos = i;
            }
        }
        Tree[pos].weight = -1;
        return pos;

    }
    void HuffmanCode_length(vector<Node> &Tree, int n){
        for(int i=0; i<n; ++i){
            Node T = Tree[i];
            while(T.parent != -1){
                T = Tree[T.parent];
                Tree[i].length++;
            }
        }
    }
    ll Huffman_weight_length(vector<Node> Tree, int n){
        ll sum = 0;
        for(int i=0; i<n; ++i){
            sum += Tree[i].length * Tree[i].weight;
        }
        return sum;
    }
    void printHuffmanTree(vector<Node> Tree){
        for(int i=0; i<Tree.size(); ++i){
            cout << Tree[i].weight << " ";
        }
        cout << endl;
    }
    string file_read(string filename){
        string str;
        ifstream in(filename);
        while(in >> str){
            cout << str << endl;
        }
        in.close();
        return str;

    }

    void file_write(string str){
        ofstream out("test1.txt");
        out << str;
        out.close();

    }
};


/*-----------------------------------------------------------------------
Problems D:
问题描述:二进制与十进制的相互转换,输入一组数据,若为十进制,则将其转换为二进制:
若为二进制则将其转换为十进制。其中所要转换的十进制与二进制的十进制大于零小于
等于255。

输入:测试用例包含多组,每组有两个数n和 m,n为所输入的数值,m为输入数的进制,
如 m=2,代表所输入的n是二进制数。当m和n均为零是表示输出结束。

输出：若输入的数是十进制,则将其转换为二进制;若所输入的数为二进制,则将其转换为
十进制,并输出。每个结果对应一行,最后输出换行。

样例输入:
10 2
10 10
0 0

样例输出
2
1010
-----------------------------------------------------------------------*/
class SolutionD{
public:
    string to_string(ll n){
        string str;
        while(n!=0){
            str.insert(0,1,(n%10)+'0');
            n /= 10;
        }
        return str;
    }
    ll B2D(ll N){
        string B = to_string(N);
        ll sum = 0;
        ll n = 1;
        for(int i=(B.length()-1); i>=0; --i){
            sum += (B[i] - '0') * n;
            n *= 2;
        }
        return sum;
    }

    void D2B(ll n){
        vector<ll> B;
        while(n!=0){
            B.insert(B.begin(), n%2);
            n /= 2;
        }
        for(int i=0; i<B.size(); ++i){
            cout << B[i];
        }
        cout << endl;
    }

};



int main(){
//    ll N;
//    cin >> N;
//    ll n;
//    SolutionA S;
//    for(int i=0; i<N; ++i){
//        cin >> n;
//        S.if_divided(S.Fibonaci(n));
//    }

//    ll a[100] = {0};
//    ll n;
//    for(int i=0; i<20; ++i){
//        cin >> n;
//        a[n]++;
//    }
//    SolutionB S;
//    S.number_times(a);

//    SolutionC S;
//    ll n, m;
//    vector<ll> A;
//    cin >> n;
//    for(int i=0; i<n; ++i){
//        cin >> m;
//        A.push_back(m);
//    }
//    vector<Node> Tree;
//    Tree = S.Init_HuffmanTree(A);
//
//    Tree = S.HuffmanTree_Structor(Tree);
//    S.printHuffmanTree(Tree);
//
//    S.HuffmanCode_length(Tree, n);
//    cout << S.Huffman_weight_length(Tree, n) << endl;

//    SolutionC S;
//    string str;
//
//    str = S.file_read("test.txt");
//
//    S.file_write(str);





    SolutionD S;
    ll n, m;
    while(1){
        cin >> n;
        cin >> m;
        if(n==0&&m==0) break;
        if(m==2){
            cout << S.B2D(n) << endl;
        }
        if(m==10){
            S.D2B(n);
        }
    }




    return 0;
}


