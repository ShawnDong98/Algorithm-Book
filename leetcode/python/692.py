from typing import List
from collections import Counter, defaultdict
import itertools

class Solution:
    def topKFrequent(self, words: List[int], k: int) -> List[int]:
        cnt = Counter(words)
        res =  sorted(cnt, key=lambda word: (-cnt[word], word))
        return res[:k]

    def topKFrequent_20220102(self, words: List[str], k: int) -> List[str]:
        """
        执行用时：36 ms, 在所有 Python3 提交中击败了 66.58% 的用户
        内存消耗：15.1 MB, 在所有 Python3 提交中击败了 27.01% 的用户
        """
        cnt = Counter(words)
        tmp = defaultdict(list)
        for w, c in cnt.most_common():
            tmp[c].append(w)
        
        
        res = [sorted(w) for c, w in tmp.items()]
        res = list(itertools.chain(*res))

        return res[:k]

    def topKFrequent_20220102(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        tmp = defaultdict(list)
        for w, c in cnt.most_common():
            tmp[c].append(w)
        
        res = []
        for c, w in tmp.items():
            print(w)
            res.extend(sorted(w))

        return res[:k]

words = ["i","love","leetcode","i","love","coding"]
k = 3
S = Solution()
print(S.topKFrequent_20220102(words, k))



