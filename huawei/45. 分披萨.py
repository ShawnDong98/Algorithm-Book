"""
吃货和馋嘴两人到披萨店点了一份铁盘(圆形）萨, 并嘱咐店员将披萨按放射状切成大小相同的偶数扇形小块。但是粗心服务员将披萨切成了每块大小都完全不同奇数块, 且肉眼能分辨出大小。由于两人都想吃到最多的披萨, 他们商量了一个他们认为公平的分法：从吃货开始, 轮流取披萨。除了第一块披萨可以任意选取以外, 其他都必须从缺口开始选。他俩选披萨的思路不同。馋嘴每次都会选最大块的披萨, 而且吃货知道馋嘴的想法。已知披萨小块的数量以及每块的大小, 求吃货能分得的最大的披萨大小的总和。

输入描述
第一行为一个正整数奇数N, 表示披萨小块数量。
3 ≤ N ≤ 500

接下来的第2行到第N + 1行(共N行), 每行为一个正整数, 表示第i块披萨的大小 1 ≤ i ≤ N

披萨小块从某一块开始, 按照一个方向次序顺序编号为1 ~ N
每块披萨的大小范围为 [1, 2147483647]

输出描述
“吃货”能吃到的最大的披萨大小的总和。

示例1:
输入
5
8
2
10
5
7
输出
19

说明

此例子中, 有5块披萨。每块大小依次为8、2、10、5、7。按照如下顺序拿披萨, 可以使“吃货”拿到最多披萨：

1、“吃货”拿大小为10的披萨

2、“馋嘴”拿大小为5的披萨

3、“吃货”拿大小为7的披萨

4、“馋嘴”拿大小为8的披萨

5、“吃货”拿大小为2的披萨

至此, 披萨瓜分完毕, “吃货”拿到的披萨总大小为10+7+2=19。
"""

def func(slices):
    max_pizza = max(slices)
    index_max = slices.index(max_pizza)

    total_sum = max_pizza
    a = index_max - 1
    b = index_max + 1
    turn = 1

    while True:
        piece_size = 0
        if a < 0:
            a = len(slices) - 1
        if b >= len(slices):
            b = 0
        if a == b:
            total_sum += slices[a]
            break
        if slices[a] > slices[b]:
            piece_size = slices[a]
            a -= 1
        else:
            piece_size = slices[b]
            b += 1
        if turn % 2 == 0:
            total_sum += piece_size

        turn += 1

    return total_sum 


N = int(input())

slices = []

for i in range(N):
    slices.append(int(input()))

print(func(slices))
