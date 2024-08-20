"""
题目： 在一个 m x n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0)。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格，直到到达棋盘的右下角。给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？

def maxValueOfGiftsBFS(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])

    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    queue = deque([(0, 0, grid[0][0])])
    directions = [(0, 1), (1, 0)]

    while queue:
        x, y, value = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                new_value = value + grid[nx][ny]

                if new_value > dp[nx][ny]:
                    dp[nx][ny] = new_value

                    queue.append((nx, ny, new_value))

    return dp[m-1][n-1]
    
"""
from collections import deque

def func(maze):
    directions = [(0, 1), (1, 0)]
    queue = deque([((0, 0), maze[0][0])])
    visited = set()
    # visited.add((0, 0))

    res = []
    while queue:
        (x, y), gifts = queue.popleft()
        if x == len(maze)-1 and y == len(maze[0])-1:
            res.append(gifts)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and (nx, ny) not in visited:
            if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                queue.append(((nx, ny), gifts+maze[nx][ny]))
                # visited.add((nx, ny))


    return max(res)
    



maze = [
    [1, 10, 3, 8],
    [12, 2, 9, 6],
    [5, 7, 4, 11],
    [3, 7, 16, 5]
]

print(func(maze))
