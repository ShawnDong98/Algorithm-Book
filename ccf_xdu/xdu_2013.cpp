#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

typedef long long ll;

/*-------------------------------------------------------------------
Problems A:
��������:
����һ���µ�쳲���������
F(O)=7:
F(1)=11;
F(n)=F(n-1)+F(n-2];{n>=2)

����:
�����ж���:��������һ�� N��N<=100),����Ҫ����Ĳ��������ĸ���:����������N��
���� ni(ni<=100),���ּ��ÿո������

���:
��F(n)�ܷ�3����,�����������'yes',�������'no'

��������:
3
0 1 2

�������:
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
��Ŀ����:
����һ������,ͳ��ÿ�������ֵĴ���,���������ֵĴ�С�������������

����:
����20������,����֮���ÿո������

���:
ͳ��ÿ�����ֳ��ֵĴ���,�������ֵĴ�С������ּ�����ֵĴ�����

��������:
9 8 5 1 7 2 8 2 9 10 1 7 8 9 5 6 9 0 1 9

���������
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
��Ŀ����:
ÿ��Ӣ����ĸ���ֵ�Ƶ�ʶ�����й��������롢���С�#������ո�,����뷽ʽ����
���˴���ȥ���뷽ʽ(��Ϊ�Ƚ϶಻�׼��䣩

����:
���ļ���ecode.txt���ж���Ҫ����Ĳ�������,���������ܳ��Ȳ����� 1000��

���:
��������Ĳ�������,�������еĿո�
---------------------------------------------------------------------*/
//��Ϊû���ļ������Ծ���ϰһ���ļ���д�͹�������
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
��������:��������ʮ���Ƶ��໥ת��,����һ������,��Ϊʮ����,����ת��Ϊ������:
��Ϊ����������ת��Ϊʮ���ơ�������Ҫת����ʮ����������Ƶ�ʮ���ƴ�����С��
����255��

����:����������������,ÿ����������n�� m,nΪ���������ֵ,mΪ�������Ľ���,
�� m=2,�����������n�Ƕ�����������m��n��Ϊ���Ǳ�ʾ���������

����������������ʮ����,����ת��Ϊ������;�����������Ϊ������,����ת��Ϊ
ʮ����,�������ÿ�������Ӧһ��,���������С�

��������:
10 2
10 10
0 0

�������
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


