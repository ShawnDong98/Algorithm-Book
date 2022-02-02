class Solution:
    def totalNQueens_v20220202(self, n: int) -> int:
        def dfs(u):
            if u == n: return 1
            res = 0
            for i in range(n):
                if not col[i] and not dg[u - i + n] and not udg[u + i]:
                    col[i] = dg[u - i + n] = udg[u + i] = True
                    res += dfs(u + 1)
                    col[i] = dg[u - i + n] = udg[u + i] = False
            return res
        col = [0] * n
        dg, udg = [0] * (2 * n), [0] * (2 * n)
        return dfs(0)
    def totalNQueens(self, n: int) -> int:
        """
        依次枚举每一行皇后的位置
        - 每一列只能有一个皇后， col[N]
        - 每条斜线上只能有一个皇后， d[2N-1], ud[2N-1]
        (x, y)
        (x+y, x-y+n)

        - 从上到下遍历每一行i，并且对于每一行i，分别遍历每一列j；
        每次进入递归，就是进入了新一行的列遍历
        - 因为任何两个皇后都不能处于同一条横行、纵行或斜线上，对于已放置了皇后的位置，
        用set集合记录已经不能再被选择的列col，正斜线pos以及副斜线neg
        - 行号i - 列号j 可确定唯一正斜线，行号i + 列号j 可确定唯一副斜线（自己画一下就明白了）
        - 对于每一行i遍历的列j，只有(i, j)这个位置对应的行和正副斜线不在三个set集合中才可以放置皇后，
        并且递归进入下一行
        - 当前行i == n时，遍历完毕，解的数量 + 1
        """
        col, pos, neg = set(), set(), set()
        def backtrack(i):
            nonlocal res
            if i == n:
                res += 1
                return
            for j in range(n):
                if j not in col and i - j not in pos and i + j not in neg:
                    col.add(j)
                    pos.add(i - j)
                    neg.add(i + j)
                    backtrack(i + 1)
                    col.remove(j)
                    pos.remove(i - j)
                    neg.remove(i + j)
        res = 0
        backtrack(0)
        return res

