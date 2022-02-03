from typing import List

class Solution:
    def solveSudoku_v20220204(self, board: List[List[str]]) -> None:
        def dfs(board, x, y):
            if y ==9:
                x += 1
                y = 0
            if x == 9: return True

            if board[x][y] != '.': return dfs(board, x, y+1)
            for i in range(9):
                if not row[x][i] and not col[y][i] and not cell[x//3][y//3][i]:
                    board[x][y] = str(1+i)
                    row[x][i] = col[y][i] = cell[x//3][y//3][i] = True
                    if (dfs(board, x, y+1)): return True
                    board[x][y] = '.'
                    row[x][i] = col[y][i] = cell[x//3][y//3][i] = False
            return False
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        cell = [[[False] * 9 for _ in range(3)] for _ in range(3)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    t = int(board[i][j]) - 1
                    row[i][t] = col[j][t] = cell[i//3][j//3][t] = True
        dfs(board, 0, 0)
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        从前往后枚举每个空格该填哪个数

        状态： row[9][9]，col[9][9], cell[3][3][9]

        Do not return anything, modify board in-place instead.
        """
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        cell = [[set() for _ in range(3)] for _ in range(3)]
        blank = []

        # 初始化，按照row， col， cell分别存入哈希表
        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    blank.append((i, j))
                else:
                    row[i].add(ch)
                    col[j].add(ch)
                    cell[i // 3][j // 3].add(ch)
        def dfs(n):
            if n == len(blank):
                return True
            i, j = blank[n]
            # 剩余的数字
            rst = nums - row[i] - col[j] - cell[i // 3][j // 3]
            if not rst:
                return False
            for num in rst:
                board[i][j] = num
                row[i].add(num)
                col[j].add(num)
                cell[i//3][j//3].add(num)
                if dfs(n+1):
                    return True
                row[i].remove(num)
                col[j].remove(num)
                cell[i//3][j//3].remove(num)

        dfs(0)


