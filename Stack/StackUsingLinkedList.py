class Node:
    def __init__(self,value):
        self.value =value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
        
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()


    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

# Check for stack is empty
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
        

# push in a stack
    def push(self,value):
        node =Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
        
        
# pop in stack
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
        return nodeValue


    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            nodeValue = self.LinkedList.head.value
        return nodeValue


    def delete(self):
        self.LinkedList.head = None




customStack = Stack()

customStack.push(10)
customStack.push(20)
customStack.push(30)
# print(customStack)
# print(" ")
# customStack.pop()
print(customStack.peek())
# print(customStack)