class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return repr(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__length = 0
    
    def __len__(self):
        return self.__length
    
    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        
        self.__length += 1 
    
    def appendleft(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        
        self.__length += 1

    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        value = self.current.value
        self.current = self.current.next
        
        return value    

    def pop(self):
        if self.tail is None:
           raise Exception('LinkedList is empty')
        
        target = self.tail.value
        self.tail = self.tail.prev
        self.tail.next = None
        self.__length -= 1
        return target
        

    def popleft(self):
        if self.head is None:
            raise Exception('LinkedList is empty')
        target = self.head.value
        self.head = self.head.next
        self.head.prev = None
        self.__length -= 1
        return target

    def remove(self, value):
        f = value.prev 
        r = value.next 
        f.next = r 
        r.prev = f 

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            
            prev = curr.prev
            curr.prev = curr.next
            curr.next = prev
            perv = curr
            curr = curr.prev
        if prev:
            self.head = prev
        return self
            
    def count(self, value):
        count = 0
        for item in self:
            if item == value:
                count += 1
        return count

    def __repr__(self):
        return repr(list(self))

ll = LinkedList()
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(1)
ll.append(2)
