"""
围棋棋盘由纵横各19条线垂直相交组成, 棋盘上一共19x19=361个交点, 对弈双方一方执白棋, 一方执黑棋, 落子时只能将棋子置于交点上。

“气”是围棋中很重要的一个概念, 某个棋子有几口气, 是指其上下左右方向四个相邻的交叉点中, 有几个交叉点没有棋子, 由此可知：

1. 在棋盘的边缘上的棋子最多有3口气, 在棋盘角点的棋子最多有2口气, 其它情况最多有4口气。
2. 所有同色棋子的气之和叫作该色棋子的气, 需要注意的是, 同色棋子重合的气点, 对于该颜色棋子来说, 只能计算一次气, 比如下图中, 黑棋一共4口气, 而不是5口气, 因为黑1和黑2中间红色三角标出的气是两个黑棋共有的, 对于黑棋整体来说只能算一个气。
3. 本题目只计算气, 对于眼也按气计算, 如果您不清楚“眼”的概念, 可忽略, 按照前面描述的规则计算即可。

现在, 请根据输入的黑棋和白棋的坐标位置, 计算黑棋和白棋一共各有多少气？

输入描述
输入包含两行数据, 

每行数据以空格分隔, 数据个数是2的整数倍, 每两个数是一组, 代表棋子在棋盘上的坐标； 坐标的原点在棋盘左上角点, 第一个值是行号, 范围从0到18; 第二个值是列号, 范围从0到18。

举例说明：如：

0 5 8 9 9 10

5 0 9 9 9 8

第一行数据表示三个坐标(0, 5)、(8, 9)、(9, 10) 第一行表示黑棋的坐标, 第二行表示白棋的坐标。 题目保证输入两行数据, 无空行且每行按前文要求是偶数个, 每个坐标不会超出棋盘范围。

输出描述
两个数字以空格分隔, 第一个数代表黑棋的气数, 第二个数代表白棋的气数。

8 7

用例
输入

0 5 8 9 9 10
5 0 9 9 9 8
输出

8 7
说明

数数黑棋一共8口气, 数数白棋一共7口气。
"""

def count_air(board, stones):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    air = 0

    for x, y in stones:
         for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == 0 and (nx, ny) not in visited:
                air += 1
                visited.add((nx, ny))

    return air


board = [[0] * 19 for _ in range(19)]

black_coords = list(map(int, input().split()))

black_stones = []

white_coords = list(map(int, input().split()))

white_stones = []

for i in range(0, len(black_coords), 2):
    x, y = black_coords[i], black_coords[i+1]
    board[x][y] = 1
    black_stones.append((x, y))

for i in range(0, len(white_coords), 2):
    x, y = white_coords[i], white_coords[i+1]
    board[x][y] = 2
    white_stones.append((x, y))

print(count_air(board, black_stones))
print(count_air(board, white_stones))
