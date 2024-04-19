class Queue:
    def __init__(self,maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1
        
    def __str__(self):
        value = [str(x) for x in self.items]
        return " ".join(value)
    
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top +1 == self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            
    
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            firstElement  = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.sta = -1
                self.top = -1
            elif self.start +1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items[self.start]
        
        
customQueue = Queue(3)
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.isEmpty())
print(customQueue.isFull())
print(customQueue.peek())
