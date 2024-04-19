class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


# check for list(empty)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False


# push in stack
    def push(self,value):
        self.list.append(value)
        return "Element is succesfully pushed"
    
    
# pop in a stack
    def pop(self):
        if self.isEmpty():
            return "No element in the Stack"
        else:
            return self.list.pop()
        
        
# Peek in a stack
    def peek(self):
        if self.isEmpty():
            return "No element in the Stack"
        else:
            return self.list[len(self.list) -1]
        

# delete complete stack
    def delete(self):
        self.list = None
        return "Stack is deleted"
        
customStack = Stack()
customStack.push(40)
customStack.push(30)
customStack.push(20)
print(customStack)
print("New Line here")
customStack.pop()
print(customStack)
print("New Line here")
print(customStack.peek())
customStack.delete()