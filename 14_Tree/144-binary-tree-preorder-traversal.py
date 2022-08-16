class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root):
    ret = []
    if not root:
        return ret
    
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        ret.append(node.val)
        
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)

    return ret


# Test
tree = TreeNode(3,
                TreeNode(9, TreeNode(2, None, None), TreeNode(5, None, None)),
                TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
print(preorder_traversal(tree))
# Output: [3, 9, 2, 5, 20, 15, 7]
