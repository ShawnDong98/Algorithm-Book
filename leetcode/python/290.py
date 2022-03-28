from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False
        if len(pattern) != len(words): return False
        pw = defaultdict(str)
        wp = defaultdict(str)
        for i in range(len(pattern)):
            a = pattern[i]
            b = words[i]
            if a in pw and pw[a] != b: return False
            pw[a] = b
            if b in wp and wp[b] != a: return False
            wp[b] = a

        return True
