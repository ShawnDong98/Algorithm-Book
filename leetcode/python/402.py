class Solution:
    """
        对于两个数 123a456 和 123b456，如果 a > b， 那么数字 123a456 大于 数字 123b456，否则数字 123a456 小于等于数字 123b456。也就说，两个相同位数的数字大小关系取决于第一个不同的数的大小

        - 从左到右遍历
        - 对于遍历到的元素，我们选择保留。
        - 但是我们可以选择性丢弃前面相邻的元素。
        - 丢弃与否的依据如上面的前置知识中阐述中的方法。

        如果给定的数字是一个单调递增的数字，那么算法会永远选择不丢弃。这个题目中要求的，要永远确保丢弃 k 个矛盾。

        题目要求丢弃 k 个， 就是保留 n - k 个元素。
        按照上面的方法遍历完成之后，再截取前n - k个元素即可
    """
    def removeKdigits(self, num: str, k: int) -> str:
        stack= []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'


