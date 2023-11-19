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
        self.length = 1
    
    def append_node(self, node : Node):
        if self.tail == None:
            self.head = node
            self.tail = node
            self.length += 1
        else:
            self.tail.next = node
            self.tail = node
            self.length += 1
    
    def dequeue(self):
        if self.head != None:
            print(self.head)
            self.head = self.head.next
            self.length -= 1
        else:
            print('Queue is empty')
    
    def size(self):
        print(f'Current length of the queue is {self.length}')
    
    def __str__(self):
        listOfNodes = []
        if self.head == None:
            return 'Queue is empty :('
        else:
            current = self.head
            while current:
                listOfNodes.append(current.value)
                current = current.next
            return ', '.join(listOfNodes)
        