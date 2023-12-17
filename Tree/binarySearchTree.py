class binarySearchTree:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = binarySearchTree(data)
        if data > self.key:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = binarySearchTree(data)
    
    def search(self, x):
        if self.key is None:
            print('Key is not found')
            return
        if self.key == x:
            print('key Found')
            return
        if x < self.key:
            if self.lchild:
                self.lchild.search(x)
            else:
                print('Key is not found')
        else:
            if x > self.key:
                if self.rchild:
                    self.rchild.search(x)
                else:
                    print('Key is not found')

    def preOrder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preOrder()
        if self.rchild:
            self.rchild.preOrder()

    def inOrder(self):
        if self.lchild:
            self.lchild.inOrder()
        print(self.key, end=" ")
        if self.rchild:
            self.rchild.inOrder()
    
    def postOrder(self):
        if self.lchild:
            self.lchild.postOrder()
        if self.rchild:
            self.rchild.postOrder()
        print(self.key, end=" ")

BST = binarySearchTree(50)
lst = [45,67,54,32,7,8,4,45]
for i in lst:
    BST.insert(i)
BST.search(100)
BST.preOrder()
print()
BST.inOrder()
print()
BST.postOrder()