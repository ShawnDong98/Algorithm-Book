"""
小华按照地图去寻宝, 地图上被划分成m行和n列的方格, 横纵坐标范围分别是[0, n-1]和[0, m-1]。在横坐标和纵坐标的数位之和不大于k的方格中存在黄金(每个方格中仅存在一克黄金), 但横坐标和纵坐标之和大于k的方格存在危险不可进入。小华从入口(0,0)进入, 任何时候只能向左, 右, 上, 下四个方向移动一格。请问小华最多能获得多少克黄金？

输入描述

坐标取值范围如下:

0<=m<=50

0<=n<=50

k的取值范围如下:

0<=k<=100

输入中包含3个字数, 分别是m, n, k

输出描述

最多能获得多少克黄金

示例1
输入输出示例仅供调试, 后台判题数据一般不包含示例

输入

40 40 18

输出

1484

说明

当k为18时, 小华能够进入方格(10,10), 因为1+0+1+0 = 2。 但是, 他不能进入方格(36,38), 因为3+6+3+8 = 20

示例2
输入输出示例仅供调试, 后台判题数据一般不包含示例

输入

4 5 7

输出

20

说明

如图每个单元格中的数位之和均不大于7, 都是符合要求的, 所以可以最多可获得20克黄金
"""

from collections import deque

def can_enter(x, y, k):
    sum_x = sum([int(i) for i in str(x)])
    sum_y = sum([int(j) for j in str(y)])

    return sum_x + sum_y <= k
        
    
def find_gold(m, n, k):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))

    gold = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and (nx, ny) not in visited and can_enter(nx, ny, k):
                gold += 1
                visited.add((nx, ny))
                queue.append((nx, ny))

    return gold


m, n, k = map(int, input().split())
print(find_gold(m, n, k))


