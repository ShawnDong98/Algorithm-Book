"""
部门准备举办一场王者荣耀表演赛, 有10名游戏爱好者参与, 分为两队, 每队5人。每位参与者都有一个评分, 代表着他的游戏水平。为了表演赛尽可能精彩, 我们需要把10名参赛者分为实力尽量相近的两队。一队的实力可以表示为这一队5名队员的评分总和。现在给你10名参与者的游戏水平评分, 请你根据上述要求分队, 最后输出这两组的实力差绝对值。

例:10名参赛者的评分分别为5 1 8 3 4 6 7 10 9 2, 分组为(1 3 5 8 10) (2 4 6 7 9) , 两组实力差最小, 差值为1。有多种分法, 但实力差的绝对值最小为1。

输入
10 个整数, 表示 10 名参与者的游戏水平评分。范围在[1,10000]之间
输出
1 个整数, 表示分组后两组实力差绝对值的最小值。

样例输入 
1 2 3 4 5 6 7 8 9 10
样例输出 
1
"""

from itertools import permutations


scores = list(map(int, input().split()))

min_error = float("inf")
for scores_ in permutations(scores, 10):
    team1 = scores_[:5]
    team2 = scores_[5:]

    if abs(sum(team1) - sum(team2)) < min_error:
        min_error = abs(sum(team1) - sum(team2)) 

print(min_error)































# from itertools import permutations

# inps = list(map(int, input().split()))


# res = 100001
# for inp in permutations(inps):
#     seq1 = inp[:5]
#     seq2 = inp[5:]

#     if abs(sum(seq1) - sum(seq2)) < res:
#         res = min(res, abs(sum(seq1) - sum(seq2)))

# print(res)


