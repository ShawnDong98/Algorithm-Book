class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 指向 s 的首位
        left, right = 0, len(s) - 1
        # 指向 t 的首位
        begin, end = 0, len(t) - 1
        while begin <= end:
            # 找到了
            if left > right:
                break
            # 找到了 s 的左
            if t[begin] == s[left]:
                # 找 s 左的下一个
                left += 1
            # 找到了 s 的右
            if t[end] == s[right]:
                # 找 s 右的下一个
                right -= 1
            begin += 1
            end -= 1
        # 找到了
        if left > right:
            return True
        else:
            return False
            
