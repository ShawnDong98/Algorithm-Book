#include <iostream>
#include <vector>
#include <algorithm>
 

 
using namespace std;

bool compare(int a, int b) {
    return a > b ? true : false;
}

class Solution {

typedef long long ll;

public:
    
    int maximumScore(int a, int b, int c) {
        ll score = 0;
        vector<int> v(3);
        v[0] = a;
        v[1] = b;
        v[2] = c;

        int res = 0;

        sort(v.begin(), v.end(), compare);

        while(true){
            if (v[0]==0 || v[1]==0) return res;
            v[0]--;
            v[1]--;
            res++;
            sort(v.begin(), v.end(), compare);
        }
        return res;
    }

};
 
int main() {
    // int a = 2;
    // int b = 4;
    // int c = 6;

    // int a = 4;
    // int b = 4;
    // int c = 6;

    int a = 1;
    int b = 8;
    int c = 8;

    Solution S;

    cout << S.maximumScore(a, b, c) << endl;
    
    return 0;
}