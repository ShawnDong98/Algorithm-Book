#include <iostream>
#include <vector>
#include <math.h>
#include <stdio.h>
#include <string>

using namespace std;

typedef long double ld;

/*--------------------------------------------------
Problems A:
请写一个程序，判断给定整数序列能否构成一个等差数列?

每组数据由两行构成，第一行只有一个整数n（<100），
表示序列长度（该序列中整数的个数），第二行为n个整数，
每个整数的取值区间都为[-32768~32767]，整数之间以空格或
跳格间隔。
---------------------------------------------------*/
class SolutionA{
public:
    bool if_arithmetic_progression(vector<int> A){
        if(A.size()==0) return 0;
        if(A.size()<=2) return 1;
        int pre, cur, min;
        pre = find_min(A);
        cur = find_min(A);
        int error = cur - pre;
        for(int i=0; i<A.size(); ++i){
            pre = cur;
            cur = find_min(A);
            if(error == cur - pre) continue;
            return 0;
        }
        return 1;
    }
    int find_min(vector<int> &A){
        int min = A[0];
        int loc = 0;
        for(int i=1; i<A.size(); ++i){
            if(A[i]<min){
                min = A[i];
                loc = i;
            }
        }
        A.erase(A.begin()+loc, A.begin()+loc+1);
        return min;
    }
};

/*------------------------------------------------------------
Problems B:
判定给定正整数是不是“水仙花数”。“水仙花数”是指一个三位数，
其各位数字的立方和等于该数， 例如153 = 1^3 + 5^3 + 3^3

输入说明：有多组数组，每组数据为一个正整数n(0<n<65536，占一行)，
为0时表示输入结束。

输入说明：对于每一组数据， 输入一个yes或no
（表示该数是否为“水仙花数”）
---------------------------------------------------------------*/
class SolutionB{
public:
    bool if_daffodils_number(int n){
        int hundreds, tens, bits;
        hundreds = n / 100;
        tens = (n % 100) / 10;
        bits = n % 10;
        if(n==(cube(hundreds) + cube(tens) + cube(bits))) return 1;
        return 0;
    }
    int cube(int n){
        return n*n*n;
    }
};

/*------------------------------------------------------------------
Problems C:
Arnold变换是一种常见的图像置乱技术， Arnold变换的定义如下：
对于任意N*N矩阵（所有元素都相同的矩阵除外）， 设i， j为矩阵元素原始
下标，经过Arnold变换后新下标为i', j'， 其满足下式：
i' = (i + j) mod N
j' = (i + 2j) mod N
i, j: 0, 1, 2 ... N-1
Arnold变换具有周期性， 即经过若干次变换后，矩阵回到最初状态， 且周期T
与N的大小有关。 对于任意N>2, TN<=N^2/2， 编写程序输出给定的N（2<N<=10）
对应的周期TN。

输入说明：对输入的每一个N，给出N*N矩阵的Arnold变换的周期T。
------------------------------------------------------------------*/
class SolutionC{
public:
    int Arnold_transform_T(vector<vector<int> > matrix){
        int T = 1;
        printMatrix(matrix);
        vector<vector<int> > M1 = matrix, M2 = Arnold_transform(matrix);
        printMatrix(M2);
        while(!if_matrix_same(M1, M2)){
            ++T;
            M2 = Arnold_transform(M2);
            printMatrix(M2);
        }
        return T;
    }
    vector<vector<int> > Arnold_transform(vector<vector<int> > matrix){
        // 这里定义出一个副本存储变换后的矩阵，注意不要在原矩阵上变换
        vector<vector<int> > M = CreateMatrix(matrix.size());
        for(int i=0; i<matrix.size(); ++i){
            for(int j=0; j<matrix.size(); ++j){
                int ii = (i + j) % matrix.size();
                int jj = (i + 2 * j) % matrix.size();
                M[i][j] = matrix[ii][jj];
            }
        }

        return M;
    }

    bool if_matrix_same(vector<vector<int> > M1, vector<vector<int> > M2){
        for(int i=0; i<M1.size(); ++i){
            for(int j=0; j<M1.size(); ++j){
                if(M1[i][j]!=M2[i][j]) return 0;
            }
        }
        return 1;
    }

    vector<vector<int> > CreateMatrix(int n){
        vector<vector<int> > M;
        int c = 1;
        for(int i=0; i<n; ++i){
            vector<int> N;
            for(int j=0; j<n; ++j){
                N.push_back(c);
                c++;
            }
            M.push_back(N);
        }
        return M;
    }
    void printMatrix(vector<vector<int> > M){
        for(int i=0; i<M.size(); ++i){
            for(int j=0; j<M.size(); ++j){
                cout << M[i][j] << ' ';
            }
            cout << endl;
        }
        cout << endl;
    }
};

