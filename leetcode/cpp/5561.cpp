#include <iostream>
#include <vector>
#include <algorithm>
 
typedef long long ll;
 
using namespace std;


class Solution {
public:
    int getMaximumGenerated(int n) {
        vector<int> num;
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        if(n>=2){
            num.push_back(0);
            num.push_back(1);
            for(int i=2; i<(n+1); ++i){
                if(i%2==0){
                    num.push_back(num[i/2]);
                }
                else{
                    num.push_back(num[(i-1)/2] + num[(i-1)/2 + 1]);
                }
            }
            // for(int i=0; i<num.size(); ++i){
            //     cout << num[i] << endl;
            // }

            sort(num.begin(), num.end());
            // cout << num[num.size()-1] << endl;
            return num[num.size()-1];
        }
        return -1;
    }
};
 
int main(){
    
    Solution S;

    cout << S.getMaximumGenerated(0) << endl;
    
    return 0;
}