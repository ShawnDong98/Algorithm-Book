class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, u, x, y):
            if board[x][y] != word[u]: return False
            if u == len(word) - 1: return True

            t = board[x][y]
            board[x][y] = '.'
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if a < 0 or a >= len(board) or b < 0 or b >= len(board[0]) or board[a][b] == '.': 
                    continue
                if dfs(board, word, u + 1, a, b): return True

            board[x][y] = t
            return False

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(board, word, 0, i, j): return True

        return False
