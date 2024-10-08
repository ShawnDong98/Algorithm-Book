"""
橱窗里有一排宝石, 不同的宝石对应不同的价格, 宝石的价格标记为gems[i], 0<=i<n, n = gems.length。宝石可同时出售0个或多个, 如果同时出售多个, 则要求出售的宝石编号连续; 例如客户最大购买宝石个数为m, 购买的宝石编号必须为gems[i],gems[i+1]...gems[i+m-1]。假设你当前拥有总面值为value的钱, 请问最多能购买到多少个宝石, 如无法购买宝石, 则返回0。

输入描述
第一行输入n, 参数类型为int, 取值范围：[0,10^6], 表示橱窗中宝石的总数量。

之后n行分别表示从第0个到第n-1个宝石的价格, 即gems[0]到gems[n-1]的价格, 类型为int, 取值范围：(0,1000]。

之后一行输入v, 类型为int, 取值范围：[0,10^9]表示你拥有的钱。

输出描述
输出int类型的返回值, 表示最大可购买的宝石数量。

示例1
输入：
7
8
4
6
3
1
6
7
10

输出：
3


示例2
输入：
0
1

输出：
0

说明：
因为没有宝石, 所以返回 0

示例3
输入：
9
6
1
3
1
8
9
3
2
4
15

输出：
4
"""

n = int(input())

gems = []

for i in range(n):
    gems.append(int(input()))


res = []
v = int(input())
for start in range(0, len(gems)-1):
    for end in range(start+1, len(gems)):
        if sum(gems[start:end]) <= v:
            res.append(gems[start:end])

if res:
    res = sorted(res, key=lambda x: -len(x))
    print(len(res[0]))
else:
    print(0)