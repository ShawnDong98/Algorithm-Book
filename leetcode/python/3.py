class Solution:
    """
    分别以每个字符为起始字符， 逐个字符判断， 直到在哈希表中发现重复字符
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
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

