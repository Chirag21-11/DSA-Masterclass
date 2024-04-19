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


def PostOrderTraversal(rootNode):   #.............Time = O(n)  space = O(n)
    if not rootNode:
        return
    PostOrderTraversal(rootNode.leftChild)
    PostOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    

PostOrderTraversal(newBT)