/*------------------------------------------------
����һ��������ת��������������ı�ͷ��
-------------------------------------------------*/
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
    // ͷ�巨
    ListNode* ReverseList(ListNode* pHead){
        if(pHead==NULL) return NULL;
        if(pHead->next==NULL) return pHead;
        ListNode *p = pHead, *r = pHead->next;
        ListNode* H = (ListNode*)malloc(sizeof(ListNode));
        H->next = NULL;
        while(r!=NULL){
            r = p->next;
            p->next = H->next;
            H->next = p;
            p = r;

        }
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
    ListNode* L;
    Solution S;
    S.CreateLinkList(L, 1);
    S.printLinkList(L);

    L = S.ReverseList(L);
    S.printLinkList(L);
    return 0;
}
