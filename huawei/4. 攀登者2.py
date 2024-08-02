"""
攀登者喜欢寻找各种地图, 并且尝试攀登到最高的山峰。地图表示为一维数组, 数组的索引代表水平位置, 数组的高度代表相对海拔高度。其中数组元素0代表地面。

例如[0,1,2,4,3,1,0,0,1,2,3,1,2,1,0], 代表如下图所示的地图, 地图中有两个山脉位置分别为1,2,3,4,5和8,9,10,11,12,13, 最高峰高度分别为4,3。最高峰位置分别为3,10。一个山脉可能有多座山峰(高度大于相邻位置的高度, 或在地图边界且高度大于相邻的高度)。

登山时会消耗登山者的体力(整数), 上山时, 消耗相邻高度差两倍的体力, 下坡时消耗相邻高度差一倍的体力, 平地不消耗体力, 登山者体力消耗到零时会有生命危险。例如, 上图所示的山峰, 从索引0, 走到索引1, 高度差为1, 需要消耗2x1=2的体力, 从索引2高度2走到高度4索引3需要消耗2x2=4的体力。如果是从索引3走到索引4则消耗1x1=1的体力。

攀登者想要评估一张地图内有多少座山峰可以进行攀登, 且可以安全返回到地面, 且无生命危险。

输入描述

第一行输入为地图一维数组

第二行输入为攀登者的体力

输出描述

确保可以安全返回地面, 且无生命危险的情况下, 地图中有多少山峰可以攀登。

用例1

输入

0,1,4,3,1,0,0,1,2,3,1,2,1,0
13

输出

3

说明

> 登山者只能登上位置10和12的山峰, 7 → 10 → 7, 14 → 12 → 14

用例2

输入

1,4,3
999

输出

1,4,3
999

说明

> 没有合适的起点和终点
"""

def calculate_energy(start, end):
    energy = 0
    if start < end:
        energy += 2 * (end - start)
    elif start > end:
        energy += start - end  

    return energy


def count_moutains(heights, energy):
    if len(heights) == 0:
        return 0
    
    peaks = []
    for i in range(len(heights)):
        if i == 0:
            if heights[i+1] < heights[i]:
                peaks.append((heights[i], heights[i], heights[i+1]))

        elif i == len(heights) - 1:
            if heights[i-1] < heights[i]:
                peaks.append((heights[i-1], heights[i], heights[i]))
        else:
            if heights[i-1] < heights[i] and heights[i+1] < heights[i]:
                peaks.append((heights[i-1], heights[i], heights[i+1]))

    res = 0
    for peak in peaks:
        left, top, right = peak
        up = calculate_energy(left, top)
        down = calculate_energy(top, left)
        if up + down <= energy:
            res += 1
    
    return res


    

heights = list(map(int, input().split(",")))
energy = int(input())

print(count_moutains(heights, energy))
