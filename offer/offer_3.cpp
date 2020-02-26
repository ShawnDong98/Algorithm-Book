/*--------------------------------------------------
����һ�������������β��ͷ��˳�򷵻�һ��ArrayList��
---------------------------------------------------*/

#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

typedef struct ListNode {
    int val;
    struct ListNode *next;
    ListNode(int x) :
          val(x), next(NULL) {

    }
}ListNode, *LinkList;



class Solution {
public:
    // �����ԣ�����Ϊ����ͷ�ڵ�ĵ�����
    // ������ʹ��ͷ�巨���ã��ٽ�val˳�����vector
    vector<int> printListFromTailToHead(ListNode* head) {

        vector<int> buffer;
        if(!head) return buffer;

        ListNode* H = (ListNode*)malloc(sizeof(ListNode));
        H->next = head;
        ListNode* p = H->next;
        ListNode* r;

        H->next = NULL;
        while(p){
            r = p->next;
            p->next = H->next;
            H->next = p;
            p = r;

        }
        p = H->next;
        while(p){
            buffer.push_back(p->val);
            p = p->next;
        }
        delete H;
        return buffer;

    }

    void CreateLinkList(ListNode* &L, int n){
        ListNode* H = (ListNode*)malloc(sizeof(ListNode));
        H->next = NULL;
        ListNode *p;
        for(int i=0; i<n; ++i){
            p = (ListNode*)malloc(sizeof(ListNode));
            p->next = H->next;
            p->val = i;
            H->next = p;
        }
        L = H->next;
    }

    void printList(ListNode* &L){
        ListNode *p = L;
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
    vector<int> buffer;
    S.CreateLinkList(L, 10);
    //cout << L->next->val << endl;
    S.printList(L);
    buffer = S.printListFromTailToHead(L);
    for(int i=0; i<buffer.size(); ++i){
        cout << buffer[i] << ' ';
    }
    return 0;
}
