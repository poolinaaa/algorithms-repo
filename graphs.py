
from fifo_lifo import Stack, Queue

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self):
        return self.value
        
class BinaryTree:
    def __init__(self, root : Node = None):
        self.root = root
        
    def append(self, node : Node):
        
        if self.root == None:
            self.root = node
        else:
            current = self.root
            queue_nodes = Queue(self.root)
            while current:
                if current.left != None:
                    queue_nodes.append_node(current.left)
                else:
                    node.parent = current
                    current.left = node
                    break
                if current.right != None:
                    queue_nodes.append_node(current.right)
                else:
                    current.right = node
                    node.parent = current
                    break
                current = queue_nodes.dequeue()
                
tree = BinaryTree(Node(1))
tree.append(Node(2))
tree.append(Node(3))
tree.append(Node(4))
print(f'VALUE {tree.root.left.left.value}')
                


       
