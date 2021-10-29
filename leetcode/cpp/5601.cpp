#include <iostream>
#include <vector>
#include <string>
 
typedef long long ll;
 
using namespace std;

class OrderedStream {
public:
    vector<string> os;
    int ptr = 1;
    OrderedStream(int n) {
        for(int i=0; i<n+2; ++i){
            os.push_back("NULL");
        }
        // for(int i=0; i<n; ++i){
        //     cout << os[i] << endl;
        // }
    }
    
    vector<string> insert(int id, string value) {
        vector<string> strlist;
        if(id!=ptr){
            // cout << "id!=ptr: " << ptr << endl;
            // cout << "1" << endl;
            os[id] = value;
            return strlist;
        }
        else
        {
            os[id] = value;
            // cout << os[id] << endl;
            while(os[id]!="NULL"){
                strlist.push_back(os[id]);
                id++;
                ptr++;
            }
            // cout << "2" << endl;
            // for(int i=0; i<strlist.size(); ++i){
            //     cout << strlist[i] << endl;
            // }
            // cout << ptr << endl;
            return strlist;
        }

    }
};


 
int main(){
    OrderedStream S(5);

    vector<string> temp;
    
    S.insert(3, "ccccc");
    S.insert(1, "aaaaa");
    S.insert(2, "bbbbb");
    S.insert(5, "eeeee");
    temp = S.insert(4, "ddddd");

    for(int i=0; i<temp.size(); ++i){
        cout << temp[i] << endl;
    }
    return 0;
}