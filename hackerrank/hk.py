class binarytree():

    def __init__(self):
        self.right=None
        self.left=None
        self.rootid=None

    def getleftchild(self):
        return self.right
    def getrightchild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getnodevalue(self):
        return self.rootid
    def insertrightchild(self,node):
        self.right=node
    def insertleftchild(self,node):
        self.left=node    
    def inorder(self):
        if self!=None:
            if self.left != None:
                self.left.inorder()
            print(self.rootid)
            if self.right != None:
                self.right.inorder()

    def printInorder(self):
        if self.left != None:
            self.left.printInorder()
        print(self.rootid)
        if self.right != None:
            self.right.printInorder()            

    def printPreorder(self):
        print(self.rootid)
        if self.left != None:
            self.left.printPreorder()
        if self.right != None:
            self.right.printPreorder()

    
    
    def inorderloop(self):
        current=self
        s=[]                
        while(1):
            if current!=None:
                s.append(current)
                current=current.left

            else:
                if len(s)>0:
                    current=s.pop() 
                    print(current.rootid)
                    current=current.right
                else:
                    break    

    def preorder(self):
        print(self.rootid)
        if self.left!=None:
           self.left.preorder()
        if self.right!=None:    
           self.right.preorder()
    def postorder(self,node):
        if node!=None:
            self.postorder(node.left)
            self.postorder(node.right) 
            print(node.rootid)         
    #from inorder and preorder
    def inorderpreorder(self,inorder,preorder):
        self.rootid=preorder[0]
        i=inorder.index(self.rootid)
        #print(inorder)
        #print(preorder)
        print(self.rootid)
        if len(inorder[0:i]) != 0:
            self.left=binarytree()
            self.left.inorderpreorder(inorder[0:i],preorder[1:i+1])
            #print(self.data)
        if len(inorder[i+1:]) != 0:
            self.right=binarytree()
            self.right.inorderpreorder(inorder[i+1:],preorder[i+1:])    
            #print(self.data)

    def inorderpostorder(self,inorder,postorder):
            self.rootid=postorder[-1]
            i = inorder.index(self.rootid)
            if len(inorder[0:i])!=0:
                self.left=binarytree()
                self.left.inorderpostorder(inorder[0:i], postorder[0:i])
            if len(inorder[i+1:])!=0:
                self.right=binarytree()
                self.right.inorderpostorder(inorder[i+1:0],postorder[i:-1])                
bt=binarytree()
inorder   = [1, 2, 3, 4, 6, 7]
preorder  = [4, 2, 1, 3, 6, 7]
postorder = [1, 3, 2, 7, 6, 4]
#bt.inorderpreorder(inorder,preorder)
#bt.inorderpostorder(inorder,postorder)
bt.setNodeValue(1)
x=bt.left
x.setNodeValue(2)
bt.left.setNodeValue(2)
#bt.right.setNodeValue(3)
#bt.left.left.setNodeValue(4)
#bt.left.right.setNodeValue(5)
print("\n")
#bt.inorder()
print("**")
#bt.preorder()
print("***")
#print(bt.postorder(bt))
#bt.printInorder()
bt.inorderloop()

