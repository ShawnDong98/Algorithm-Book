import collections

class Codec:
    """
    序列化：
    - 用BFS遍历树， 与一般遍历不同点是不管node的左右子节点是否存在，
    统统加到队列中
    - 在节点出队时， 如果节点不存在， 在返回值res中加入一个
    null；如果节点存在， 则加入节点值的字符串形式

    反序列化：
    - 同样使用BFS方法， 利用队列新建二叉树
    - 首先要将data转换成列表， 然后遍历，只要不为null将节点按顺序加入二叉树中；
    同时还要将节点入队
    - 队列为空时遍历完毕， 返回根节点
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        queue = collections.deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append('None')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data: return []
        dataList = data[1:-1].split(',')
        root = TreeNode(int(dataList[0]))
        queue = collections.deque([root])
        i = 1
        while queue:
            node = queue.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                queue.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                queue.append(node.right)
            i += 1
        return root
