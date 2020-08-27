class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def buildParseTree(self, fpexp):
        fplist = fpexp.split()
        pStack = []
        eTree = BinaryTree("")
        pStack.append(eTree)
        currentTree = eTree
        for i in fplist:
            if i == "(":
                currentTree.insertLeft("")
                pStack.append(currentTree)
                currentTree = currentTree.getLeftChild()
            elif i not in ["+", "-", "*", "/", ")"]:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            elif i in ["+", "-", "*", "/"]:
                currentTree.setRootVal(i)
                currentTree.insertRight("")
                pStack.append(currentTree)
                currentTree = currentTree.getRightChild()
            elif i == ")":
                currentTree = pStack.pop()
            else:
                raise ValueError
        return eTree
