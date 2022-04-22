class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        c = ''
        i = 0
        t = 0
        while i < len(a) or i < len(b) or t:
            if i < len(a): t += int(a[i])
            if i < len(b): t += int(b[i])
            c += str(t % 2)
            t //= 2
            i += 1

        c = c[::-1]
        return c
