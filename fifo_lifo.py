class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
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
            print(self.head.value)
            self.head = self.head.next
            self.length -= 1
        else:
            print('Queue is empty')
    
    def size(self):
        print(f'Current length of the queue is {self.length}')
        
    def front(self):
        if self.head != None:
            print(f'Current front is {self.head.value}')
        else:
            print('Queue is empty')
    
    def __str__(self):
        listOfNodes = []
        if self.head == None:
            return 'Queue is empty :('
        else:
            current = self.head
            while current:
                listOfNodes.append(str(current.value))
                current = current.next
            return ', '.join(listOfNodes)
        
kolejka = Queue(Node(2))
kolejka.append_node(Node(3))
kolejka.append_node(Node(6))
print(kolejka)
kolejka.dequeue()
print(kolejka)

class Stack:
    def __init__(self, top : Node):
        self.bottom = top
        self.top = top
        self.top.previous = None
        self.length = 1
    
    def push_node(self, node : Node):
        if self.top == None:
            self.top = node
            self.top.previous = None
            self.bottom = node
            self.length += 1
        else:
            node.previous = self.top
            self.top.next = node
            self.top = node
            self.length += 1
            
    def pop_node(self):
        if self.top == None:
            print('Stack is empty')
        else:
            print(self.top.value)
            self.top = self.top.previous
            self.length -= 1
            
    def size(self):
        print(f'Current length of the stack is {self.length}')
            
    def __str__(self):
        if self.top == None:
            return 'Stack is empty'
        else:
            stackList = []
            current = self.top
            while current:
                stackList.append(str(current.value))
                current = current.previous
            return ', '.join(stackList)

stos = Stack(Node(1))
stos.push_node(Node(2))
stos.push_node(Node(3))
stos.push_node(Node(4))
stos.push_node(Node(5))
stos.push_node(Node(6)) 
stos.pop_node()    
print(stos)       
stos.size()
    
    