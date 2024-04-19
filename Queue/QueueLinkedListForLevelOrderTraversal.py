class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        

            
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
        
        
    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.linkedList.head == None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
            
            
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        else:
            return False           
            
            
    def dequeue(self):
        if self.linkedList.head == None:
            return "Queue is empty"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head =None
                self.linkedList.tail = None
            else:   
                self.linkedList.head = self.linkedList.head.next
            return tempNode 
        
        
        
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.linkedList.head
            
            
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None
            
            
            
customQueue = Queue()
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.peek())
        
        
        