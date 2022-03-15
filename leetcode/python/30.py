from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if len(words) == 0: return res
        n = len(s)
        m = len(words)
        w = len(words[0])
        tot = defaultdict(int)
        for word in words: tot[word] += 1
        for i in range(w):
            wd = defaultdict(int)
            cnt = 0
            for j in range(i, n, w):
                if j >= i + m * w:
                    word = s[j - m * w : j - (m - 1) * w]
                    wd[word] -= 1
                    if wd[word] < tot[word]: cnt -= 1
                word = s[j : j + w]
                wd[word] += 1
                if wd[word] <= tot[word]: cnt += 1
                if cnt == m: res.append(j - (m - 1) * w)
        return res
