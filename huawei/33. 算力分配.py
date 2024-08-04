"""
现有两组服务器A和B, 每组有多个算力不同的CPU, 其中A[i]是A组第i个CPU的运算能力, B[i]是B组第i个CPU的运算能力。一组服务器的总算力是各CPU的算力之和。为了让两组服务器的算力相等, 允许从每组各选出一个CPU进行一次交换, 求两组服务器中, 用于交换的CPU的算力, 并且要求从A组服务器中选出的CPU, 算力尽可能小。

输入描述:

第一行输入为L1和L2, 以空格分隔, L1表示A组服务器中的CPU数量, L2表示B组服务器中的CPU数量。

第二行输入为A组服务器中各个CPU的算力值, 以空格分隔。

第三行输入为B组服务器中各个CPU的算力值, 以空格分隔。

1<=L1<=10000

1<=L2<=10000

1 <=A[i]<=100000

1 <=B[i]<=100000

输出描述:

对于每组测试数据, 输出两个整数, 以空格分隔, 依次表示A组选出的CPU算力、B组选出的CPU算力。要求从A组选出的CPU的算力尽可能小。

备注: 保证两组服务器的初始总算力不同。答案肯定存在。

用例：

输入	
2 2
1 1
2 2
输出	
1 2
"""

L1, L2 = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

res = []

sum_A = sum(A)
sum_B = sum(B)

for a in A:
    for b in B:
        if sum_A - a + b == sum_B - b + a:
            res.append((a, b))

res = sorted(res, key=lambda x: x[0])

print(" ".join(map(str, res[0])))
