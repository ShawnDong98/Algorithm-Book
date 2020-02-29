/*------------------------------------------------
������ջ��ʵ��һ�����У���ɶ��е�Push��Pop������
�����е�Ԫ��Ϊint���͡�
-------------------------------------------------*/
#include <iostream>
#include <stack>

using namespace std;

class Solution
{
public:
    void push(int node) {
        while(!stack2.empty()){
            stack1.push(stack2.top());
            stack2.pop();
        }
        stack1.push(node);
    }

    int pop() {
        while(!stack1.empty()){
            stack2.push(stack1.top());
            stack1.pop();
        }
        int node = stack2.top();
        stack2.pop();
        return node;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};


int main(){
    Solution S;
    S.push(2);
    int t = S.pop();
    cout << t << endl;
    S.push(3);
    S.push(4);
    cout << S.pop() << endl;
    return 0;
}
