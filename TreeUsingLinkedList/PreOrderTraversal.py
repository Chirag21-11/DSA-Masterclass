class TreeNode:
    def __init__(self,data):
        self.data = data
        self.rightChild = None
        self.leftChild = None
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTraversal(rootNode):     #.............Time = O(n)  space = O(n)
    if not rootNode:
        return 
    else:
        print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
preOrderTraversal(newBT)