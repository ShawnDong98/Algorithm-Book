/*----------------------------------------------------------
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
----------------------------------------------------------*/

#include <iostream>
#include <stdlib.h>

using namespace std;

struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};

class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        ListNode *p1 = pHead1, *p2 = pHead2;
        ListNode *H = (ListNode*)malloc(sizeof(ListNode));
        //H->next = NULL;
        ListNode *p = H;
        while(p1!=NULL && p2!=NULL){
            if(p1->val>p2->val){
                p->next = p2;
                p = p2;
                p2 = p2->next;
            }else{
                p->next = p1;
                p = p1;
                p1 = p1->next;
            }
        }
        if(p1!=NULL) p->next = p1;
        if(p2!=NULL) p->next = p2;
        p = H->next;
        delete H;
        return p;
    }
    void CreateLinkList(ListNode* &L, int n){
        ListNode* p = (ListNode*)malloc(sizeof(ListNode));
        p->val = 1;
        p->next = NULL;
        L = p;
        for(int i=n; i>1; --i){
            p = (ListNode*)malloc(sizeof(ListNode));
            p->next = L->next;
            p->val = i;
            L->next = p;
        }
        if(n==0) L = NULL;
    }
    void printLinkList(ListNode* L){
        ListNode* p = L;
        while(p!=NULL){
            cout << p->val << ' ';
            p = p->next;
        }
        cout << endl;
    }
};

int main(){
    ListNode *L1, *L2, *L;
    Solution S;
    S.CreateLinkList(L1, 0);
    S.CreateLinkList(L2, 0);

    L = S.Merge(L1, L2);
    S.printLinkList(L);
    return 0;
}
