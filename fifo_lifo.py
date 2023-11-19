class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return self.value
        
class Queue:
    def __init__(self, head : Node):
        self.head = head
        self.tail : Node = head
    
    def append_node(self, node : Node):
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.head != None:
            print(self.head)
            self.head = self.head.next
        else:
            print('Queue is empty')
    
    def size(self):
        pass
    
    def __str__