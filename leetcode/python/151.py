class Solution:
    def reverseWords(self, s: str) -> str:
        s_l = s.split()
        return ' '.join(s_l[::-1])



