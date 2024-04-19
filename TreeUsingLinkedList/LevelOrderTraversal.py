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




class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild





def levelOrderTraversal(rootNode):      #..............Time = O(n)  Space = O(n)
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
                
levelOrderTraversal(newBT)
        