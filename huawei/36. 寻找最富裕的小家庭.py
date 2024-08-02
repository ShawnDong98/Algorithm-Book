"""
在一棵树中, 每个节点代表一个家庭成员, 节点的数字表示其个人的财富值, 一个节点及其直接相连的子节点被定义为一个小家庭。现给你一棵树, 请计算出最富裕的小家庭的财富和。

输入描述
第一行为一个数N, 表示成员总数, 成员编号1-N, 1<=N<=1000

第二行为N个空格分隔的数, 表示编号1- N 的成员的财富值。 0 <= 财富值 <= 1000000

接下来 N-1 行, 每行两个空格分隔的整数(N1,N2),  表示 N1 是 N2 的父节点。

输出描述
最富裕的小家庭的财富和

示例1
输入：
4
100 200 300 500
1 2
1 3
2 4

输出：
700

示例2
输入：
4
100 200 300 500
1 2
1 3
1 4

输出：
1100
"""
from collections import defaultdict

def max_wealth(N, wealthes, relations):
    res = []
    tree = defaultdict(list)
    for parent, child in relations:
        tree[parent].append(child)
    
    for node in range(1, N+1):
        family_wealth = wealthes[node-1]
        for child in tree[node]:
            family_wealth += wealthes[child-1]

        res.append(family_wealth)

    return max(res)


N = int(input())

wealthes = list(map(int, input().split()))

relations = []

for _ in range(N-1):
    relations.append(list(map(int, input().split())))

print(max_wealth(N, wealthes, relations))
