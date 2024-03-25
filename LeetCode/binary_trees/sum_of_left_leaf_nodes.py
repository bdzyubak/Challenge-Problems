
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumOfLeftLeaves(root: Optional[TreeNode]) -> int:
    queue = [(root, False)]
    if not root:
        return 0
    sum = 0

    while queue:
        node, is_left = queue.pop(0)
        if node.left is None and node.right is None and is_left:
            sum += node.val
        else:
            if node.left:
                queue += [(node.left, True)]
            if node.right:
                queue += [(node.right, False)]
    return sum