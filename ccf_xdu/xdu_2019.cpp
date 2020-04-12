#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

/*--------------------------------------------------------------------
问题描述:
    给定一个整数数列，数列中连续相同的最长整数序列算成一段，问数列中共
    有多少段？

输入格式:
    输入的第一行包含一个整数n，表示数列中整数的个数。
　　第二行包含n个整数a1, a2, …, an，表示给定的数列，相邻的整数之间用一
个空格分隔。

输出格式:
    输出一个整数，表示给定的数列有多个段。

样例输入
8
8 8 8 0 12 12 8 0

样例输出
5

样例说明:
　　8 8 8是第一段，0是第二段，12 12是第三段，倒数第二个整数8是第四段，
最后一个0是第五段。
---------------------------------------------------------------------*/
class SolutionA {
   public:
    void ProblemA() {
        int n;
        ll c;
        vector<ll> a;
        cin >> n;
        while (n--) {
            cin >> c;
            a.push_back(c);
        }

        int pre = 0;
        int counter = 1;
        for (int i = 1; i < a.size(); ++i) {
            if (a[pre] != a[i]) {
                counter++;
                pre = i;
            }
        }
        cout << counter << endl;
    }
};

/*---------------------------------------------------------------------------
问题描述　　
    给定n个整数，请统计出每个整数各位数字和，按出现数字和从大到小的顺序输出。

输入格式　　
    输入的第一行包含一个整数n，表示给定数字的个数。　　
    第二行包含n个整数，相邻的整数之间用一个空格分隔，表示所给定的整数。

输出格式　　
    输出多行，每行包含两个整数，分别表示一个给定的整数和它出现的各位数字和。按出现
次数递减的顺序输出。如果两个整数出现的各位数字和相同，则先输出值较小的，然后输出
值较大的。

样例输入
5
101 100 999 1234 110

样例输出
999 27
1234 10
101 2
110 2
100 1
----------------------------------------------------------------------------*/
struct N {
    ll num;
    ll sum;
};

bool compare(N a, N b) {
    if (a.sum == b.sum) return a.num < b.num;
    return a.sum > b.sum;
}
class SolutionB {
   public:
    void ProblemB() {
        int n = 0;
        cin >> n;
        N c;
        vector<N> numVec;
        while (n--) {
            cin >> c.num;
            vector<ll> num = int2vec(c.num);
            c.sum = SumOfVec(num);
            numVec.push_back(c);
        }
        sort(numVec.begin(), numVec.end(), compare);
        for (int i = 0; i < numVec.size(); ++i) {
            cout << "num: " << numVec[i].num << " "
                 << "sum: " << numVec[i].sum << endl;
        }
    }

    vector<ll> int2vec(ll n) {
        vector<ll> num;
        while (n != 0) {
            num.insert(num.begin(), n % 10);
            n = n / 10;
        }
        return num;
    }

    ll SumOfVec(vector<ll> num) {
        ll sum = 0;
        for (int i = 0; i < num.size(); ++i) {
            sum += num[i];
        }
        return sum;
    }
};

