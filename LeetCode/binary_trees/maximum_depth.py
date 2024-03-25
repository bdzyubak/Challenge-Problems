from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth_left = 1 + self.maxDepth(root.left)
        depth_right = 1 + self.maxDepth(root.right)

        return max(depth_left, depth_right)
