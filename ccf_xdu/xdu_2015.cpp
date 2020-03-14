#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

typedef long long ll;

/*--------------------------------------------------------------------
Problems A:
求一串数中大于1的素数之和
输入不超过100个数 不超过10 组 输入0结束

例：

输入
4 1 2 3 4
5 1 2 3 4 5
0

输出
5
10
---------------------------------------------------------------------*/
//此题收获在于不容易判断换行符时，读入一行数据的处理方式
class SolutionA{
public:
    void ProblemsA(){
        string line;
        vector<ll> A;
        while(1){
            getline(cin, line);
            if(line[0]=='0') break;
            cout << prime_num_sum(str2vec(line)) << endl;
        }

    }
    ll prime_num_sum(vector<ll> A){
        vector<ll> prime_nums;
        for(int i=0; i<A.size(); ++i){
            if(if_prime_number(A[i])){
               vector<ll>::iterator pos = find(prime_nums.begin(), prime_nums.end(), A[i]);
               if(pos == prime_nums.end()) prime_nums.push_back(A[i]);
            }
        }
        ll sum = 0;
        for(int i=0; i<prime_nums.size(); ++i){
                sum += prime_nums[i];
        }
        return sum;
    }
    bool if_prime_number(ll n){
        if(n==0 || n==1) return 0;
        ll i = 2;
        while(i!=n){
            if(n%i==0) return 0;
            i++;
        }
        return 1;
    }
    vector<ll> str2vec(string line){
        vector<ll> A;
        for(int i=0; i<line.size(); ++i){
            if(line[i]>'0' && line[i]<='9'){
                A.push_back(line[i] - '0');
            }
        }
        return A;
    }
};

/*-------------------------------------------------------------------------
Problems B:

压缩字符串
输入只含A-Z的字符串 不超过1000个字母将连续相同字母压缩为重复次数+字母（这个
忘记是多组输入还是单组了）

例：

输入
ABBCCC

输出
A2B3C
-------------------------------------------------------------------------*/
class SolutionB{
public:
    void ProblemsB(){
        string str;
        getline(cin, str);
        ll pre = 0;
        ll Size = str.size();
        for(int i=1; i<Size; ++i){
            if(str[pre]==str[i]) continue;
            else{
                if(i-pre>1){
                    char c = str[i-1];
                    str.erase(str.begin()+pre, str.begin()+i-1);
                    str.insert(pre, 1, i-pre+'0');
                    str.insert(pre+1, 1, c);
                }
                pre = i;
            }
        }
        if(Size-pre>1){
            char c = str[Size-1];
            str.erase(str.begin()+pre, str.begin()+Size-1);
            str.insert(pre, 1, Size-pre+'0');
            str.insert(pre+1, 1, c);
        }
        cout << str << endl;
    }
};

/*---------------------------------------------------------------------
Problems C:
机器人走迷宫
迷宫由 N W S E 组成 踩到N向上走一格 踩到W向左走一格 踩到S向下走一格 踩到
E向右走一格

输入迷宫行数、列数（不大于10）、机器人初始列数（注意这个列数是从1开始数的）
判断能否走出迷宫。能走出输出步数

多组输入 遇 0 0 0 结束输入

例

输入
4 6 5
NNNNSN
NNNSWN
NNSWNN
NSWNNN
3 5 2
NSNNN
NSWNN
NENNN
0 0 0
输出
7
No
---------------------------------------------------------------------*/
struct maze{
    bool passed;
    char direction;
//    maze(bool x, char d): passed(x), direction(d){
//    }
};

class SolutionC{
public:
    void ProblemsC(){
        ll m, n, init_col;
        while(cin >> m >> n >> init_col){
            if(m==0&&n==0&&init_col==0) return;
            char t;
            vector<vector<char> > M;
            vector<char> N;
            for(int i=0; i<m; ++i){
                for(int j=0; j<n; ++j){
                    cin >> t;
                    N.push_back(t);
                }
                M.push_back(N);
                N.erase(N.begin(), N.end());
            }
            vector<vector<maze> > Maze;
            Maze = CreateMaze(m, n, M);
            play(Maze, init_col-1);
        }

    }
    void play(vector<vector<maze> > Maze, ll init_col){
        ll i = 0, j = init_col;
        ll counter = 0;
        while(1){
            if(Maze[i][j].passed==1){
                cout << "No" << endl;
                cout << "because of me" << endl;
                return;
            }
            Maze[i][j].passed = 1;
            ++counter;
            if(Maze[i][j].direction=='N'){
                --i;
                if(i<0 || j<0 || j>Maze[0].size()-1){
                    cout << "No" << endl;
                    return;
                }
                if(i>Maze.size()-1){
                    cout << counter << endl;
                    return;
                }
                continue;
            }
            if(Maze[i][j].direction=='S'){
                ++i;
                if(i<0 || j<0 || j>Maze[0].size()-1){
                    cout << "No" << endl;
                    return;
                }
                if(i>Maze.size()-1){
                    cout << counter << endl;
                    return;
                }
                continue;

            }
            if(Maze[i][j].direction=='W'){
                --j;
                if(i<0 || j<0 || j>Maze[0].size()-1){
                    cout << "No" << endl;
                    return;
                }
                if(i>Maze.size()-1){
                    cout << counter << endl;
                    return;
                }
                continue;

            }
            if(Maze[i][j].direction=='E'){
                ++j;
                if(i<0 || j<0 || j>Maze[0].size()-1){
                    cout << "No" << endl;
                    return;
                }
                if(i>Maze.size()-1){
                    cout << counter << endl;
                    return;
                }
                continue;
            }


        }
    }
    vector<vector<maze> > CreateMaze(ll m, ll n, vector<vector<char> > M){
        vector<vector<maze> > Maze;
        vector<maze> N;
        maze T;
        for(int i=0; i<m; ++i){
            for(int j=0; j<n; ++j){
                T.passed = 0;
                T.direction = M[i][j];
                N.push_back(T);
            }
            Maze.push_back(N);
            N.erase(N.begin(), N.end());
        }
        return Maze;
    }
    void printMaze(vector<vector<maze> > Maze){
        for(int i=0; i<Maze.size(); ++i){
            for(int j=0; j<Maze[i].size(); ++j){
                cout << Maze[i][j].direction << ' ';
            }
            cout << endl;
        }
        cout << endl;
    }
};

