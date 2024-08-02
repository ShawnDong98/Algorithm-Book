"""
用数组代表每个人的能力, 一个比赛活动要求参赛团队的最低能力值为N, 每个团队可以由1人或2人组成, 且1个人只能参加1个团队, 请计算出最多可以派出多少支符合要求的团队？

输入描述
第一行代表总人数, 范围[1,500000]

第二行数组代表每个人的能力, 每个元素的取值范围为[1,500000],数组的大小范围[1,500000]

第三行数值为团队要求的最低能力值, 范围[1,500000]

输出描述
3 最多可以派出的团队的数量

示例1
输入：
5
3 1 5 7 9
8

输出：
3

说明：
3, 5组成一队, 1, 7组成一队, 9自己一个队, 故而输出3
"""
N = int(input())

abilities = list(map(int, input().split()))

threshold = int(input())

abilities = sorted(abilities, key=lambda x: -x)

cnt = 0
for i, a in enumerate(abilities):
    if a >= threshold:
        cnt += 1
        abilities.pop(i)

left = 0
right = len(abilities) - 1
while left < right:
    if abilities[left] + abilities[right] >= threshold:
        cnt += 1
        left += 1
        right -= 1
    else:
        right -= 1

print(cnt)