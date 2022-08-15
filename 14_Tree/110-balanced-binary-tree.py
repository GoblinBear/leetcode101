class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root):
    return helper(root) != -1


def helper(root):
    if not root:
        return 0
    
    left = helper(root.left)
    right = helper(root.right)

    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1
    
    return 1 + max(left, right)


# Test
tree = TreeNode(1,
                TreeNode(2, 
                         TreeNode(3, None, None),
                         TreeNode(3, TreeNode(4, None, None), TreeNode(4, None, None))),
                TreeNode(2, None, None))
print(is_balanced(tree))
# Output: False
