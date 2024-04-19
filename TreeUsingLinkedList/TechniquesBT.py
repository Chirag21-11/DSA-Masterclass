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



def SearchingBT(rootNode,nodeValue):           #.............Time = O(n)  space = O(n)
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Failed"



def insertNodeBT(rootNode,newNode):        #.............Time = O(n)  space = O(n)
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            node= customQueue.dequeue()
            if (node.value.leftChild is not None):
                customQueue.enqueue(node.value.leftChild)
            else:
                node.value.leftChild = newNode
                return "Successfully Inserted"
            if (node.value.rightChild is not None):
                customQueue.enqueue(node.value.rightChild)
            else:
                node.value.rightChild = newNode
                return "Successfully Inserted"
            



# Delete Node
def getDeepestNode(rootNode):      #..............Time = O(n)  Space = O(n)
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        DeepestNode = root.value
        return DeepestNode


def deleteDeepestNode(rootNode,DNode):       #..............Time = O(n)  Space = O(n)
    if rootNode is None:
        return
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.value is DNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild is DNode:
                    root.value.leftChild =  None
                    return
                else:
                    customqueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild is DNode:
                    root.value.rightChild =  None
                    return
                else:
                    customqueue.enqueue(root.value.rightChild)


def deleteNodeBT(rootNode,Node):          #..............Time = O(n)  Space = O(n)
    if rootNode is None:
        return
    else:
        customqueue=Queue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.value.data == Node:
                DNode = getDeepestNode(rootNode)
                root.value.data = DNode.data
                deleteDeepestNode(rootNode,DNode)
                return "The node is deleted bro"
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
        return "Failed to delete"
            

def deleteFullBT(rootNode):        #..............Time = O(1)  Space = O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild =None
    return "Whole Treee is Deleted....!"

print(deleteFullBT(newBT))
levelOrderTraversal(newBT)