#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;
 
using namespace std;


/*
用堆(优先级队列)取维护一个我们可以吃的苹果和它的过期日期(date, apple)

每次从最早过期(date)的苹果(apple)中吃一个
*/
class Solution {
public:
    int eatenApples(vector<int>& apples, vector<int>& days) {
            typedef pair<int, int> PII;
            priority_queue<PII, vector<PII>, greater<PII>> heap;
            int ret = 0;
            int n = apples.size();
            for(int i = 0; i <= 40000; ++i) {
                if (i < n && apples[i] > 0) {
                    // 入队
                    heap.push({i + days[i] - 1, apples[i]});
                }
                // 如果队列不空 并且 过期日期 比 i 小， 也就是说已经过期， 出队
                while (heap.size() && heap.top().first < i) heap.pop();
                // 队列空了， 也就是当天产的以及之前产的苹果吃完了或过期了
                if(heap.empty()) continue;
                // 将队头取出
                auto t = heap.top();
                // 队头出队
                heap.pop();
                // 吃的苹果加一
                ret++;
                // 将队头的苹果数减一再入队
                if (--t.second) heap.push(t);
            }
            return ret;
    }
};


 
int main(){
    // vector<int> apples = {1,2,3,5,2};
    // vector<int> days = {3,2,1,4,2};

    vector<int> apples = {3,0,0,0,0,2};
    vector<int> days = {3,0,0,0,0,2};

    Solution S;

    cout << S.eatenApples(apples, days) << endl;

    return 0;
}