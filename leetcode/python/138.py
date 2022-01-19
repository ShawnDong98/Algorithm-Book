class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
            - 哈希表Mydic映射原有节点->新的节点
            - 原节点为空，则返回空
            - 原节点在哈希表中可以找到，则说明新的节点已生成，直接返回
            - 根据原有节点的值，创建新的节点
            - 将原有节点和新节点的对应关系添加到哈希表中Mydic[node] = root
            - 最后参照原节点的next和random关系，创建新的next和random节点给新节点root
            - 递归整个过程
        """
        Mydic = dict()
        def recursion(node: 'Node') -> 'Node':
            if node is None: return None
            if node in Mydic: return Mydic.get(node)
            root = Node(node.val)
            Mydic[node] = root
            root.next = recursion(node.next)
            root.random = recursion(node.random)
            return root
        return recursion(head)
