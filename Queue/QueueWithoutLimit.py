class Queue:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        value = [str(x) for x in self.list]
        return ' '.join(value)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.list.append(value)
        return "The element is inserted at the end of queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list.pop(0)
        
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.list[0]

    def delete(self):
        self.list = None
        return "Queue is deleted"
     
     
     
CustomQueue = Queue()
CustomQueue.enqueue(1)
CustomQueue.enqueue(2)
CustomQueue.enqueue(3)
print(CustomQueue)
CustomQueue.dequeue()
print(CustomQueue)
print(CustomQueue.peek())
# print(CustomQueue)
print(CustomQueue.isEmpty())
print(CustomQueue.delete())
    
    