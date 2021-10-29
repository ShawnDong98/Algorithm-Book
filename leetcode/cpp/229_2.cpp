#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

// 计算各个为1的点离j的距离的绝对值之和
class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector<int> res(boxes.size());
        for (int i = 0; i < boxes.size(); ++i) {
            res[i] = 0;
            for (int j = 0; j < boxes.size(); ++j) {
                if(boxes[j] == '1') {
                    res[i] += abs(j - i);
                }
            }
        }
        return res;

    }
};
 
int main() {
    // string boxes = "110";

     string boxes = "001011";

    Solution S;

    vector<int> res = S.minOperations(boxes);

    for(auto x: res) {
        cout << x << endl;
    }

    
    return 0;
}