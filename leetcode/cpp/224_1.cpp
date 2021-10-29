#include <iostream>
#include <vector>
#include <algorithm>

 
typedef long long ll;
 
using namespace std;

/*
首先找出可切的最大正方形边长maxlen，一个vector存储各组可切的正方形边长， 找最大值

然后找有几组可以切maxlen大小的正方形
*/
class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        vector<int> R;
        int maxlen = 0, t = 0;
        int num = 0;
        for (int i = 0; i < rectangles.size(); ++i) {
            // cout << find_min(rectangles[i]) << endl;
            t = find_min(rectangles[i]);
            if(t > maxlen) maxlen = t; 
            R.push_back(t);
        }
        num = count(R.begin(), R.end(), maxlen);
        return num;
    }
    int find_min(vector<int> rectangle) {
        return rectangle[0]<rectangle[1] ? rectangle[0] : rectangle[1];
    }
};

class Solution_ {
public:
    int countGoodRectangles(vector<vector<int>>& r) {
        int maxlen = 0;
        for (auto& t: r) maxlen = max(min(t[0], t[1]), maxlen);
        int res = 0;
        for (auto& t: r){
            if (t[0] >= maxlen && t[1] >= maxlen) res ++;
        }
        return res;
    }
};
 
int main() {
    vector<int> R1 = {5, 8};
    vector<int> R2 = {3, 9};
    vector<int> R3 = {5, 12};
    vector<int> R4 = {16, 5};
    vector<vector<int>> rectangles;

    rectangles.push_back(R1);
    rectangles.push_back(R2);
    rectangles.push_back(R3);
    rectangles.push_back(R4);

    // vector<int> R1 = {2, 3};
    // vector<int> R2 = {3, 7};
    // vector<int> R3 = {4, 3};
    // vector<int> R4 = {3, 7};
    // vector<vector<int>> rectangles;

    // rectangles.push_back(R1);
    // rectangles.push_back(R2);
    // rectangles.push_back(R3);
    // rectangles.push_back(R4);

    Solution_ S;

    cout << S.countGoodRectangles(rectangles) << endl;
    

    return 0;
}