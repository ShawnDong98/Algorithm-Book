/*-----------------------------------------------------------
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
-----------------------------------------------------------*/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        if(rotateArray.size() == 0) return 0;
        int m = find_min(rotateArray);
        for(int i=0; i<m; ++i){
            rotateArray.push_back(rotateArray[i]);
        }
        rotateArray.erase(rotateArray.begin(), rotateArray.begin()+m);
        return rotateArray[0];

    }
    int find_min(vector<int> rotateArray){
        int m = 0;
        for(int i=0; i<rotateArray.size();++i){
            if(rotateArray[i]<rotateArray[m]){
                m = i;
            }
        }
        return m;
    }
    void print(vector<int> A){
        for(vector<int>::iterator it=A.begin();it!=A.end();++it){
            cout << *it << ' ';
        }
        cout << endl;
    }
};

int main(){
    int a[10] = {6, 7, 8, 9, 10, 1, 2, 3, 4, 5};
    vector<int> A(a, a+10);

    Solution S;
    S.minNumberInRotateArray(A);
    S.print(A);
//    for(vector<int>::iterator it=A.begin();it!=A.end();++it){
//        cout << *it << ' ';
//    }
//    cout << endl;
//
//    A.push_back(A[0]);
//
//    A.erase(A.begin(), A.begin()+1);
//
//    for(vector<int>::iterator it=A.begin();it!=A.end();++it){
//        cout << *it << ' ';
//    }
//    cout << endl;

    return 0;
}
