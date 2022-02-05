class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(s, u, path, cnt, l, r):
            if u == len(s):
                if not cnt: res.append(path)
                return
            if (s[u] != '(' and s[u] != ')'): dfs(s, u+1, path+s[u], cnt, l, r)
            elif s[u] == '(':
                k = u
                while k < len(s) and s[k] == '(': k += 1
                l -= k - u
                for i in range(k-u, -1, -1):
                    if l >= 0: dfs(s, k, path, cnt, l, r)
                    path += '('
                    cnt += 1
                    l += 1
            elif s[u] == ')':
                k = u
                while k < len(s) and s[k] == ')': k += 1
                r -= k - u
                for i in range(k-u, -1, -1):
                    if cnt >= 0 and r >= 0: dfs(s, k, path, cnt, l, r)
                    path += ')'
                    cnt -= 1
                    r += 1
        res = []
        l = r = 0
        for x in s:
            if x == '(': l += 1
            elif x == ')':
                if l==0: r += 1
                else: l -= 1
        dfs(s, 0, '', 0, l, r)
        return res
