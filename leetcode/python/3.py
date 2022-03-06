from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring_v20220306(self, s: str) -> int:
        res = 0
        heap = defaultdict(int)
        i, j = 0, 0
        while i < len(s):
            heap[s[i]] += 1
            while heap[s[i]] > 1:
                heap[s[j]] -= 1
                j += 1
            res = max(res, i - j + 1)
            i += 1
        return res
    def lengthOfLongestSubstring(self, s: str) -> int:
    """
    分别以每个字符为起始字符， 逐个字符判断， 直到在哈希表中发现重复字符
    """
        ans = 0
        hash_set = set()

        for i in range(len(s)):
            cur_ans = 0
            for j in range(i, len(s)):
                if s[j] in hash_set:
                    hash_set.clear()
                    break
                else:
                    hash_set.add(s[j])
                    cur_ans += 1
            ans = max(ans, cur_ans)
        return ans

