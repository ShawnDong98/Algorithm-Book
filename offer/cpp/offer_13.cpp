/*---------------------------------------------------------
����һ���������飬ʵ��һ�����������������������ֵ�˳��
ʹ�����е�����λ�������ǰ�벿�֣����е�ż��λ������ĺ�벿�֣�
����֤������������ż����ż��֮������λ�ò��䡣
---------------------------------------------------------*/
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void reOrderArray(vector<int> &array) {
        if(array.size()==0) return;
        int i = 0, j, tmp;
        //�ҵ���һ��żԪ��
        while(array[i]%2!=0) ++i;
        j = i+1;
        while(j<array.size()){
            //�ҵ�i֮��ĵ�һ����Ԫ��
            while(array[j]%2==0) ++j;
            if(j>=array.size()) break;
            tmp = array[j];
            // i��j֮���żԪ�غ���һλ
            for(int k=j; k>i; --k){
                array[k] = array[k-1];
            }
            array[i] = tmp;
            ++i;
            j = i+1;
        }

    }

    void reOrderArray_1(vector<int> &array) {
        vector<int> tmp;
        for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it){
            if(*it%2==1){
                tmp.push_back(*it);
            }
        }
        for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it){
            if(*it%2==0){
                tmp.push_back(*it);
            }
        }
        array.swap(tmp);
    }
};

int main(){
    //int a[10] = {1, 3, 5, 6, 7, 8, 10, 11};
    vector<int> array;

    Solution S;

    S.reOrderArray(array);

    for(vector<int>::iterator it=array.begin(); it!=array.end(); ++it){
        cout << *it << ' ';
    }

    return 0;
}
