from random import randint

class Node:
    data = None
    next = None

    def __init__(self,data):
        self.data = data
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        cur = self.head
        while cur != None:
            yield cur.data
            cur = cur.next

    def __str__(self):
        values = [str(x) for x in self]
        return '->'.join(values)
    
    def __len__(self):
        length = 0
        for _ in self:
            length += 1
        return length
    
    def add(self,value):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_to_front(self,value):
        node = Node(value)
        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

    def generate(self,count,min,max):
        for _ in range(count):
            self.add(randint(min,max))
    


