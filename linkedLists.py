class Element():
    
    def __init__(self, value):
        self.value = value 
        self.next = None

class List():
    
    def __init__(self, head : Element):
        self.head = head
        self.length = 0

    def appendingElement(self,element:Element):
        if self.head == None:
            self.head = element
            
        else:
            curr = self.head
            while True:
                if curr.next == None:
                    curr.next = element
                    break
                else:
                    curr = curr.next
        self.length += 1 

    def __str__(self):
        current = self.head
        listOfValues = []
        listOfValues.append(current.value)
        while current.next != None:
            listOfValues.append(current.next.value)
            current = current.next
        return str(listOfValues)




    
    
li = List(Element(2))
li.appendingElement(Element(5))
print(li)
    