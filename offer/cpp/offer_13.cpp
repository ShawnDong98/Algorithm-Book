/*---------------------------------------------------------
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
---------------------------------------------------------*/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void reOrderArray(vector<int> &array) {
        if(array.size()==0) return;
        int i = 0, j, tmp;
        //找到第一个偶元素
        while(array[i]%2!=0) ++i;
        j = i+1;
        while(j<array.size()){
            //找到i之后的第一个奇元素
            while(array[j]%2==0) ++j;
            if(j>=array.size()) break;
            tmp = array[j];
            // i到j之间的偶元素后移一位
            for(int k=j; k>i; --k){
                array[k] = array[k-1];
            }
            array[i] = tmp;
            ++i;
            j = i+1;
        }

    }

    void reOrderArray_1(vector<int> &array) {
        vector<int> tmp;
        for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it){
            if(*it%2==1){
                tmp.push_back(*it);
            }
        }
        for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it){
            if(*it%2==0){
                tmp.push_back(*it);
            }
        }
        array.swap(tmp);
    }
};

int main(){
    //int a[10] = {1, 3, 5, 6, 7, 8, 10, 11};
    vector<int> array;

    Solution S;

    S.reOrderArray(array);

    for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it){
        cout << *it << ' ';
    }

    return 0;
}