/*-----------------------------------------------------------------------
问题描述
    消除类游戏是深受大众欢迎的一种游戏，游戏在一个包含有n行m列的游戏棋盘
上进行，棋盘的每一行每一列的方格上放着一个有颜色的棋子，当一行或一列上有
连续三个或更多的相同颜色的棋子时，这些棋子都被消除。当有多处可以被消除时，
这些地方的棋子将同时被消除。

请注意：一个棋子可能在某一行和某一列同时被消除。

    输入的第一行包含两个整数n, m，用空格分隔，分别表示棋盘的行数和列数。

    接下来n行，每行m个整数，用空格分隔，分别表示每一个方格中的棋子的颜色。
颜色使用1至9编号。

    输出n行，每行m个整数，相邻的整数之间使用一个空格分隔，表示经过一次消除
后的棋盘。如果一个方格中的棋子被消除，则对应的方格输出0，否则输出棋子的颜色
编号。

输入样例：
第一组：
4 5
2 2 3 1 2
3 4 5 1 4
2 3 2 1 3
2 2 2 4 4
第二组：
4 5
2 2 3 1 2
3 1 1 1 1
2 3 2 1 3
2 2 3 3 3

输出结果示例：
第一组：
2 2 3 0 2
3 4 5 0 4
2 3 2 0 3
0 0 0 4 4
第二组：
2 2 3 0 2
3 0 0 0 0
2 3 2 0 3
2 2 0 0 0

------------------------------------------------------------------------*/
/*------------------------------------------------------------------------
思路：要创建一个矩阵副本（get trick：以后遇到类似改变值的问题， 都可使用
副本来解决）， 原矩阵行或列三个相同，则将副本对应的位置置0.
------------------------------------------------------------------------*/
class SolutionC {
   public:
    void ProblemC() {
        int n, m, c;
        cin >> n >> m;
        int M[n][m], M1[n][m];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> c;
                M[i][j] = c;
                M1[i][j] = c;
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (M[i][j] == M[i][j + 1] && M[i][j + 1] == M[i][j + 2]) {
                    M1[i][j] = 0;
                    M1[i][j + 1] = 0;
                    M1[i][j + 2] = 0;
                }
            }
        }
        for (int j = 0; j < m; ++j) {
            for (int i = 0; i < n; ++i) {
                if (M[i][j] == M[i + 1][j] && M[i + 1][j] == M[i + 2][j]) {
                    M1[i][j] = 0;
                    M1[i + 1][j] = 0;
                    M1[i + 2][j] = 0;
                }
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cout << M1[i][j] << " ";
            }
            cout << endl;
        }
    }
};

/*----------------------------------------------------------------
题目描述：
    定义每个游戏由4个从1-9的数字和三个四则运算符组成，保证数字运算符
将数字两两隔开，不存在括号和其他字符，运算顺序按照四则运算顺序进行。其中
加法用符号‘+’表示，减法用符号‘-’表示，乘法用小写字母'x'表示，除法用符号
'/'表示，在游戏里除法为整除，例如2/3=0，3/2=1，4/2=2。

给出一个符合上述定义的表达式，请求出表达式的值

输入说明：
    输入是一个长度为7的字符串， 表示一个表达式

输出说明：
    输出一个整数，表示表达式求值的结果

输入样例：
    9+3+4x3
    1x9-5/9

输出样例：
    24
    9
------------------------------------------------------------------*/
class SolutionD {
public:
    void ProblemD() {
        string s;
        getline(cin, s);
        calculate(s);
    }

    int calculate(string s) {
        stack<ll> num;
        stack<char> sign;
        for(int i=0; i<s.size(); ++i){
            
            if(s[i]>='0' && s[i] <='9'){
                num.push(s[i]-'0');
            }else{
                if(s[i]=='+'){
                    sign.push(s[i]);
                }
                // 以下做法思路可借鉴，将减法转为加法
                // 且不拘泥于一个元素一个元素处理
                if(s[i]=='-'){
                    num.push((s[i+1] - '0') * (-1));
                    sign.push(s[i]);
                    ++i;
                }
                if(s[i]=='x'){
                    ll a = num.top(); num.pop();
                    ll b = s[i+1] - '0';
                    num.push(a*b);
                    ++i;
                }
                if(s[i]=='/'){
                    ll a = num.top(); num.pop();
                    ll b = s[i+1] - '0';
                    num.push(a/b);
                    ++i;
                }

            }    
        }
        while(!sign.empty()){
            sign.pop();
            ll a = num.top(); num.pop();
            ll b = num.top(); num.pop();
            num.push(a+b);
        } 
        cout << num.top() << endl;
    }
};



int main() {
    //    SolutionA S;
    //    S.ProblemA();

    //    SolutionB S;
    //    S.ProblemB();

    // SolutionC S;
    // S.ProblemC();

    SolutionD S;
    S.ProblemD();
    system("pause");
    return 0;
}
