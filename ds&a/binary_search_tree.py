"""
Binary Search tree consists of node being greater than or equal to the left sub tree, and less than or equal to the right sub tree
There should not be any duplicates in the tree

"""
class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        """
        Method to insert a new node into the existing binary search tree
        """
        if self.data == data:
            return False
        elif data < self.data:
            # Since input data is less than node data, the new node is placed in the left sub tree
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            # Since data is greater than the node data, new node is inserted in the right sub tree
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True

    def minValueNode(self, node):
        """
        Given a node, return the node containing minimum value in its subtree
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def maxValueNode(self, node):
        """
        Given a node, return the node containing maximum value in its subtree
        """
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def delete(self, data, root):
        if self is None:
            return None
        if data < self.data:
            self.left = self.left.delete(data, root)
        elif data > self.data:
            self.right = self.right.delete(data, root)
        else:
            # deleting node with one child only
            if self.left is None:
                if self == root:
                    temp = self.minValueNode(self.right)
                    self.data = temp.data
                    self.right = self.right.delete(temp.data, root)
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                if self == root:
                    temp = self.maxValueNode(self.left)
                    self.data = temp.data
                    self.left = self.left.delete(temp.data, root)
                temp = self.left
                self = None
                return temp
            # Deleting node with two children
            # Get the inorder successor and then delete
            temp = self.minValueNode(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data, root)
        return self
    
    def find(self, data):
        """
        Checks if the given data value is present in the tree
        """
        if data == self.data:
            return True
        elif data < self.data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    
    def preorder(self):
        """
        Preorder traversal of bst
        """
        if self:
            print(str(self.data))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def inorder(self):
        """
        Inorder traversal of bst
        """
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data))
            if self.right:
                self.right.inorder()
    
    def postorder(self):
        """
        Postorder traversal of bst
        """
        if self:
            if self.left:
                self.left.inorder()
            if self.right:
                self.right.inorder()
            print(str(self.data))

"""
Binary Tree implementation
"""
class Tree():
    def __init__(self) -> None:
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data, self.root)
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            self.root.preorder()
    
    def inorder(self):
        if self.root is not None:
            self.root.inorder()
    
    def postorder(self):
        if self.root is not None:
            self.root.postorder()

"""
Example implementation
"""
if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)

    tree.preorder()
    tree.postorder()

    tree.delete(10)