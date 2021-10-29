#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;


/*
利用性质：

a ^ b = c
b = c ^ a
*/
class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        vector<int> arr;
        int temp = 0;
        arr.push_back(first);
        for (int i = 1; i <= encoded.size(); ++i) {
            temp = encoded[i-1] ^ arr[i-1];
            arr.push_back(temp);
        }
        // for (auto i: arr) {
        //     cout << i <<endl;
        // }

        return arr;
    }
};
 
int main() {
    // vector<int> encoded = {1,2,3};
    // int first = 1;

    vector<int> encoded = {6,2,7,3};
    int first = 4;

    Solution S;

    S.decode(encoded, first);
    
    return 0;
}