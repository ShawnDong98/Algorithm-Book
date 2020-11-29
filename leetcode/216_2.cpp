#include <iostream>
#include <string>


typedef long long ll;
 
using namespace std;

/*
贪心算法：

要构造出的字符串字典序最小， 考虑贪心地从字符串开头开始构造， 每次选择一个满足要求的最小的字母。

假设我们当前构造到了某一个位置，此位置还剩下n'个位置没有放入字符， 并且这些位置的数值之和为k'， 如果我们放入字母c， 那么剩余n'-1个位置以及k'-c的数值之和， 必须满足 n'-1 <= k'-c <= 26(n' - 1)

n是剩余的字母个数， k为它们之和， 也就是说，取完这个字母之后， k-c需要满足的条件是大于等于剩下的字母全选a， 小于等于剩下的字母全选z。

化简得： k' - 26(n' - 1) <= c <= k' - (n' - 1)

那么得到c的取值下限 k' - 26(n' - 1)。 因此：

如果 k' - 26(n' - 1) <= 0， 我们选择字符a
如果 k' - 26(n' - 1) > 0， 我们选择该数值对应的字符
*/
class Solution {
public:
    string getSmallestString(int n, int k) {
        string ans;
        for(int rest=n; rest >= 1; --rest){
            int bound = k - 26 * (rest - 1);
            if(bound > 0){
                ans += char(bound + 'a' - 1);
                k -= bound;
            }
            else{
                ans += 'a';
                k -= 1;
            }
        }
        return ans;
    }
};
 
int main(){
    int n = 3, k=27;

    Solution S;

    cout << S.getSmallestString(n, k) <<endl;


    return 0;
}