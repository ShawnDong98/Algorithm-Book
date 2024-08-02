"""
绘图机器的绘图笔初始位置在原点 0 0, 机器启动后其绘图笔按下面规则绘制直线:
1 尝试沿着横向坐标轴正向绘制直线, 直到给定的终点值 E。
2 期间可通过指令在纵坐标轴方向进行偏移, 并同时绘制直线, 偏移后按规则 1 绘制直线；指令的格式为 X offsetY, 表示在横坐标 X 沿纵坐标方向偏移, offsetY 为正数表示正向偏移, 为负数表示负向偏移。

给定了横坐标终点值 E、以及若干条绘制指令, 请计算绘制的直线和横坐标轴、以及 X=E 的直线组成图形的面积。

输入描述: 
首行为两个整数 N E, 表示有 N 条指令, 机器运行的横坐标终点值 E。
接下来 N 行, 每行两个整数表示一条绘制指令 X offsetY, 用例保证横坐标 X 以
递增排序方式出现, 且不会出现相同横坐标 X。
取值范围: 0 < N <= 10000, 0 <= X <= E <=20000, -10000 <= offsetY <= 10000。
输出描述: 
一个整数, 表示计算得到的面积, 用例保证, 结果范围在 0~4294967295 内

示例1:

输入

4 10
1 1       # 1
2 1       # 1 + 1*2
3 1       # 1 + 1*2 + 1*3
4 -2      # 1 + 1*2 + 1*3 + 1
 
输出

12
"""

N, E = map(int, input().split())
area = 0
current_x, current_y = 0, 0
for i in range(N):
    X, offsetY = input().split()
    X = int(X)
    width = X - current_x
    height = current_y
    current_x = X
    if offsetY[0] != "-":
        current_y += int(offsetY)
    else:
        current_y -= int(offsetY[1:])
    area += width * height

width = E - current_x
height = current_y
area += width * height

print(area)      
    