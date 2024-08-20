"""
下图中, 每个方块代表一个像素, 每个像素用其行号和列号表示。下图中的多段线可以用下面的坐标串表示：(2, 8), (3, 7), (3, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 3), (8, 4), (7, 5)。但可以发现, 这种表示不是最简的, 其实只需要存储6个蓝色的关键点即可, 它们是线段的起点、拐点、终点, 而剩下4个点是冗余的。现在, 请根据输入的包含有冗余数据的多段线坐标列表, 输出其最简化的结果。

输入描述

2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5

1、所有数字以空格分隔, 每两个数字一组, 第一个数字是行号, 第二个数字是列号；

2、行号和列号范围为[0,64), 用例输入保证不会越界, 考生不必检查；

3、输入数据至少包含两个坐标点。

输出描述

2 8 3 7 3 5 6 2 8 4 7 5

压缩后的最简化坐标列表, 和输入数据的格式相同。 

示例1
输入输出示例仅供调试, 后台判题数据一般不包含示例

输入

2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5

输出

2 8 3 7 3 5 6 2 8 4 7 5

说明

如上图所示, 6个蓝色像素的坐标依次是(2,8)、(3,7)、(3,5)、(6,2)、(8,4)、(7,5)。

将他们按顺序出即可。

备注

输出的坐标相对顺序不能变化。
"""


def simplify_coordinates(points):

    simplified_points = [points[0]]
    
    def direction(p1, p2):
        return (p2[0] - p1[0], p2[1] - p1[1])
    
    for i in range(1, len(points) - 1):
        prev_direction = direction(points[i-1], points[i])
        next_direction = direction(points[i], points[i+1])

        if prev_direction != next_direction:
            simplified_points.append(points[i])


    simplified_points.append(points[-1])

    res = []
    for x, y in simplified_points:
        res.append(x)
        res.append(y)

    return res

    


coords = list(map(int, input().split()))

points = [(coords[i], coords[i+1]) for i in range(0, len(coords), 2)]

res = simplify_coordinates(points)

print(" ".join(map(str, res)))