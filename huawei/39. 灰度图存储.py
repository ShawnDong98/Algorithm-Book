"""
黑白图像常采用灰度图的方式存储, 即图像的每个像素填充一个灰阶值, 256阶灰度图是一个灰阶值取值范围为0到255的灰阶矩阵, 0表示全黑、255表示全白, 范围内的其他值表示不同的灰度, 比如下面的图像及其对应的灰阶矩阵:

但在计算机中实际存储时, 会使用压缩算法, 其中一种压缩格式和描述如下:

10 10 255 34 0 1 255 8 0 3 255 6 0 5 255 4 0 7 255 2 0 9 255 21

1、所有数值以空格分隔
2、前两个数分别表示矩阵的行数和列数
3、从第三个数开始, 每两个数一组, 每组第一个数是灰阶值, 第二个数表示该灰阶值从左到右, 从上到下的连续像素个数。比如题目所述例子, “255 34”表示有连续34个像素的灰阶值是255。

如此, 图像软件在打开此格式灰度图的时候, 就可以根据此算法从压缩数据恢复出原始灰度图矩阵。

请从输入的压缩数恢复灰度图原始矩阵, 并返回指定像素的灰阶值。

输入描述
10 10 255 34 0 1 255 8 0 3 255 6 0 5 255 4 0 7 255 2 0 9 255 21

3 4

输入包行两行, 第一行是灰度图压缩数据, 第二行表示一个像素位置的行号和列号, 如 0 0 表示左上角像素。

输出描述
0

输出数据表示的灰阶矩阵的指定像素的灰阶值。

示例1
输入:
10 10 56 34 99 1 87 8 99 3 255 6 99 5 255 4 99 7 255 2 99 9 255 21
3 4

输出:
99

说明:
将压缩数据恢复后的灰阶矩阵第3行第4列的像素灰阶值是99。
示例2
输入:
10 10 255 34 0 1 255 8 0 3 255 6 0 5 255 4 0 7 255 2 0 9 255 21
3 5

输出:
255

说明:
将压缩数据恢复后的灰阶矩阵第3行第5列的像案灰阶值是255。
"""

def func(inp, row, col):
    rows = inp[0]
    cols = inp[1]

    matrix = [[0] * cols for _ in range(rows)]

    compressed_data = inp[2:]
    index = 0

    current_row = 0
    current_col = 0

    while index < len(compressed_data):
        value = compressed_data[index]
        count = compressed_data[index + 1]
        index += 2

        for i in range(count):
            matrix[current_row][current_col] = value
            current_col += 1
            if current_col >= cols:
                current_col = 0
                current_row += 1

    return matrix[row][col]





inp = list(map(int, input().split()))

row, col = map(int, input().split())

print(func(inp, row, col))