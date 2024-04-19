class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize= size
        
    def insertNode(self,value):             #..............Time = O(1)  Space = O(1)
        if self.lastUsedIndex+1 == self.maxSize:
            return "Binary Tree is Full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex +=1
        return (f"The Node value :{value} is inserted")
    
    
    def searchingNode(self,value):           #..............Time = O(n)  Space = O(n)
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return "Success"
        return "Not Found"
    
    
    
    
    def preOrderTraversal(self,index):      #..............Time = O(n)  Space = O(n)
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 +1)
        
        
        
        
    def inorderTraversal(self,index):         #..............Time = O(n)  Space = O(n)
        if index > self.lastUsedIndex:
            return 
        self.inorderTraversal(index*2)
        print(self.customList[index])
        self.inorderTraversal(index*2 +1)
    
    
    
    def postOrderTraversal(self,index):         #..............Time = O(n)  Space = O(n)
        if index > self.lastUsedIndex:
            return 
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 +1)
        print(self.customList[index])
    
    
    
    def levelOrderTraversal(self,index):         #..............Time = O(n)  Space = O(1)
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])
        
        
        
        
    def deleteNode(self,value):             #..............Time = O(n)  Space = O(1)
        if self.lastUsedIndex == 0:
            return
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return "The node is deleted"
                
        
    def deleteBT(self):                   #..............Time = O(1)  Space = O(1)
        self.customList =None
        return "Binary Tree is deleted"
        
        
newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")

# newBT.inorderTraversal(1)
# print("..............New Line..........")
# newBT.postOrderTraversal(1)

print(newBT.deleteNode("Hot"))
newBT.levelOrderTraversal(1)
print(newBT.deleteBT())