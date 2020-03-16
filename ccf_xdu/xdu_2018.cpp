#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long ll;

/*-------------------------------------------------------------------------
Problems A:
��������һ�����С��Ϸ����ȫ��,�ܵ�������ҵ�ϲ����

�򻯺����һ����������:���ÿ�δӵ�ǰ����������һ������,���û������
��һ������������Ϸ������

��������˷�����,��û�������������������1��:������������ʱ,����һ
�εĵ÷�Ϊ1�ֻ����Ǳ�����Ϸ�ĵ�һ����Ծ��˴ε÷�Ϊ2��,����˴ε÷ֱ�
��һ�ε÷ֶ����֣�������������������ʱ,�ܵ÷ֽ�+2,+4,+6,+8.)��

���ڸ���һ������һ����ȫ����,���������������Ϸ�ĵ÷�
��������Ŀ�����Ĺ��򣩡�

�����ʽ
��������������,�ÿո�ָ�,ÿ�����ֶ���1,2,0֮һ,1��ʾ�˴���Ծ������
�����ϵ���û����������,2��ʾ�˴���Ծ�����˷����ϲ��������˷�������,0��
ʾ�˴���Ծû�����������ϣ���ʱ��Ϸ��������

�����ʽ
���һ������,Ϊ������Ϸ�ĵ÷֣��ڱ���Ĺ�����)

��������
1 1 2 2 2 1 1 2 2 0
�������
22
���ݹ�ģ��Լ��
�������в�����������������ֲ�����30���� ��֤0���ó���һ����Ϊ���һ������
--------------------------------------------------------------------------*/
class SolutionA{
public:
    void ProblemsA(){
        vector<ll> A;
        ll n;
        while(cin >> n){
            A.push_back(n);
            if(n==0) break;
        }
        play(A);
    }
    void play(vector<ll> A){
        ll last_scores = 0, sum=0;
        for(int i=0; i<A.size(); ++i){
            if(A[i]==1){
                sum+=1;
                last_scores = 0;
            }
            if(A[i]==2){
                sum += (last_scores + 2);
                last_scores += 2;
            }
            if(A[i]==0){
                cout << sum << endl;
            }
        }

    }
};

/*-----------------------------------------------------------------------
Problems B:
����������
����һ���ַ����Ͷ������֣�����Щ�������ҵ��ַ������ֵ���Щ�С���ĳ���
��֧�ִ�Сд����ѡ���ѡ���ʱ����ʾͬһ����ĸ�Ĵ�д��Сд������ͬ��
�ַ�����ѡ��ر�ʱ����ʾͬһ����ĸ�Ĵ�д��Сд������ͬ���ַ���

�����ʽ��
����ĵ�һ�а���һ���ַ���s���ɴ�СдӢ����ĸ��ɡ�

�ڶ��а���һ�����֣���ʾ��Сд���е�ѡ�������Ϊ0ʱ��ʾ��Сд�����У���
����Ϊ1ʱ��ʾ��Сд���С�

�����а���һ������n����ʾ���������ֵ�������

������n�У�ÿ�а���һ���ַ������ַ����ɴ�СдӢ����ĸ��ɣ������ո������
�ַ���

�����ʽ��
������У�ÿ�а���һ���ַ����������ֵ�˳�����θ�����Щ�������ַ���S���С�

�������룺
Hello
1
5
HelloWorld
HiHiHelloHiHi
GrepIsAGreatTool
HELLO
HELLOisNOTHello

���������
HelloWorld
HiHiHelloHiHi
HELLOisNOTHello
-------------------------------------------------------------------------*/
class SolutionB{
public:
    void ProblemsB(){
        string Substr;
        ll if_sens;
        ll n;
        getline(cin, Substr);
        cin >> if_sens >> n;
        string str;
        cin.ignore();
        for(int i=0; i<n; ++i){
            getline(cin, str);
            if(!if_sens){
                string str_ = str2str(str);
                Substr = str2str(Substr);
                int pos = str_.find(Substr, 0);
                if(pos != -1) cout << str << endl;
            }
            else{
                int pos = str.find(Substr, 0);
                if(pos != -1) cout << str << endl;
            }
        }
    }

    // ͳһ���ַ�����ΪСд
    string str2str(string str){
        for(int i=0;i<str.size(); ++i){
            if(str[i]>='A' && str[i]<='Z'){
                str[i] += 'a' - 'A';
            }
        }
        return str;
    }

    int KMP(string S, string T, ll Next[]){
        S.insert(0, 1, '0');
        T.insert(0, 1, '0');
        int i = 1;
        int j = 1;
        while(i<=S.length()&&j<=T.length()){
            if(j==0 || S[i]==T[j]){
                cout << S[i] << " " << T[j] << endl;
                ++i; ++j;
            }
            else{
                j = Next[j];
            }
        }
        if(j>T.length())
            return (i - T.length()-1);
        return -1;
    }

    void getNext(string S, ll Next[]){
        S.insert(0, 1, '0');
        int i = 1;
        int j = 0;
        Next[1] = 0;
        while(i<=S.length()){
            if(j==0||S[i]==S[j]){
                ++i; ++j; Next[i] = j;
            }
            else{
                j = Next[j];
            }
        }
    }
};

