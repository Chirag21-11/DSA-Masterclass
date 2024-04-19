class BinaryTree:
    def __init__(self,size):               #..............Time = O(1)  Space = O(1)
        self.customlist = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size
        
newBT= BinaryTree(8)