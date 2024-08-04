"""
题 ⽬: 请 设 计 ⼀ 个 函 数 ,  ⽤ 来 判 断 在 ⼀ 个 矩 阵 中 是 否 存 在 ⼀ 条 包 含 某字 符 串 所 有 字 符 的 路 径 。 路 径 可 以 从 矩 阵 中 的 任 意 ⼀ 格 开 始 ,  每 ⼀ 步 可 以 在 矩 阵 中 向 左 、 右 、 上 、 下 移 动 ⼀ 格 。 如 果 ⼀ 条 路 径 经 过 了 矩 阵 的 某 ⼀ 格 , 那 么 该 路 径 不 能 再 次 进 ⼊ 该 格 ⼦ 。 例 如 ,  在 下 ⾯ 的 3 x 4 的 矩 阵 中 包 含 ⼀ 条 字 符 串 “ b f c e ” 的 路 径 ( 路 径 中 的 字 母 ⽤ 下 画 线 标 出 ) 。 但 矩 阵 中 不 包 含 字 符 串 “ a b f b ” 的 路 径 ,  因 为 字 符 串 的 第 ⼀ 个 字 符 b 占 据 了 矩 阵 中 的 第 ⼀ ⾏ 第 ⼆ 个 格 ⼦ 之 后 ,  路 径 不 能 再 次 进 ⼊ 这 个 格 ⼦
"""
from collections import deque

def exist(board, word):

    def bfs(i, j):
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(i, j, 0)])
        visited = set((i, j))

        while queue:
            i, j, index = queue.popleft()
            if index == len(word) - 1:
                return True
            
            for dx, dy in direction:
                nx, ny = j + dx, i + dy
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and (nx, ny) not in visited and board[ny][nx] == word[index+1]:
                    print(board[ny][nx])
                    queue.append((nx, ny, index+1))
                    visited.add((nx, ny))


    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == word[0] and bfs(i, j):
                return True
    return False



# Example usage
board = [
    ['a', 'b', 'c', 'e'],
    ['s', 'f', 'c', 's'],
    ['a', 'd', 'e', 'e']
]
word1 = "bfce"
word2 = "abfb"

print(exist(board, word1))  # Output: True
print(exist(board, word2))  # Output: False