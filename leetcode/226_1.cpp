#include <iostream>
#include <vector>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    int num2sum(int num) {
        int sum = 0;
        while (num) {
            // cout << "in..." << endl;
            sum += num % 10;
            num = num / 10;
        }
        return sum;
    }
    int countBalls(int lowLimit, int highLimit) {
        vector<int> hash_map(50);
        int sum = 0;
        for (int i = lowLimit; i <=highLimit; ++i) {
            sum = num2sum(i);
            // cout << "sum: " << sum << endl;
            hash_map[sum] += 1;
        }
        // for (auto x : hash_map) { cout << x << endl; }
        sort(hash_map.begin(), hash_map.end());
        // cout << hash_map[49] << endl;
        return hash_map[49];
    }

};
 
int main() {
    // int lowLimit = 1, highLimit = 10;

    int lowLimit = 5, highLimit = 15;

    Solution S;

    cout << S.countBalls(lowLimit, highLimit) << endl;
    return 0;
}