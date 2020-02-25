/*---------------------------------------------------
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为
We%20Are%20Happy。
----------------------------------------------------*/
#include <iostream>
#include <string>
#include <stdlib.h>

using namespace std;

class Solution {
public:
	void replaceSpace(char *str,int length) {
	    for(int i=0; i<length; ++i){
            if(str[i] == ' '){
                houyi(str, length, i);
                length += 2;
                str[i] = '%';
                str[i+1] = '2';
                str[i+2] = '0';
            }
	    }

	}
	void houyi(char *str, int length, int pos){
	    char *p1, *p2;
	    length += 2;
	    p1 = str + length - 1;
	    p2 = str + length - 3;
	    for(int i=pos+3; i<length; ++i){
            *p1 = *p2;
            --p2;
            --p1;
	    }

	}
};



int main(){
    char str[20] = "We Are Happy";
    Solution S;
    S.replaceSpace(str, 12);
    cout << str << endl;

    return 0;
}
