/*---------------------------------------------------
    在一个二维数组中（每个一维数组的长度相同），每一
行都按照从左到右递增的顺序排序，每一列都按照从上到下
递增的顺序排序。请完成一个函数，输入这样的一个二维数
组和一个整数，判断数组中是否含有该整数。

----------------------------------------------------*/
#include <iostream>
#include <vector>

using namespace std;

// 牛客不通过，段错误
// 这道题要求内存空间为32768K
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        for(vector<vector<int> >::iterator it=array.begin();it<array.end();++it)
        {
            if(Binary_Search(target, *it)) return true;
        }
        return false;
    }
    bool Binary_Search(int target, vector<int> a){
        int l = a.front(), r = a.back();
        int mid;
        while(l<=r){
            mid = l + (r - l) / 2;
            if(a[mid] == target) return true;
            if(a[mid] < target){
                l = mid + 1;
            }else{
                r = mid - 1;
            }
        }
        return false;
    }
};

// AC
class Solution_1 {
public:
    bool Find(int target, vector<vector<int> > array) {
        for(vector<vector<int> >::iterator it=array.begin();it<array.end();++it)
        {
            for(int i=0; i<(*it).size(); ++i)
            {
                if(target == (*it)[i]) return true;
            }
        }
        return false;
    }
};

int main(){
    vector<vector<int> > M;
    vector<int> N;

    for(int i=0; i<10; ++i){
        for(int j=0; j<10; ++j){
            N.push_back(j);
        }
        M.push_back(N);
    }

//    for(int i=0; i<10; ++i){
//        for(int j=0; j<10; ++j){
//            cout << M[i][j] << ' ';
//        }
//    }
    Solution_1 S;
    int flag;

    flag = S.Find(5, M);

    cout << flag << endl;

    return 0;
}

