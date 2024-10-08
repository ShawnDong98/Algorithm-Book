"""
为了达到新冠疫情精准防控的需要, 为了避免全员核酸检测带来的浪费, 需要精准圈定可能被感染的人群。现在根据传染病流调以及大数据分析, 得到了每个人之间在时间、空间上是否存在轨迹的交叉。现在给定一组确诊人员编号(X1, X2, X3, .... Xn),在所有人当中, 找出哪些人需要进行核酸检测, 输出需要进行核酸检测的人数。(注意: 确诊病例自身不需要再做核酸检测)需要进行核酸检测的人, 是病毒传播链条上的所有人员, 即有可能通过确诊病例所能传播到的所有人。例如: A是确诊病例, A和B有接触、B和C有接触、C和D有接触、D和E有接触, 那么BCDE都是需要进行核酸检测的人。

输入描述
第一行为总人数N

第二行为确诊病例人员编号 (确证病例人员数量 < N) , 用逗号隔开

接下来N行, 每一行有N个数字, 用逗号隔开, 其中第i行的第个j数字表名编号i是否与编号j接触过。0表示没有接触, 1表示有接触

输出描述
输出需要做核酸检测的人数

补充说明

人员编号从0开始
0 < N < 100

示例1
输入: 
5
1,2
1,1,0,1,0
1,1,0,0,0
0,0,1,0,1
1,0,0,1,0
0,0,1,0,1

输出
3

说明: 
编号为1、2号的人员为确诊病例1号与0号有接触, 0号与3号有接触, 2号54号有接触。所以, 需要做核酸检测的人是0号、3号、4号,总计3人要进行核酸检测。
题解
"""
from collections import deque



def func(chains, ills):
    queue = deque(ills)
    visited = set()
    for ill in ills:  
        visited.add(ill)

    cnt = 0

    while queue:
        ill = queue.popleft()
        chain = chains[ill]
        for i in range(0, len(chain)):
            if chain[i]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
                    cnt += 1


    return cnt



N = int(input())

ills = list(map(int, input().split(","))) 

chains = []
for i in range(N):
    chains.append(list(map(int, input().split(","))))


print(func(chains, ills))
