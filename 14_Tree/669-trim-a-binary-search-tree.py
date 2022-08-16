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


def trim_BST(root, low, high):
    if not root:
        return root

    if root.val > high:
        return trim_BST(root.left, low, high)
    
    if root.val < low:
        return trim_BST(root.right, low, high)

    root.left = trim_BST(root.left, low, high)
    root.right = trim_BST(root.right, low, high)
    return root


# Test
tree = TreeNode(1,
                TreeNode(0, None, None),
                TreeNode(2, None, None))
print(preorder_traversal(trim_BST(tree, 1, 2)))
# Output: [1, 2]
tree = TreeNode(3,
                TreeNode(0, None, TreeNode(2, TreeNode(1, None, None), None)),
                TreeNode(4, None, None))
print(preorder_traversal(trim_BST(tree, 1, 3)))
# Output: [3, 2, 1]
