from linked_list import make_from_list, LinkedList


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def print_nodes(head):
    nodes_list = list()
    current_node = head
    while current_node:
        nodes_list.append(current_node.data)

        print(current_node.data)
        current_node = current_node.next
    return nodes_list


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def merge_sorted_lists(headA, headB):
    # A dummy node to store the result
    dummyNode = SinglyLinkedListNode(0)

    # Tail stores the last node
    tail = dummyNode
    while True:

        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # Compare the data of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        # Advance the tail
        tail = tail.next

    # Returns the head of the merged list
    return dummyNode.next


if __name__ == '__main__':
    list1 = [1, 3, 7]
    llist1 = make_from_list(list1)

    list2 = [1, 2]
    llist2 = make_from_list(list2)

    correct_answer = [1, 1, 2, 3, 7]
    merged_list = merge_sorted_lists(llist1.head, llist2.head)
    merged_items = print_nodes(merged_list)
    assert merged_items == correct_answer

    print('Tests passed.')
