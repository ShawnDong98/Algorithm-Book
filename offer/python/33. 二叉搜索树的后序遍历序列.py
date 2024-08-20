"""
题目：输入一个整数数组, 判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true, 否则返回 false。假设输入的数组的任意两个数字都互不相同。

例如, 输入数组 {5, 7, 6, 9, 11, 10, 8}, 则返回 true, 因为这个整数序列是图 4.9 二叉搜索树的后序遍历结果。如果输入的数组是 {7, 4, 6, 5}, 则由于没有哪棵二叉搜索树的后序遍历结果是这个序列, 因此返回 false。
"""

def verify_postorder(postorder):
    def verify(postorder, start, end):
        if start >= end:
            return True
        
        root = postorder[end]
        i = start
        while i < end and postorder[i] < root:
            i  += 1

        for j in range(i, end):
            if postorder[j] < root:
                return False
            
        return verify(postorder, start, i - 1) and verify(postorder, i, end-1)
    
    if not postorder:
        return True
    
    return verify(postorder, 0, len(postorder) - 1)


# 测试
print(verify_postorder([5, 7, 6, 9, 11, 10, 8]))  # 输出: True
print(verify_postorder([7, 4, 6, 5]))             # 输出: False

