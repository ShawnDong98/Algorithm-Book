"""
疫情期间, 小明隔离在家, 百无聊赖, 在纸上写数字玩。他发明了一种写法: 给出数字个数n和行数m(0 < n ≤ 999, 0 < m ≤ 999), 从左上角的1开始, 按照顺时针螺旋向内写方式, 依次写出2,3...n, 最终形成一个m行矩阵。小明对这个矩阵有些要求: 

1. 每行数字的个数一样多
2. 列的数量尽可能少
3. 填充数字时优先填充外部
4. 数字不够时, 使用单个*号占位

用例1
输入
9 4

输出
1 2 3
* * 4
9 * 5
8 7 6

用例2
输入
3 5

输出
1
2
3
*
*
"""
import math

def generate_spiral_matrix(n, m):
    cols =  math.ceil(n / m)
    matrix = [[None] * cols for _ in range(m)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    direction_index = 0

    row, col = 0, 0

    for num in range(1, n + 1):
        matrix[row][col] = num
        next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]

        if not (0 <= next_row < m and 0 <= next_col < cols and matrix[next_row][next_col] is None):
            direction_index = (direction_index + 1) % 4
            next_row, next_col = row + directions[direction_index][0], col + directions[direction_index][1]

        row, col = next_row, next_col


    for i in range(m):
        for j in range(cols):
            if matrix[i][j] is None:
                matrix[i][j] = "*"
    
    for row in matrix:
        print(" ".join(str(cell) for cell in row))




n, m = map(int, input().split())
generate_spiral_matrix(n, m)
