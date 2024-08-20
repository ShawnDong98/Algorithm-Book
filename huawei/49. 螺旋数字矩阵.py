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

def func(matrix, n):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row = 0
    col = 0
    direction_idx = 0

    for i in range(1, n+1):
        matrix[row][col] = i
        next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]

        if not (0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] == "*"):
            direction_idx += 1
            next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]

        row, col = next_row, next_col

    return matrix



n, m = list(map(int, input().split()))

cols = n // m + 1

matrix = [["*"] * cols for _ in range(m)]

matrix = func(matrix, n)

for row in matrix:
    print(" ".join(map(str, row)))
