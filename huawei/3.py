"""
已知树形结构的所有节点信息,  现要求根据输入坐标(x, y)找到该节点保存的内容值,  其中x表示节点所在的层数,  根节点位于第0层, 根节点的子节点位于第1层, 以此类推;  y表示节点在该层内的相对偏移, 从左至右, 第一个节点偏移0, 第二个节点偏移1, 依此类推; 

输入描述：每个节点以一维数组(int[])表示, 所有节点信息构成二维数组(int[][]),  二维数组的0位置存放根节点; 表示单节点的一维数组中,  0位置保存内容值, 后续位置保存子节点在二维数组中的索引位置; 根节点可以表示为(10, 1, 2),  树的整体表示为((10, 1, 2), (-21, 3, 4), (23, 5), (14), (35), (66))

输出描述: 查询到内容值时, 输出(内容值), 查询不到输出() 

示例：输入： 0 10 1 2 -21 3 4 23 5 14 35 66 1 1 

输出: (23)
"""



class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def build_tree(nodes):
    tree = {}
    for i, node in enumerate(nodes):
        tree[i] = Node(node[0], node[1:])
    return tree

def dfs(tree, node_id, x, y):
    node = tree[node_id]
    if x == 0 and y == 0:
        return node.value
    if x < 0 or y < 0 or y >= len(tree[x].children):
        return None
    child_id = tree[x].children[y]
    if child_id is None:
        return None
    return dfs(tree, child_id, x-1, 0)

if __name__ == "__main__":
    nodes = [[0, 1, 2], [10, 3, 4], [21, 5], [23], [14, 6, 7], [35], [66], None, None, [1]]
    tree = build_tree(nodes)
    x, y = 2, 0
    res = dfs(tree, 0, x, y)
    print("({})".format(res) if res is not None else "()")