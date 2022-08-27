import copy

class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self): 
        self.head = None

    def insert_end(self,new_val): 
        node = Node(new_val)
        if not self.head: 
            self.head = node
            return
        current = self.head
        while current.next: 
            current = current.next
        current.next = node
    
    def insert_start(self,new_val): 
        node = Node(new_val)
        new_node = node
        new_node.next = self.head
        self.head = new_node
    
    def print(self): 
        if not self.head: 
            print('Empty list.') 
            return
        current = self.head
        data = list()
        while current: 
            print(current.data)
            data.append(current.data)
            current = current.next
        return data

    def reverse(self):
        # initialize variables
        previous = None         # `previous` initially points to None
        current = self.head     # `current` points at the first element
        following = current.next    # `following` points at the second element

        # go till the last element of the list
        while current:
            current.next = previous # reverse the link
            previous = current      # move `previous` one step ahead
            current = following         # move `current` one step ahead
            if following:               # if this was not the last element
                following = following.next    # move `following` one step ahead

        self.head = previous
        return self
       
if __name__ == '__main__': 
    llist_manual = LinkedList()
    llist_manual.head = Node("Mon")
    e2 = Node("Tue")
    e3 = Node("Wed")
    llist_manual.head.next = e2
    e2.next = e3
    llist_manual.print()
    
    llist_insert_start = LinkedList()
    llist_insert_start.head = Node("Mon")
    llist_insert_start.insert_end("Tue")
    llist_insert_start.insert_end("Wed")
    llist_insert_start.print()

    llist_insert_end = LinkedList()
    llist_insert_end.head = Node("Wed")
    llist_insert_end.insert_start("Tue")
    llist_insert_end.insert_start("Mon")
    llist_returned = llist_insert_end.print()

    assert llist_returned == ['Mon','Tue','Wed']

    list_reverse = copy.deepcopy(llist_manual).reverse()
    llist_returned = list_reverse.print()
    assert llist_returned == ['Wed','Tue','Mon']

    print('Done.')

