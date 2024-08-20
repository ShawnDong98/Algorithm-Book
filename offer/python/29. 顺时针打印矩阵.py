"""
输⼊⼀个矩阵, 按照从外向⾥以顺时针的顺序依次打印出每个数字
"""
from collections import deque
def bfs(maze):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_row = 0
    current_col = 0

    queue = deque([(0, 0)])
    visited = set()
    visited.add((0, 0))
    current_direction = 0

    while queue:
        x, y = queue.popleft()
        print(maze[x][y])
        dx, dy = direction[current_direction]
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and (nx, ny) not in visited:
            visited.add((nx, ny))
            queue.append((nx, ny))
        else:
            current_direction += 1
            current_direction %= 4
            dx, dy = direction[current_direction]
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maze[0]) and 0 <= ny < len(maze) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))


maze = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
    
bfs(maze)




