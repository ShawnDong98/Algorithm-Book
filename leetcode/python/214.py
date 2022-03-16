class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]
        n = len(s)
        p = ' ' + s + '#' + t
        ne = [0] * len(p)
        i = 2
        j = 0
        while i < len(p):
            while j and p[i] != p[j+1]: j = ne[j]
            if p[i] == p[j+1]: j += 1
            ne[i] = j
            i += 1

        return s[:ne[-1]-1:-1] + s

