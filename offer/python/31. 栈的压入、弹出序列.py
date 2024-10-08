"""
题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。
"""

def func(push_seq, pop_seq):
    stack = []
    for num in push_seq:
        stack.append(num)

        while stack and stack[-1] == pop_seq[0]:
            pop_seq.pop(0)
            stack.pop(-1)
    
    return not stack


push_seq = [1, 2, 3, 4, 5]
pop_seq = [4, 5, 3, 2, 1]

print(func(push_seq, pop_seq))