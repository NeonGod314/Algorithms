from BinaryTree import BinaryTree

bt = BinaryTree()
bt.fromInorderPostorder([5, 10, 15, 20, 30, 35], [5, 15, 10, 35, 30, 20])
#bt.setData(20)
#bt.setLeftChild(BinaryTree())
#bt.setRightChild(BinaryTree())
#bt.getLeftChild().setData(10)
#bt.getRightChild().setData(30)
#bt.getLeftChild().setLeftChild(BinaryTree())
#bt.getLeftChild().setRightChild(BinaryTree())
#bt.getRightChild().setLeftChild(BinaryTree())
#bt.getRightChild().setRightChild(BinaryTree())
#bt.getLeftChild().getLeftChild().setData(5)
#bt.getLeftChild().getRightChild().setData(15)
#bt.getRightChild().getLeftChild().setData(25)
#bt.getRightChild().getRightChild().setData(35)
bt.printInorder()
bt.printPreorder()
bt.printPostorder()