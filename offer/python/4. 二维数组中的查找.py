"""
题目:

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的个二维数组和一个整数，判断数组中是否含有该整数。
"""
def search(matrix, value):

    rows = len(matrix)
    cols = len(matrix[0])
    col = cols - 1
    row = 0

    while col > 0 and row < rows:
        if matrix[row][col] == value:
            return True
        elif matrix[row][col] > value:
            col -= 1
        else:
            row += 1

    return False
            


n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

value = int(input())
print(search(matrix, value))