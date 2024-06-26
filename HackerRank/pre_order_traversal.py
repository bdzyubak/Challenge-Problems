class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def preOrder(root):
    node_values = ''
    node_values = traverse(root, node_values)
    node_values = node_values[:-1]  # Remove trailing space
    print(node_values)
    return node_values


def traverse(root, node_values):
    if root:
        # print(root.info)
        node_values += str(root.info) + ' '
        if root.left:
            node_values = traverse(root.left, node_values)

        if root.right:
            node_values = traverse(root.right, node_values)
    return node_values


if __name__ == '__main__':
    tree = BinarySearchTree()
    arr = [1, 2, 5, 3, 4, 6]
    for i in range(len(arr)):
        tree.create(arr[i])

    assert preOrder(tree.root) == '1 2 5 3 4 6'
    print('Done.')

    # Sample output: 1 2 5 3 4 6
