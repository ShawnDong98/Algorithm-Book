"""
1.众数是指一组数据中出现次数量多的那个数, 众数可以是多个
2.中位数是指把一组数据从小到大排列, 最中间的那个数, 如果这组数据的个数是奇数, 那最中间那个就是中位数, 如果这组数据的个数为偶数, 那就把中间的两个数之和除以2, 所得的结果就是中位数
3.查找整型数组中元素的众数并组成一个新的数组, 求新数组的中位数

输入描述: 

输入一个一维整型数组, 数组大小取值范围 0<n<1000
数组中每个元素取值范围,  0<e<1000

输出描述: 

输出众数组成的新数组的中位数。

示例

1.输入: 

10 11 21 19 21 17 21 16 21 18 16

输出: 21

2.输入: 

2 1 5 4 3 3 9 2 7 4 6 2 15 4 2 4

输出: 3

3.输入: 

5 1 5 3 5 2 5 5 7 6 7 3 7 11 7 55 7 9 98 9 17 9 15 9 9 1 39
输出: 7
"""
from collections import Counter
def func(nums):
    cnt = Counter(nums)
    cnt = sorted(cnt.items(), key=lambda x: -x[1])
    max_cnt = cnt[0][1]
    new_nums = [c[0] for c in cnt if c[1] == max_cnt]
    medium_idx = len(new_nums) // 2
    if len(new_nums) % 2 != 0:
        return new_nums[medium_idx]
    else:
        return int((new_nums[medium_idx-1] + new_nums[medium_idx]) / 2)
    

nums = list(map(int, input().split()))

print(func(nums))

