from collections import defaultdict
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash = defaultdict(int)
        for i in range(len(s)-9):
            hash[s[i:i+10]] += 1
        res = []
        for k, v in hash.items():
            if v > 1:
                res.append(k)
        return res

s = "AAAAAAAAAAA"
S = Solution()
print(S.findRepeatedDnaSequences(s))
