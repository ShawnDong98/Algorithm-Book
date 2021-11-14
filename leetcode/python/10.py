import re

class Solution:
    """
        动态规划做不出来
    """
    def isMatch(self, s: str, p: str) -> bool:
        r = re.search(p, s)
        if r and r.group() == s:
            return True
        else:
            return False

