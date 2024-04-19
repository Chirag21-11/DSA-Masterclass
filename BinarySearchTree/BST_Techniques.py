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
        
    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next 
            
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


class BSTNode:
    def __init__(self,data):   
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
def insertNode(rootNode,nodeValue):      #..............Time = O(log(n))  Space = O(log(n))
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Node is inserted"
    
    
def preOrderTraversal(rootValue):          #..............Time = O(n)  Space = O(n)
    if rootValue is None:
        return
    print(rootValue.data)
    preOrderTraversal(rootValue.leftChild)
    preOrderTraversal(rootValue.rightChild)   
    
    
def inOrderTraversal(rootValue):          #..............Time = O(n)  Space = O(n)
    if rootValue is None:
        return
    inOrderTraversal(rootValue.leftChild)
    print(rootValue.data)
    inOrderTraversal(rootValue.rightChild) 
    
    
def postOrderTraversal(rootValue):          #..............Time = O(n)  Space = O(n)
    if rootValue is None:
        return
    postOrderTraversal(rootValue.leftChild)
    postOrderTraversal(rootValue.rightChild) 
    print(rootValue.data)
    


def levelOrderTraversal(rootNode):            #..............Time = O(n)  Space = O(n)
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        
            
def searchingNode(rootNode,NodeValue):               #..............Time = O(log(n))  Space = O(log(n))
    if rootNode.data == NodeValue:
        print("Value is found")
    elif NodeValue <  rootNode.data:
        if rootNode.leftChild.data == NodeValue:
            print("Value is Found")
        else:
            searchingNode(rootNode.leftChild,NodeValue)
    else:
        if rootNode.rightChild.data ==NodeValue:
            print("value if found")
        else:
            searchingNode(rootNode.rightChild,NodeValue)        


def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current= current.leftChild
    return current


def deleteNode(rootNode,NodeValue):
    if rootNode is None:
        return rootNode
    if NodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,NodeValue) 
    elif NodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,NodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data) 
    return rootNode



newBST = BSTNode(None) 
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
# preOrderTraversal(newBST)
# print("......................................")
# inOrderTraversal(newBST)
# print("......................................")
# postOrderTraversal(newBST)
# print("......................................")
# searchingNode(newBST,30)
deleteNode(newBST,100)
levelOrderTraversal(newBST)
