class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        res = ""
        for _ in s:
            if (ord(_) >= 97 and ord(_)<=97+25): res += _
            if (ord(_) >= 65 and ord(_)<=65+25): res += _.lower()
            if (ord(_) >= 48 and ord(_)<=48+9): res += _

        return res == res[::-1]
