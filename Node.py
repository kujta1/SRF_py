class Node(object):
    def __init__(self):
        self.isLeaf=True
        self.leftChild=None
        self.rightChild=None
        
    def addLeftChild(self,leftNode):
        self.leftChild=leftNode
        self.isLeaf=False
    def addRightChild(self,rightNode):
        self.rightChild=rightNode
    