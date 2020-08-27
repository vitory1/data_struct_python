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

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.key)


class Solution:
    def isSubStructure(self, A, B):
        def recur(A, B):
            if not B:
                return True
            if not A or A.key != B.key:
                return False
            return recur(A.leftChild, B.leftChild) and recur(A.rightChild, B.rightChild)
        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.leftChild, B) or self.isSubStructure(A.rightChild, B))


if __name__ == "__main__":
    etree1 = BinaryTree(3)
    etree1.insertLeft(4)
    etree1.insertRight(5)
    etree1.getLeftChild().insertLeft(1)
    etree1.getLeftChild().insertRight(2)

    etree2 = BinaryTree(4)
    etree2.insertLeft(1)

    s = Solution()
    print(s.isSubStructure(etree1, etree2))
