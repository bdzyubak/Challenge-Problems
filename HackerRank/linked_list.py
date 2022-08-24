
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self): 
        self.head = None

    def insert(self,data): 
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        
        current = self.head
        while current.next: 
            current = current.next
        current.next = new_node
    
    def insert_start(self,data): 
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    
    def print(self): 
        if not self.head: 
            print('Empty list.') 
            return
        current = self.head
        while current: 
            print(current.data)
            current = current.next

    def reverse(llist): 
        prev = None
        node = llist.head
        while node: 
            keep = node.next
            node.next = prev
            prev = node
            node = keep
        llist.head = prev
        return llist

    def reverse_constructor(llist): 
        node = Node(llist.data,None)
        while node.next: 
            node = Node(node.next.data,node)
        

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
    llist_insert_start.insert("Tue")
    llist_insert_start.insert("Wed")
    llist_insert_start.print()

    llist_insert_end = LinkedList()
    llist_insert_end.head = Node("Wed")
    llist_insert_end.insert_start("Tue")
    llist_insert_end.insert_start("Mon")
    llist_insert_end.print()