/*-------------------------------------------------------
Problems D:
对于一个正整数n，如果它的各位之和等于它的所有质因数的各位
之和， 则该数被称为smith数。
例如：
31527 = 3 * 3 * 23 * 151, 31527的各位之和为3+1+2+5+7=18
它的所有质因数各位之和3+3+2+3+1+5+1=18， 因此，31527是一个
smith数。 编写一个程序判断输入的正整数是不是smith数。

输入说明：有多组数据， 每组数据只有一个整数n(<10000, 占一行),
为0时表示输入结束。

输出说明：对于每一组数据，输出一个yes或no
-------------------------------------------------------*/
class SolutionD{
public:
    bool is_smith(int n){
        vector<int> factor;
        int n_backup = n;
        while(n!=1){
            int i = 2;
            while(i<=n){
                if((is_prime_number(i))&&is_factor(n, i)){
                    factor.push_back(i);
                    // 如果直接遍历，重复的质因数会丢失
                    // 每次除质因数后的结果，再去找质因数
                    n = n / i;
                    break;
                }
                ++i;
            }
        }
        int sum_factor = 0;
        for(int i=0; i<factor.size();++i){
            cout << "factor " << i << ": " << factor[i] << endl;
            sum_factor += bits_sum(factor[i]);
        };
        cout << "sum_factor: " << sum_factor << endl;
        cout << "n_sum: " << bits_sum(n_backup) << endl;
        if(bits_sum(n_backup)==sum_factor) return 1;
        else return 0;
    }
    bool is_prime_number(int n){
        int c = 2;
        while(n%c!=0){
            c++;
        }
        if(c!=n) return 0;
        else return 1;
    }
    bool is_factor(int n, int factor){
        if(n%factor == 0) return 1;
        return 0;
    }
    int bits_sum(int n){
        int bits, tens, hundreds, thousands, ten_thousand;
        ten_thousand = n / 10000;
        thousands = (n % 10000) / 1000;
        hundreds = (n % 1000) / 100;
        tens = (n % 100) / 10;
        bits = n % 10;
        return ten_thousand + thousands + hundreds + tens + bits;
    }
};

/*------------------------------------------------------------------
Problems E:
请写一个程序， 计算R^n精确结果(0.0<R<99.999, n是整数且0<n<=25)

输入说明：有多组数据，每组数据占一行，用一对数据表示， 第一个数据是R
(含小数点6位)， 第二个数据是n， 两个数据之间有一个空格。

输入说明： 对每个 输入 输出其结果（占一行）
-------------------------------------------------------------------*/
class SolutionE{
public:
    vector<int> cal_pow(vector<int> R, int n, int x){
        int temp = 0;
        vector<int> t;
        while(--n){
            temp = 0;
            for(int i=R.size()-1; i>=0; --i){
                temp += R[i] * x;
                t.insert(t.begin(), temp%10);
                temp /= 10;
            }
            while(temp!=0){
                t.insert(t.begin(), temp%10);
                temp /= 10;
            }
            R = t;
            t.erase(t.begin(), t.end());
        }
        return R;
    }
    vector<int> int2vec(int n){
        vector<int> t;
        while(n!=0){
            t.insert(t.begin(), n%10);
            n /= 10;
        }
        return t;
    }
    vector<int> float2vec(ld f){
        ld temp = f - (ld)(int)f;
        vector<int> t;
        while(temp==0){
            temp *= 10;
            t.push_back(int(temp));
            temp = temp - (ld)int(temp);
        }
        return t;
    }
};

int main(){
//    int n = 0, t;
//    vector<int> A;
//    cin >> n;
//    for(int i=0; i<n; ++i){
//        cin >> t;
//        A.push_back(t);
//    }
//    SolutionA S;
//    cout << S.if_arithmetic_progression(A) << endl;

//    int n;
//    SolutionB S;
//    while(cin >> n){
//        if(n==0) return 0;
//        cout << S.if_daffodils_number(n) << endl;
//    }
//    return 0;

//    SolutionC S;
//    vector<vector<int> > M;
//
//    M = S.CreateMatrix(8);
//    cout << S.Arnold_transform_T(M) << endl;


//    SolutionD S;
//    cout << S.is_smith(123) << endl;

//    SolutionE S;
//    cout << S.cal_pow(95.123, 12) << endl;

    vector<int> t, t2, tf;
    SolutionE S;

    t = S.int2vec(95123);

    for(int i=0; i<t.size(); ++i){
        cout << t[i] << " ";
    }
    cout << endl;

    t2 = S.cal_pow(t, 12, 95123);

    for(int i=0; i<t2.size(); ++i){
        cout << t2[i] << " ";
    }
    cout << endl;

    ld n;
    string str;
    //scanf("%f", &n);
    cin >> n;
    str = to_string(n);
    cout << str[0] << endl;
//    tf = S.float2vec(n);
//
//    for(int i=0; i<tf.size(); ++i){
//        cout << tf[i] << " ";
//    }
//    cout << endl;

}
