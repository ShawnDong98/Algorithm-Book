class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        n = len(matrix)
        if not n: return res
        m = len(matrix[0])

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        st = [[False] * m for _ in range(n)]

        i = 0
        x = 0
        y = 0
        d = 0
        while i < n*m:
            res.append(matrix[x][y])
            st[x][y] = True

            a = x + dx[d]
            b = y + dy[d]
            if a < 0 or a >= n or b < 0 or b >= m or st[a][b]:
                d = (d + 1) % 4
                a = x + dx[d]
                b = y + dy[d]
            x = a
            y = b
            i += 1

        return res
