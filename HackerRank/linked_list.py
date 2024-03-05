from copy import deepcopy


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if not self.head:
            print('Empty list.')
            return
        items = list()
        current = self.head
        while current:
            print(current.data)
            items.append(current.data)
            current = current.next
        return items

    def insert_start(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self):
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.insert_start(current.data)
            current = current.next
        return new_list

    # def reverse(self): 
    #     # Verbose version with insert_start expanded
    #     new_list = LinkedList()
    #     current = self.head
    #     while current: 
    #         # Insert at start part
    #         new_data = Node(current.data)
    #         current_head = new_list.head
    #         new_list.head = new_data
    #         new_list.head.next = current_head
    #         # End insert at start part
    #         current = current.next
    #     return new_list

    # def reverse(llist): 
    #     # Alternative verbose solution
    #     prev = None
    #     node = llist.head
    #     while node: 
    #         keep = node.next
    #         node.next = prev
    #         prev = node
    #         node = keep
    #     llist.head = prev
    #     return llist


def make_from_list(list):
    llist = LinkedList()
    # Inserting at the start of linked lists is more efficient, but will reverse order. 
    # So traverse the input in opposite order to use this functionality
    for item in list[::-1]:
        llist.insert_start(item)
    return llist


if __name__ == '__main__':
    regular_list = ["Mon", "Tue", "Wed"]

    llist_manual = LinkedList()
    llist_manual.head = Node(regular_list[0])
    e2 = Node(regular_list[1])
    llist_manual.head.next = e2
    e3 = Node(regular_list[2])
    e2.next = e3
    items_manual = llist_manual.print()
    assert items_manual == regular_list

    list_insert_start = deepcopy(llist_manual)
    list_insert_start.insert_start("Fri")
    items_insert_start = list_insert_start.print()
    assert items_insert_start == ["Fri"] + regular_list

    list_insert_end = deepcopy(llist_manual)
    list_insert_end.insert("Fri")
    items_insert_end = list_insert_end.print()
    assert items_insert_end == regular_list + ["Fri"]

    llist_from_list = make_from_list(regular_list)
    items_from_list = llist_from_list.print()
    assert items_from_list == regular_list

    list_reversed = deepcopy(llist_manual).reverse()
    items_reversed = list_reversed.print()
    assert items_reversed == regular_list[::-1]
    print('Tests pased.')
