#include <iostream>
#include <vector>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        // 箱子容量从大到小排序， 类似于计算智能中的背包问题
        sort(boxTypes.begin(), boxTypes.end(), [](const auto& L, const auto& R){return L[1] > R[1];});
        int ans=0, n=0;
        for(int i=0; i<boxTypes.size() && truckSize>0; ++i){
            // 要取的箱子数， 如果最大容量的箱子数比可以装载箱子的最大数量小， 那么将最大容量的箱子全部取出
            // 如果最大容量的箱子数比可以装载箱子的最大数量大， 那么就只取最大容量的箱子就够了
            n = min(truckSize, boxTypes[i][0]);
            truckSize -= n;
            ans += n * boxTypes[i][1];
        }
        return ans;
    }
};
 
int main(){
    vector<vector<int>> boxTypes;

    // vector<int> a = {1, 3}, b = {2, 2}, c = {3, 1};

    // boxTypes.push_back(a);
    // boxTypes.push_back(b);
    // boxTypes.push_back(c);

    vector<int> a = {5, 10}, b = {2, 5}, c = {4, 7}, d = {3, 9};

    boxTypes.push_back(a);
    boxTypes.push_back(b);
    boxTypes.push_back(c);
    boxTypes.push_back(d);


    Solution S;
    
    cout << S.maximumUnits(boxTypes, 10) << endl;
    
    return 0;
}