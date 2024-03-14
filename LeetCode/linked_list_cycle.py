from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    pos = head
    nodes_visited = list()

    while pos.next is not None:
        if pos.next in nodes_visited:
            return True
        nodes_visited.append(pos)
        pos = pos.next
    if len(set(nodes_visited)) == len(nodes_visited):
        return False
    else:
        return True
