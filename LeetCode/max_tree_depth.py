
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative - breadth first
def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0

    q = [root]
    levels = 0

    while q:
        nodes_at_level = len(q)
        for i in range(nodes_at_level):
            curr = q.pop(0)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        levels += 1

    return levels


# Recursive - depth-first
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0

    left_depth = 1 + self.maxDepth(root.left)
    right_depth = 1 + self.maxDepth(root.right)

    return max(left_depth, right_depth)
