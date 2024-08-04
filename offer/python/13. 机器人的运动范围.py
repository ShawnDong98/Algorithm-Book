"""
题 ⽬ : 地 上 有 ⼀ 个 m ⾏ n 列 的 ⽅ 格 。 ⼀ 个 机 器 ⼈ 从 坐 标 (0 , 0 ) 的 格 ⼦ 开 始 移 动, 它 每 次 可 以 向 左 、 右 、 上 、 下 移 动 ⼀ 格 , 但 不 能 进 ⼊ ⾏ 坐 标 和 列 坐 标 的 数 位 之 和 ⼤ 于 k 的 格 ⼦ 。 例 如 , 当 k 为 1 8 时 , 机 器 ⼈ 能 够 进 ⼊ ⽅ 格 (3 5 , 3 7) , 因 为 3 + 5 + 3 + 7 = 1 8 。 但 它 不 能 进 ⼊ ⽅ 格 (3 5 , 3 8) , 因 为 3 + 5 + 3 + 8 = 1 9 。 请 问 该 机 器 ⼈ 能 够 到 达 多 少 个 格 ⼦ ?
"""
from collections import deque
def func(maze, k):
    rows = len(maze)
    cols = len(maze[0])
    queue = deque([(0, 0)])
    visited = set((0, 0))
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and (eval("+".join(list(str(nx)))) + eval("+".join(list(str(ny))))) <= k:
                queue.append((nx, ny))
                visited.add((nx, ny))
                cnt += 1

    return cnt




maze = [
    ['a', 'b', 'c', 'e'],
    ['s', 'f', 'c', 's'],
    ['a', 'd', 'e', 'e'],
    ['a', 'd', 'e', 'e']
]

k = 1

print(func(maze, k))

