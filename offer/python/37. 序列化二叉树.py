"""
题目：请实现两个函数，分别用来序列化和反序列化二叉树。
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        def helper(node):
            if not node:
                return "#"
            left_serialized =  helper(node.left)
            right_serialized = helper(node.right)

            return f"{node.val},{left_serialized},{right_serialized}"
        
        return helper(root)
    
    def deserialize(self, data):
        def helper(nodes):
            val = nodes.pop(0)
            if val == "#":
                return None
            
            node = TreeNode(int(val))
            node.left = helper(nodes)
            node.right = helper(nodes)
            return node
        
        node_list = data.split(",")
        return helper(node_list)
    
# Example usage:
codec = Codec()
tree = codec.deserialize("1,2,#,#,3,4,#,#,5,#,#")
serialized_tree = codec.serialize(tree)
print(serialized_tree)  # Output should be "1,2,#,#,3,4,#,#,5,#,#"