#include <iostream>
#include <queue>
 
typedef long long ll;
 
using namespace std;

class MyStack {
public:
    queue<int> q;
    /** Initialize your data structure here. */
    MyStack() {

    }
    
    /** Push element x onto stack. */
    // 
    void push(int x) {
        int n = q.size();
        q.push(x);
        for(int i=0; i<n; ++i){
            q.push(q.front());
            q.pop();
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    // 弹出栈顶元素， 也就是弹出队列头部元素
    int pop() {
        int r = q.front();
        q.pop();
        return r;
    }
    
    /** Get the top element. */
    // 返回栈顶元素， 即返回队列头部元素
    int top() {
        int r = q.front();
        return r;
    }
    
    /** Returns whether the stack is empty. */
    // 判断栈是否为空， 也就是判断队列是否为空
    bool empty() {
        return q.empty();
    }
};

 
int main(){
    MyStack S;

    for(int i=0; i<10; ++i){
        S.push(i);
    }
    for(int i=0; i<10; ++i){
        cout << S.pop() << endl;

    }
    
    return 0;
}