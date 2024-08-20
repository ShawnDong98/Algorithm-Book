"""
寿司店周年庆, 正在举办优惠活动回馈新老客户。寿司转盘上总共有n盘寿司, prices[i]是第i盘寿司的价格, 如果客户选择了第i盘寿司, 寿司店免费赠送客户距离第i盘寿司最近的下一盘寿司 j, 前提是prices[j]小于prices[i], 如果没有满足条件的 j, 则不赠送寿司。每个价格的寿司都可无限供应。

输入描述
输入的每一个数字代表每盘寿司的价格, 每盘寿司的价格之间使用空格分隔, 例如:

3 15 6 14

表示: 

第 0 盘寿司价格 prices[0] 为 3

第 1 盘寿司价格 prices[1] 为 15

第 2 盘寿司价格 prices[2] 为 6

第 3 盘寿司价格 prices[3] 为 14

寿司的盘数 n 范围为: 1 ≤ n ≤ 500

每盘寿司的价格 price 范围为: 1 ≤ price ≤ 1000

输出描述
输出享受优惠后的一组数据, 每个值表示客户选择第 i 盘寿司时实际得到的寿司的总价格。使用空格进行分隔, 例如: 

3 21 9 17 

用例1

输入: 

3 15 6 14
输出: 

3 21 9 17


用例2

输入: 

10 8 5 12
输出: 

18 13 5 22
"""

prices = list(map(int, input().split()))

prices_ = prices + prices

n = len(prices)

for i in range(len(prices)):
    for j in range(i, i + n):
        if prices_[j] < prices_[i]:
            prices[i] += prices_[j]
            break

print(prices)








# def calculate_discounted_prices(prices):
#     n = len(prices)
#     result = [0] * n

#     for i in range(n):
#         j = 1
#         result[i] = prices[i]
#         while j <= n:
#             idx = (i + j) % n
#             if prices[idx] < prices[i]:
#                 result[i] += prices[idx]
#                 break

#             j += 1

#     return result

# prices = list(map(int, input().split()))

# res = calculate_discounted_prices(prices)

# print(" ".join(map(str, res)))