/*---------------------------------------------------------------------
Problems C:
����������
��һ��������ֱ������ϵ��ֽ�ϣ� ��һ��(x1, y1)��(x2, y2)�ľ���ָ��������
��Χ��x1��x2�������귶Χ��y1��y2֮�������Ϳ����ɫ��

ͼ������һ�������������ε����ӡ���һ��������(1,1)��(4,4),����ɫ����ɫ��ʾ
�ڶ���������(2.3)��(6,5),����ɫ����ɫ��ʾ��ͼ��,һ����15����λ�������Ϳ
����ɫ�� ������ɫ���ֱ�Ϳ������,���ڼ������ʱֻ����һ�Ρ���ʵ�ʵ�Ϳɫ��
����,���еľ��ζ�Ϳ��ͳһ����ɫ,ͼ����ʾ��ͬ��ɫ��Ϊ˵�����㡣

������Ҫ���ľ���,�����ܶ����λ�������Ϳ����ɫ��

�����ʽ
����ĵ�һ�а���һ������n,���Ҫ���ľ��εĸ�����
������ n ��,ÿ��4���Ǹ�����,�ֱ��ʾҪ���ľ��ε����½ǵĺ�������������,��
�����Ͻǵĺ������������ꡣ

�����ʽ
���һ������,��ʾ���ٸ���λ�������Ϳ����ɫ��

��������
2
1 1 4 4
2 3 6 5

�������
15
----------------------------------------------------------------------*/
// һ��ʼ�ҵ��뷨���жϾ��ε����λ��
// һ����6����������������棬�����Ͻǣ������Ͻǣ������½ǣ������½�
// ����û�а���

struct pos{
    ll x1;
    ll y1;
    ll x2;
    ll y2;
};
class SolutionC{
public:
    void ProblemsC(){
        ll n;
        pos p;
        bool flag[100][100];
        cin >> n;
        ll S = 0;
        while(n--){
            cin >> p.x1 >> p.y1 >> p.x2 >> p.y2;
            cout << p.x1 << " " <<  p.y1 << " "
                << p.x2 << " " << p.y2 << endl;
            S += cal_S(p);
            for(int i=p.x1; i<p.x2; ++i){
                for(int j=p.y1; j<p.y2; ++j){
                    if(flag[i][j]==1)
                        S--;
                    flag[i][j] = 1;
                }
            }
        }
        cout << S << endl;


    }
    int abs(ll a, ll b){
        if(a > b) return a - b;
        else return b - a;
    }
    int cal_S(pos p){
        int width = abs(p.x2, p.x1);
        int height = abs(p.y2, p.y1);
        return height * width;
    }

};

/*------------------------------------------------------------------------
Problems D:
����������
����һ���¼n(n<100)С������ʱ�ڵĿ��Գɼ��� ��ʽΪ����+�ɼ��� �м��Կո�
������ ��¼֮��������룬����

2008/6/3 80
2009/1/1 56

������������Ҫ�����1996-2100 �·�1-12 ����1-31
��Ҫ���Է���Ϊ�ؽ��ִӴ�1С�����������,��������ͬ�����ڴ�С��������

��������
4
2017/1/1 95
2017/6/10 85
2017/3/2 95
2017/1/1 65

�������
2017/1/1 95
2017/3/2 95
2017/6/10 85
2017/1/1 65
-------------------------------------------------------------------------*/
// �����ջ񣬶�sort��ʹ�ã��Լ������ڵ����򷽷�
struct Info{
    int year;
    int month;
    int day;
    int scores;
};

bool compare_scores(Info a, Info b){
        return a.scores > b.scores;
}

bool compare_date(Info a, Info b){
    if(a.year==b.year){
        if(a.month==b.month){
            return a.day < b.day;
        }else{
            return a.month < b.month;
        }
    }
    else return a.year < b.year;
}

class SolutionD{
public:

    void ProblemsD(){
        vector<Info> info;
        Info temp;
        int year, month, day, scores;
        int n;
        cin >> n;
        while(n--){
            scanf("%d/%d/%d %d", &year, &month, &day, &scores);
            temp.year = year;
            temp.month = month;
            temp.day = day;
            temp.scores = scores;
            info.push_back(temp);
        }
        sort(info.begin(), info.end(), compare_scores);
        ll pre = 0;
        for(int i=1; i<info.size(); ++i){
            if(info[i].scores==info[pre].scores) continue;
            if(info[i].scores!=info[pre].scores){
                sort(info.begin()+pre, info.begin()+i, compare_date);
            }
        }
        for(int i=0; i<info.size(); ++i){
            printf("%d/%d/%d %d\n", info[i].year, info[i].month, info[i].day, info[i].scores);
        }
    }


};
int main(){
//    SolutionA S;
//    S.ProblemsA();

//    SolutionB S;
//    S.ProblemsB();

//    SolutionC S;
//    S.ProblemsC();

    SolutionD S;
    S.ProblemsD();
//    int year, month, day, scores;
//    cout << scanf("%d/%d/%d %d", &year, &month, &day, &scores) << endl;
    return 0;
}





