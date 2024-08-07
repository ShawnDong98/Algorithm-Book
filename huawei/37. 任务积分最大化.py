"""
现有N个任务需要处理, 同一时间只能处理一个任务, 处理每个任务所需要的时间固定为1。每个任务都有最晚处理时间限制和积分值, 在最晚处理时间点之前处理完成任务才可获得对应的积分奖励。可用于处理任务的时间有限, 请问在有限的时间内, 可获得的最多积分。

输入描述
第一行为一个数 N , 表示有 N 个任务(1 ≤ N ≤ 100)

第二行为一个数 T , 表示可用于处理任务的时间。(1 ≤ T ≤ 10)

接下来 N 行, 每行两个空格分隔的整数(SLA 和 和 V), SLA 表示任务的最晚处理时间, V 表示任务对应的积分。

1≤SLA≤100 , 0 ≤ V ≤ 100000

输出描述
可获得的最多积分

示例1
输入：
4
3
1 2
1 3
1 4
1 5

输出：
5

说明：
虽然有 3 个单位的时间用于处理任务, 可是所有任务在时刻1之后都无效。 所以在第 1 个时间单位内, 选择处理有 5 个积分的任务。1-3 时无任务处理。

示例2

4
3
1 2
1 3
1 4
3 5

输出：
9

说明：
第 1 个时间单位内, 处理任务3, 获得 4 个积分
第 2 个时间单位内, 处理任务 4, 获得 5 个积分
第 3 个时间单位内, 无任务可处理。
共获得 9 个积分
"""
def func(N, T, tasks):
    tasks = sorted(tasks, key=lambda x: (-x[1], x[0]))
    total_score = 0
    time_slots = [False] * (T+1)

    for sla, score in tasks:
        for i in range(min(sla, T), 0, -1):
            if not time_slots[i]:
                time_slots[i] = True
                total_score += score
                break

    return total_score


N = int(input())

T = int(input())

tasks = []
for i in range(N):
    SLA, V = list(map(int, input().split()))
    tasks.append((SLA, V))


print(func(N, T, tasks))