"""
宝宝和妈妈参加亲子游戏, 在一个二维矩阵(N*N)的格子地图上, 宝宝和妈妈抽签决定各自的位置, 地图上每个格子有不同的糖果数量, 部分格子有障碍物。   游戏规则是妈妈必须在最短的时间(每个单位时间只能走一步)到达宝宝的位置, 路上的所有糖果都可以拿走, 不能走障碍物的格子, 只能上下左右走。 请问妈妈在最短到达宝宝位置的时间内最多拿到多少糖果(优先考虑最短时间到达的情况下尽可能多拿糖果)。

输入描述: 
第一行输入为 N, 表示二维矩阵的大小。
接下来有 N 行, 每行有 N 个值, 表示矩阵每个位置的值。
-3: 妈妈的起点。
-2: 宝宝的位置。
-1: 障碍物, 不能通过。
>=0: 表示该位置的糖果数(0 表示没有糖果, 但可以走)。

输出描述: 
输出妈妈在最短时间内到达宝宝位置时, 能够拿到的最多糖果数。

示例输入: 
4
3 2 1 -3
1 -1 1 1
1 1 -1 2
-2 1 2 3

示例输出: 
9
"""
from collections import deque

def bfs(maze):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for x in range(len(maze[0])):
        for y in range(len(maze)):
            if maze[y][x] == "-3":
                start_x, start_y = x, y

    queue = deque([((start_x, start_y), 0)])
    visited = set()
    visited.add((start_x, start_y))

    res = []
    while queue:
        (x, y), candy = queue.popleft()
        if maze[y][x] == "-2":
            res.append(candy)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and (nx, ny) not in visited and maze[ny][nx] != "-1":
                visited.add((nx, ny))
                queue.append(((nx, ny), candy+max(0, int(maze[ny][nx]))))

    
    return max(res)


N = int(input())
maze = []
for i in range(N):
    inp = input().split()
    maze.append(inp)

print(bfs(maze))