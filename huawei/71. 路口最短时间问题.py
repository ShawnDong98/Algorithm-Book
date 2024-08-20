"""
假定街道是棋盘型的, 每格距离相等, 车辆通过每格街道需要时间均为 timePerRoad; 街道的街口(交叉点)有交通灯, 灯的周期T(=lights[row][col])各不相同; 车辆可直行、左转和右转, 其中直行和左转需要等相应 T 时间的交通灯才可通行, 右转无需等待。现给出 n*m 个街口的交通灯周期, 以及起止街口的坐标, 计算车辆经过两个街口的最短时间。
其中：
1)起点和终点的交通灯不计入时间, 且可以任意方向经过街口
2)不可超出 n*m 个街口, 不可跳跃, 但边线也是道路(即 lights[0][0] -> lights[0][1] 是有效路径)

入口函数定义:
/**
 * lights : n*m 个街口每个交通灯的周期，值范围[0,120], n和m的范围为[1,9]
 * timePerRoad : 相邻两个街口之间街道的通过时间,范围为[0,600]
 * rowStart : 起点的行号
 * colStart : 起点的列号
 * rowEnd : 终点的行号
 * colEnd : 终点的列号
 * return : lights[rowStart][colStart] 与 lights[rowEnd][colEnd] 两个街口之间的最短通行时间
 */
int calcTime(int[][] lights, int timePerRoad, int rowStart, int colStart, int rowEnd, int colEnd)

"""

from collections import deque

def min_time_to_reach(n, m, lights, start, end, time_per_riad):
    min_time = [[float("inf")] * m for _ in range(n)]
    min_time[start[0]][start[1]] = 0

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    queue = deque([((start[0], start[1]), 0)])
    visited = set()
    visited.add((start[0], start[1]))

    res = []

    while queue:
        (x, y), current_time = queue.popleft()

        if (x, y) == end:
            res.append(current_time)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if x


    if not res:
        return float("inf")
    else:
        return min(res)
        


n = 3
m = 3
lights = [
    [3, 4, 5],
    [2, 3, 4],
    [1, 2, 3]
]

start = (0, 0)
end = (2, 2)
time_per_road = 1

# 计算最短时间
result = min_time_to_reach(n, m, lights, start, end, time_per_road)
print(result)