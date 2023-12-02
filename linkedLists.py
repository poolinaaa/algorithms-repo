class Element():

    def __init__(self, value):
        self.value = value
        self.next = None


class List():

    def __init__(self, head: Element):
        self.head = head
        self.length = 0

    def append_element(self, element: Element):
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

    def reverse_list(self):
        if self.length == 0 or self.length == 1:
            pass
        else:
            nextTb = None
            curr = self.head
            while True:
                prev = curr.next
                curr.next = nextTb
                nextTb = curr
                if prev == None:
                    self.head = curr
                    break
                else:
                    curr = prev

    def __str__(self):
        current = self.head
        listOfValues = []
        listOfValues.append(current.value)
        while current.next != None:
            listOfValues.append(current.next.value)
            current = current.next
        return str(listOfValues)


li = List(Element(2))
li.append_element(Element(5))
li.append_element(Element(6))
li.append_element(Element(7))
li.append_element(Element(8))

print(li)
li.reverse_list()
print(li)
