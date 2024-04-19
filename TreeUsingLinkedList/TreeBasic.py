class TreeNode:
    def __init__(self,data,children = []):
        self.data = data
        self.children = children
    
    def __str__(self,level = 0):
        ret = " " * level+str(self.data) + "\n"
        for child in self.children:
            ret+= child.__str__(level+1)
        return ret
    
    def addchild(self,TreeNode):
        self.children.append(TreeNode)
        
Tree = TreeNode('Drink',[])
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])
Cola = TreeNode('Cola',[])
Fanta = TreeNode('Fanta',[])
Tea = TreeNode('Tea',[])
coffee = TreeNode('Coffee',[])
Tree.addchild(cold)
Tree.addchild(hot)
cold.addchild(Cola)
cold.addchild(Fanta)
hot.addchild(Tea)
hot.addchild(coffee)
print(Tree)