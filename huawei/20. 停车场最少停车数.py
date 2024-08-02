"""
特定大小的停车场, 数组 cars 表示, 其中 1 表示有车, 0 表示没车。车辆大小不一, 小车占一个车位（长度 1), 货车占两个车位（长度 2), 卡车占三个车位（长度 3), 统计停车场最少可以停多少辆车, 返回具体的数目。

输入描述:
整型字符串数组cars[], 其中1表示有车, 0表示没车, 数组长度小于1000。

输出描述: 
整型数字字符串, 表示最少停车数目。

示例 1: 

输入

1,0,1

输出

2


说明

- 1个小车占第1个车位
- 第二个车位空
- 1个小车占第3个车位
- 最少有两辆车

示例 2: 

输入

1,1,0,0,1,1,1,0,1


输出

3

说明

- 1个货车占第1、2个车位
- 第3、4个车位空
- 1个卡车占第5、6、7个车位
- 第8个车位空
- 1个小车占第9个车位
- 最少3辆车
"""

cars = list(map(int, input().split(",")))

i = 0

res = 0

while i < len(cars) - 1:
    cnt = 0
    if cars[i] == 1:
        cnt += 1
        while i < len(cars) - 1 and cars[i] == 1:
            cnt += 1
            i += 1
        if cnt % 3 == 0:
            res += cnt // 3
        elif cnt % 3 != 0:
            res += cnt // 3 + 1
    else:
        i += 1

print(res)
