class Element():
    
    def __init__(self, value):
        self.value = value 
        self.next = None

class List():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appendingElement(self,element:Element):
        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.tail = element
        self.length += 1 

    def __str__(self):
        current = self.head
        listOfValues = []
        listOfValues.append(current.value)
        while current.next != None:
            listOfValues.append(current.next.value)
            current = current.next
        return str(listOfValues)



el = Element(20)


li = List()
li.appendingElement(el)
el = Element(21)
li.appendingElement(el)

el = Element(22)
li.appendingElement(el)

el = Element(23)
li.appendingElement(el)

el = Element(24)
li.appendingElement(el)

print(li.tail.next)
print(li.length)
print(li)
    
    

    