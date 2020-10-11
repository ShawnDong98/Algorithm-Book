#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

/*
先看数组长度
flag 表示当前测试的特征值
counter计数 当前数组中大于等于当前测试特征值的个数
从高往低遍历看是否有符合条件的
*/
class Solution{
public:
    int specialArray(vector<int>& nums) {
        int counter=0;
        for(int flag=nums.size(); flag>=0; --flag){
            counter = 0;
            // cout << "flag: " << flag << endl;
            for(int j=0; j<nums.size(); ++j){
                if(nums[j]>=flag) counter++;
            }
            if(counter==flag) return flag;
        }
        return -1;
    }
};
 
int main(){
    // int b[2] = {3, 5};
    // vector<int> a(b, b+2);

    // int b[2] = {0,0};
    // vector<int> a(b, b+2);

    // int b[5] = {0,4,3,0,4};
    // vector<int> a(b, b+5);

    int b[5] = {3,6,7,7,0};
    vector<int> a(b, b+5);

    Solution S;
    cout << S.specialArray(a) << endl;
    system("pause");
    return 0;
}