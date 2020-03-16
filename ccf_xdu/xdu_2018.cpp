#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long ll;

/*-------------------------------------------------------------------------
Problems A:
近来、跳一跳这款小游戏风靡全国,受到不少玩家的喜爱。

简化后的跳一跳规则如下:玩家每次从当前方块跳到下一个方块,如果没有跳到
下一个方块上则游戏结束。

如果跳到了方块上,但没有跳到方块的中心则获得1分:跳到方块中心时,若上一
次的得分为1分或这是本局游戏的第一次跳跃则此次得分为2分,否则此次得分比
上一次得分多两分（即连续跳到方块中心时,总得分将+2,+4,+6,+8.)。

现在给出一个人跳一跳的全过程,请你求出他本局游戏的得分
（按照题目描述的规则）。

输入格式
输入包含多个数字,用空格分隔,每个数字都是1,2,0之一,1表示此次跳跃跳到了
方块上但是没有跳到中心,2表示此次跳跃跳到了方块上并且跳到了方块中心,0表
示此次跳跃没有跳到方块上（此时游戏结束）。

输出格式
输出一个整数,为本局游戏的得分（在本题的规则下)

样例输入
1 1 2 2 2 1 1 2 2 0
样例输出
22
数据规模和约定
对于所有测评用例，输入的数字不超过30个， 保证0正好出现一次且为最后一个数字
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
问题描述：
给出一个字符串和多行文字，在这些文字中找到字符串出现的那些行。你的程序还
需支持大小写敏感选项；当选项打开时，表示同一个字母的大写和小写看作不同的
字符；当选项关闭时，表示同一个字母的大写和小写看作相同的字符。

输入格式：
输入的第一行包含一个字符串s，由大小写英文字母组成。

第二行包含一个数字，表示大小写敏感的选项，当数字为0时表示大小写不敏感，当
数字为1时表示大小写敏感。

第三行包含一个整数n，表示给出的文字的行数。

接下来n行，每行包含一个字符串，字符串由大小写英文字母组成，不含空格和其他
字符。

输出格式：
输出多行，每行包含一个字符串，按出现的顺序依次给出那些包含了字符串S的行。

样例输入：
Hello
1
5
HelloWorld
HiHiHelloHiHi
GrepIsAGreatTool
HELLO
HELLOisNOTHello

样例输出：
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

    // 统一将字符串变为小写
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
问题描述：
在一个定义了直角坐标系的纸上， 画一个(x1, y1)到(x2, y2)的矩形指将横坐标
范围从x1到x2，纵坐标范围从y1到y2之间的区域涂上颜色。

图给出了一个画了两个矩形的例子。第一个矩形是(1,1)到(4,4),用绿色和紫色表示
第二个矩形是(2.3)到(6,5),用蓝色和紫色表示。图中,一共有15个单位的面积被涂
上颜色， 其中紫色部分被涂了两次,但在计算面积时只计算一次。在实际的涂色过
程中,所有的矩形都涂成统一的颜色,图中显示不同颜色仅为说明方便。

出所有要画的矩形,请问总多个单位的面积被涂上颜色。

输入格式
输入的第一行包含一个整数n,表尔要画的矩形的个数。
接下来 n 行,每行4个非负整数,分别表示要画的矩形的左下角的横坐标与纵坐标,以
及右上角的横坐标与纵坐标。

输出格式
输出一个整数,表示有少个单位的面积被涂上颜色。

样例输入
2
1 1 4 4
2 3 6 5

样例输出
15
----------------------------------------------------------------------*/
// 一开始我的想法是判断矩形的相对位置
// 一共有6种情况，包含在里面，在左上角，在右上角，在左下角，在右下角
// 或者没有包含

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
问题描述：
给定一组记录n(n<100)小明各个时期的考试成绩， 格式为日期+成绩， 中间以空格
隔开， 记录之间分行输入，例如

2008/6/3 80
2009/1/1 56

其中日期输入要求年份1996-2100 月份1-12 日期1-31
现要求以分数为关健字从大到1小对其进行排序,若分数相同则按日期从小到大排序

输入样例
4
2017/1/1 95
2017/6/10 85
2017/3/2 95
2017/1/1 65

输出样例
2017/1/1 95
2017/3/2 95
2017/6/10 85
2017/1/1 65
-------------------------------------------------------------------------*/
// 此题收获，对sort的使用，以及对日期的排序方法
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





