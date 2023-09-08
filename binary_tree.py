class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftchild = None
        self.rightchild = None

    def insertLeft(self, value):
        if self.leftchild == None:
            self.leftchild = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t.leftchild = self.leftchild
            self.leftchild = t
    
    def insertRight(self, value):
        if self.rightchild == None:
            self.rightchild = BinaryTree(value)
        else:
            t = BinaryTree(value)
            t.rightchild = self.rightchild
            self.rightchild = t

    def getRightChild(self):
        return self.rightchild
    
    def getLeftChild(self):
        return self.leftchild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())