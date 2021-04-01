#include <iostream>
#include <vector>
 
typedef long long ll;
 
using namespace std;

class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        if(image.empty() || image[0].empty()) return image;
        int dx[4] = {-1, 0, 1, 0}, dy[4] = {0, 1, 0, -1};
        //---------- 记录下旧的像素值 ------------
        int oldColor = image[sr][sc];
        if (oldColor == newColor) return image;
        //---------- 将新的像素值赋上 ------------
        image[sr][sc] = newColor;
        for (int i = 0; i < 4; ++i) {
            int x = sr + dx[i], y = sc + dy[i];
            if (x >= 0 && x < image.size() && y >=0 && y<image[0].size() && image[x][y] == oldColor)
                floodFill(image, x, y, newColor);
                
        }
        return image;
    }
};



 
int main() {
    vector<vector<int>> image;
    vector<int> row1 = {1, 1, 1};
    vector<int> row2 = {1, 1, 0};
    vector<int> row3 = {1, 0, 1};
    image.push_back(row1);
    image.push_back(row2);
    image.push_back(row3);

    int sr = 1, sc = 1, newColor = 2;

    Solution S;

    vector<vector<int>> newimage = S.floodFill(image, sr, sc, newColor);

    for (int i = 0; i < newimage.size(); ++i) {
        for (int j = 0; j < newimage[0].size(); ++j) {
            cout << newimage[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}