/*------------------------------------------------------------------
Problems D:
从文件Score.txt中读取学生信息，对其进行排序，学生信息包括学号不高于20
位，题目数不超过10， 分数， 首先按照回答题数从大往小排，题数一样按照
分数从小往大排。

例
文件内容:
CS00000001 4 110
CS00000002 4 120
CS00000003 5 150

输出
1 CS00000003 5 150
2 CS00000001 4 110
3 CS00000002 4 120
-------------------------------------------------------------------*/
struct Info{
    string ID;
    ll subjects;
    ll scores;
};

class SolutionD{
public:
    void Information_Sort(){
        vector<Info> info = Init_Students_Info();
        QuickSort(0, info.size()-1, info, "subjects");
        ll pre = 0;
        for(int i=1; i<info.size(); ++i){
            if(info[pre].subjects == info[i].subjects) continue;
            if(info[pre].subjects != info[i].subjects){
                QuickSort(pre, i-1, info, "scores");
                pre = i;
            }
        }
        // 将剩下的最后一组排序
        QuickSort(pre, info.size()-1, info, "scores");
        for(int i=0; i<info.size(); ++i){
            cout << info[i].ID << ' ' << info[i].subjects
                << ' ' << info[i].scores <<endl;
        }

    }
    void QuickSort(ll i, ll j, vector<Info> &info, string str){
        if(i<j){
            if(str=="subjects"){
                ll pos = Partition_subjects(i, j, info);
                QuickSort(i, pos-1, info, "subjects");
                QuickSort(pos+1, j, info, "subjects");
            }
            if(str=="scores"){
                ll pos = Partition_scores(i, j, info);
                QuickSort(i, pos-1, info, "scores");
                QuickSort(pos+1, j, info, "scores");
            }
        }
    }

    ll Partition_subjects(ll low, ll high, vector<Info> &info){
        Info k = info[low];
        while(low<high){
            while(low<high&&info[high].subjects<=k.subjects) --high;
            info[low] = info[high];
            while(low<high&&info[low].subjects>k.subjects) ++low;
            info[high] = info[low];
        }
        info[low] = k;
        return low;
    }
    ll Partition_scores(ll low, ll high, vector<Info> &info){
        Info k = info[low];
        while(low<high){
            while(low<high&&info[high].scores>=k.scores) --high;
            info[low] = info[high];
            while(low<high&&info[low].scores<k.scores) ++low;
            info[high] = info[low];
        }
        info[low] = k;
        return low;
    }
    vector<Info> Init_Students_Info(){
        ifstream in("Score.txt");
        string info;
        vector<Info> information;
        Info S;
        while(getline(in, info)){
            ll pos = info.find(' ');
            S.ID.assign(info, 0, pos);
            info.erase(0, pos+1);
            pos = info.find(' ');
            string sub = string(info, 0, pos);
            S.subjects = str2num(sub);
            info.erase(0, pos+1);
            S.scores = str2num(info);
            information.push_back(S);
        }
        return information;

    }
    ll str2num(string str){
        ll sum = 0;
        for(int i=0; i<str.size(); ++i){
            sum = sum*10 + str[i] - '0';
        }
        //cout << sum << endl;
        return sum;
    }
};

bool compare(Info a, Info b){
    return a.subjects > b.subjects;
}

int main(){
//    SolutionA S;
//    S.ProblemsA();

//    SolutionB S;
//    S.ProblemsB();

//    SolutionC S;
//    S.ProblemsC();

    SolutionD S;
//    string str = "12";
    S.Information_Sort();
//    S.str2num(str);
    return 0;
}
