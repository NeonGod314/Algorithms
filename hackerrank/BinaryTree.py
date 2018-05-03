class BinaryTree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None
        
    def getLeftChild(self):
        return self.left
    
    def setLeftChild(self, node):
        self.left = node
    
    def getRightChild(self):
        return self.right
    
    def setRightChild(self, node):
        self.right = node
    
    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def printInorder(self):
        if self.left != None:
            self.left.printInorder()
        print(self.data)
        if self.right != None:
            self.right.printInorder()
            
    def printPreorder(self):
        print(self.data)
        if self.left != None:
            self.left.printPreorder()
        if self.right != None:
            self.right.printPreorder()
            
    def printPostorder(self):
        if self.left != None:
            self.left.printPostorder()
        if self.right != None:
            self.right.printPostorder()
        print(self.data)
        
    def fromInorderPreorder(self, inorderList, preorderList):
        self.data = preorderList[0]
        i = inorderList.index(self.data)

        if len(inorderList[:i]) != 0:
            self.left = BinaryTree()
            self.left.fromInorderPreorder(inorderList[:i], preorderList[1:i+1])
        if len(inorderList[i+1:]) != 0:
            self.right = BinaryTree()
            self.right.fromInorderPreorder(inorderList[i+1:], preorderList[i+1:])
            
    def fromInorderPostorder(self, inorderList, postorderList):
        print(inorderList)
        print(postorderList)
        self.data = postorderList[-1]
        i = inorderList.index(self.data)
        
        if len(inorderList[:i]) != 0:
            self.left = BinaryTree()
            self.left.fromInorderPostorder(inorderList[:i], postorderList[:i])
            
        if len(inorderList[i+1:]) != 0:
            self.right = BinaryTree()
            self.right.fromInorderPostorder(inorderList[i+1:], postorderList[i:-1])
            