def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    seq1 = list()
    seq2 = list()

    def get_leaf_seq(root, seq):
        if not root:
            return seq

        if not root.left and not root.right:
            seq.append(root.val)

        seq = get_leaf_seq(root.left, seq)
        seq = get_leaf_seq(root.right, seq)
        return seq

    return get_leaf_seq(root1, seq1) == get_leaf_seq(root2, seq2)