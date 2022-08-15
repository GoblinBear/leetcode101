class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def average_of_levels(root):
    ans = []
    if not root:
        return ans
    
    queue = []
    queue.append(root)

    while queue:
        count = len(queue)
        sum = 0
        for i in range(count):
            node = queue.pop(0)
            sum = sum + node.val

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)

        ans.append(sum / count)
    
    return ans


# Test
tree = TreeNode(3,
                TreeNode(9, None, None),
                TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
print(average_of_levels(tree))
# Output: [3, 14.5, 11]
