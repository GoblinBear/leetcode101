class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root:
        return 1 + max(max_depth(root.left), max_depth(root.right))
    else:
        return 0


tree = TreeNode(3,
                TreeNode(9, None, None),
                TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

# Test
print(max_depth(tree))
