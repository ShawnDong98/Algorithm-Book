/*--------------------------------------
输入一个链表，输出该链表中倒数第k个结点。
---------------------------------------*/
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
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        if(pListHead==NULL) return NULL;
        if(k<=0) return NULL;
        ListNode* p = pListHead;
        int length = 0;
        while(p!=NULL){
            length++;
            p = p->next;
        }
        if(k>length) return NULL;
        p = pListHead;
        for(int i=0; i<length-k; ++i){
            p = p->next;
        }
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
    ListNode* T;
    Solution S;
    S.CreateLinkList(L, 10);
    S.printLinkList(L);
    T = S.FindKthToTail(L, 11);
    cout << T->val << endl;
    return 0;
}
