#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;


// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class LinkList {
public:
    ListNode* Structor(vector<int> a) {
        ListNode* head = new ListNode(a[0]);
        ListNode* p = head;
        for (int i = 1; i < a.size(); ++i) {
            ListNode* temp = new ListNode(a[i]);
            p->next = temp;
            p = temp;
        }
        p->next = nullptr; 

        return head;
    }
};


// 考试做法
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        vector<int> a;
        for (auto p = head; p; p = p->next) a.push_back(p->val);
        swap(a[k-1], a[a.size() - k]);
        head = new ListNode(a[0]);
        auto cur = head;
        for (int i = 1; i < a.size(); ++i) {
            cur = cur->next = new ListNode(a[i]);
        }
        return head;
    }
};


// 面试做法
// 找到目标位置的前一节点 将前一节点指向目标节点的指针 以及 目标节点指向下一节点的指针 交换 
class Solution_ {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        auto dummy = new ListNode(-1);
        dummy->next = head;
        int n = 0;
        for (auto p = dummy; p; p= p->next) n ++;
        k ++;
        auto a = dummy;
        for (int i = 0; i < k-2; ++i) a = a->next;
        auto b = dummy;
        for (int i = 0; i < n-k; ++i) b = b->next;

        if(a == b) return dummy->next;

        auto pa = a->next, qa = pa->next;
        auto pb = b->next, qb = pb->next;
        if (a->next == b) {
           a->next = qa, qa->next = pa;
           pa->next = qb;
           return dummy->next;
        }else if (b->next == a) {
            b -> next = qb, qb ->next = pb;
            pb -> next = qa;
            return dummy->next;
        }

        pa->next = qb, b->next = pa;
        pb->next = qa, a->next = pb;
        
        return dummy->next;
    }


};



 
int main() {
    // vector<int> a = {1, 2, 3, 4, 5};
    // int k = 2;
    // LinkList L;
    // ListNode* l =  L.Structor(a);

    // vector<int> a = {7,9,6,6,7,8,3,0,9,5};
    // int k = 5;
    // LinkList L;
    // ListNode* l =  L.Structor(a);

    // vector<int> a = {1};
    // int k = 1;
    // LinkList L;
    // ListNode* l =  L.Structor(a);

    vector<int> a = {1,2};
    int k = 1;
    LinkList L;
    ListNode* l =  L.Structor(a);

    Solution_ S;

    // Solution S;
    

    l = S.swapNodes(l, k);

    for (auto p=l; p; p=p->next) {
        cout << p->val << endl; 
    }




    return 0;
}