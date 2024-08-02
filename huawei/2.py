"""
题目：工位由序列 F1,F2...Fn 组成,  Fi 值为 0 、1 或 2 , 其中 0 代表空置, 1 代表有人, 2 代表障碍物。 

某一空位的友好度为左右连续老员工工数之和 

为方便新员工学习求助, 优先安排友好度高的空位； 给出工位序列, 求所有空位中友好度的最大值。

输入： 输入第一行为工位序列: F1, F2...Fn 组成, 1≤n≤100000 , Fi值为 0 、1 或 2 , 其中 0 代表空置, 1 代表有人, 2 代表障碍物。

输出：所有空位中友好度的最大值。如果没有空位, 返回 0。

示例： 
输入:0 1 0
输出: 1
"""
def max_friendlyness(F):
    n = len(F)
    friendlyness = [0] * n  # 初始化友好度数组

    # 计算第 i 个空位的友好度
    for i in range(n):
        if F[i] == 0:  # 如果该空位为空置
            left_count = 0  # 左侧老员工工数
            j = i - 1
            while j >= 0 and F[j] != 2:
                if F[j] == 1:
                    left_count += 1
                j -= 1

            right_count = 0  # 右侧老员工工数
            j = i + 1
            while j < n and F[j] != 2:
                if F[j] == 1:
                    right_count += 1
                j += 1

            # 计算友好度
            friendlyness[i] = left_count + right_count

    if max(friendlyness) > 0:  # 如果存在空位
        return max(friendlyness)
    else:
        return 0

F = list(map(int, input().split()))  # 获取工位序列
print(max_friendlyness(F))  # 输出所有空位中友好度的最大值