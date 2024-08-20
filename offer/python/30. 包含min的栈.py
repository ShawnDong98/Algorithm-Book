"""
题目：定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数。在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。
"""


class stack:
    def __init__(self):
        self.stack = []
        self.min_ = float("inf")

    def pop(self):
        return self.stack[-1]

    def push(self, val):
        if val < self.min_:
            self.min_ = val
        return self.stack.append(val)
    
    def min(self):
        return self.min_