class Solution:
    def magicalString(self, n: int) -> int:
        """
        例一：
        1 2 2 1 1 2 1
        1 2 2 1 1

        例二：
        2 2 1 1 2 1 2 2
        2 2 1 1 2
        """
        s = "122"
        i = 2
        k = 1
        while len(s) < n:
            for j in range(0, int(s[i])):
                s += str(k)
            i += 1
            k = 3 - k

        res = 0
        for i in range(n): res += s[i] == '1'
        return res
