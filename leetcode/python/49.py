from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for st in strs:
            key = ''.join(sorted(st))
            m[key].append(st)
        return list(m.values())

S = Solution()
print(S.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


