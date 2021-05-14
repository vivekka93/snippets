"""
A tree is a data structure consisting of nodes in a hierarchy
"""

class Node():
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data
    

"""
TREE TRAVERSAL
Tree traversal can be done primarily in two ways- breadth first search and depth first search
Depth first search can be done in three different ways- inorder, preorder and postorder traversal
Inorder traversal- left, root and then right
Preorder traversal- Root, left and then right
Postorder traversal- Left, right and then root
"""
def inorder(Tree):
    if Tree:
        inorder(Tree.getLeft())
        print(Tree.getData())
        inorder(Tree.getRight())
    return

def preorder(Tree):
    if Tree:
        print(Tree.getData())
        preorder(Tree.getLeft())
        preorder(Tree.getRight())
    return

def postorder(Tree):
    if Tree:
        postorder(Tree.getLeft())
        postorder(Tree.getRight())
        print(Tree.getData())
    return
