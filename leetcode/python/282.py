class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(num, u, length, a, b, target):
            if u == len(num):
                if a == target: res.append(''.join(path[0:length-1]))
            else:
                c = 0
                for i in range(u, len(num)):
                    c = c * 10 + int(num[i])
                    path[length] = num[i]
                    length += 1

                    # +
                    path[length] = '+'
                    dfs(num, i+1, length+1, a+b*c, 1, target)

                    if (i + 1 < len(num)):
                        # -
                        path[length] = '-'
                        dfs(num, i+1, length+1, a+b*c, -1, target)

                       # *
                        path[length] = '*'
                        dfs(num, i+1, length+1, a, b*c, target)

                    if num[u] == '0': break

        res = []
        path = [0] * 100
        dfs(num, 0, 0, 0, 1, target)
        return res 
