from copy import deepcopy
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self): 
        self.head = None

    def print(self): 
        return 

    # def make_from_list(self,list): 
    #     for item in list: 
    #         self.insert_start(Node(item))

    def insert(self,data): 
        return
    
    def insert_start(self,data): 
        return

    def reverse(llist): 
        return     

if __name__ == '__main__':     
    regular_list = ["Mon","Tue","Wed"]

    llist_manual = LinkedList()
    llist_manual.head = Node(regular_list[0])
    e2 = Node(regular_list[1])
    llist_manual.head.next = e2
    e3 = Node(regular_list[2])
    e2.next = e3
    items_manual = llist_manual.print()
    assert items_manual == regular_list
    
    # llist_from_list = LinkedList()
    # llist_from_list.make_from_list(regular_list)
    # items_from_list = llist_from_list.print()
    # assert items_from_list == regular_list

    list_insert_start = deepcopy(llist_manual)
    list_insert_start.insert_start("Fri")
    items_insert_start = list_insert_start.print()
    assert items_insert_start == ["Fri"] + regular_list

    list_insert_end = deepcopy(llist_manual)
    list_insert_end.insert("Fri")
    items_insert_end = list_insert_end.print()
    assert items_insert_end == regular_list +["Fri"]

    list_reversed = deepcopy(llist_manual)
    list_reversed.reverse()
    items_reversed = list_reversed.print()
    assert items_reversed == regular_list[::-1]
    print('Tests pased.')