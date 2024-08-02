"""
从前有个村庄, 村民们喜欢在各种田地上插上小旗子, 旗子上标识了各种不同的数字。某天集体村民决定将覆盖相同数字的最小矩阵形的土地分配给为村里做出巨大贡献的村民, 请问, 此次分配土地, 做出贡献的村民中最大会分配多大面积？

输入描述：
第一行输入n和m, m代表村子的土地的长, n代表土地的宽
第二行开始输入地图上的具体标识
输出描述：
输出需要分配的土地面积, 即包含相同数字旗子的最小矩阵中的面积。
补充说明：
旗子的数字为1-500, 土地边长不超过500
未插旗子的土地用标识0
示例1
输入：
3 3
1 0 1
0 0 0
0 1 0
输出：
9
说明：
土地上的旗子为1, 其坐标分别为(0,0), (2,1)以及(0,2), 为了覆盖所有旗子, 矩阵需要覆盖的横坐标为0和2, 纵坐标为0和2, 所以面积为9, 即(2-0+1)*(2-0+1)=9。
示例2
输入：
3 3
1 0 2
0 0 0
0 3 4
输出：
1
说明：
由于不存在成对的小旗子, 故而返回1, 即一块土地的面积。
"""
def func(n, m, maze):
    boundaries = {}
    for i in range(n):
        for j in range(m):
            if maze[i][j] != 0:
                if maze[i][j] not in boundaries:
                    boundaries[maze[i][j]] = [i, j, i, j]
                else:
                    boundaries[maze[i][j]][0] = min(boundaries[maze[i][j]][0], i)
                    boundaries[maze[i][j]][1] = min(boundaries[maze[i][j]][1], j)
                    boundaries[maze[i][j]][2] = max(boundaries[maze[i][j]][2], i)
                    boundaries[maze[i][j]][3] = max(boundaries[maze[i][j]][3], j)
        
    max_area = 0
    for k, v in boundaries.items():
        left, top, right, bottom = v
        area = (right - left + 1) * (bottom - top + 1)
        if area > max_area:
            max_area = area
    
    return max_area

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input().split())))

print(func(n, m, maze))