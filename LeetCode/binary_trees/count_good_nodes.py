def goodNodes(self, root: TreeNode) -> int:
    def count_good_nodes(node, path_max):
        if not node:
            return 0

        if path_max <= node.val:
            count = 1
        else:
            count = 0

        if node.val > path_max:
            path_max = node.val

        count += count_good_nodes(node.left, path_max)
        count += count_good_nodes(node.right, path_max)

        return count

    return count_good_nodes(root, root.val)