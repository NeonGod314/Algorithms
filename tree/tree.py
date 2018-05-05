class node:
    def __init__(self):
        self.data  = None
        self.left  = None
        self.right = None

    #getters and setters
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def getdata(self):
        return self.data
    def setdata(self,value):
        self.data=value

    # constructing tree from given transversals 
    def inorderPreorder(self, inorder, preorder):
        self.data=preorder[0]
        i=inorder.index(self.data)
        if len(inorder[0:i]) != 0:
            self.left=node()
            self.left.inorderPreorder(inorder[0:i], preorder[1:i+1])
        if len(inorder[i+1:]) != 0:
            self.right=node()
            self.right.inorderPreorder(inorder[i+1:], preorder[i+1:])    

    def inorderPostorder(self, inorder, postorder):
        self.data=postorder[-1]
        i=inorder.index(self.data)
        if len(inorder[0:i]) != 0:
            self.left=node()
            self.left.inorderPostorder(inorder[0:i], postorder[0:i])
        if len(inorder[i+1:]) != 0:
            self.right=node()
            self.right.inorderPostorder(inorder[i+1:], postorder[i:-1])    

    #printing inorder, preorder and postorder transversal
    def inorder(self):
        if self.left != None:
            self.left.inorder()
        print(self.data), 
        if self.right != None:
            self.right.inorder()

    def preorder(self):
        print(self.data),
        if self.left != None:
            self.left.preorder() 
        if self.right != None:
            self.right.preorder()

    def postorder(self):
        if self.left != None:
            self.left.postorder() 
        if self.right != None:
            self.right.postorder()
        print(self.data),

    # inorder transversal using loop, stack    
    def inorderLoop(self):
        current=self
        s=[]
        while(1):
            if current is not None:
                s.append(current)
                current=current.left
            else:
                if len(s) > 0:
                    current=s.pop()
                    print(current.data),
                    current=current.right
                else:
                    break        

# main function                
root = node()

#tree construction from orders
inorder  = [9, 2, 5, 1, 6, 3, 7]
preorder = [1, 2, 9, 5, 3, 6, 7]
postorder= [9, 5, 2, 6, 7, 3, 1]

#root.inorderPreorder(inorder, preorder)
root.inorderPostorder(inorder,postorder)
print("Inorder traversal")
root.inorder()
print("\nPreorder traversal")
root.preorder()
print("\nPostorder traversal")
root.postorder()
print("\nInorder transversal using stack")
root.inorderLoop()


# test for inorder, preorder and postorder display