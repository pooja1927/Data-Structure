class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None

class DLL:
    def __init__(self):
        self.head = None

    def printData(self):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.nref

    def printDataReverse(self):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.pref
            
    def addBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.nref = n
            n.pref = new_node
            self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def afterNode(self, data, x):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.data is not x:
                n = n.nref
            new_node.pref = n
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node

    def beforeNode(self, data, x):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref.data is not x:
                n = n.nref
            new_node.pref = n
            new_node.nref = n.nref
            n.nref = new_node
            n.nref.pref = new_node
            
    def deleteBegin(self):
        if self.head is None:
            print('Linked List is empty we cannot delete!')
        else:
            n = self.head
            n.pref = None
            self.head = n.nref

    def deleteEnd(self):
        if self.head is None:
            print('Linked List is empty we cannot delete!')
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            n.nref = None

    def deleteInbetween(self, x):
        if self.head is None:
            print('Linked List is empty we cannot delete!')
        else:
            n = self.head
            while n.nref.data is not x:
                n = n.nref
            n.nref.pref = n
            n.nref = n.nref.nref
            

LL = DLL()
LL.addBegin(10)
LL.addBegin(20)
LL.printData()
print('\nAdd 12 at the end of linked list')
LL.addEnd(12)
LL.printData()
print('\nAdd 25 after 10')
LL.afterNode(25, 10)
LL.printData()
print('\nAdd 45 before 12')
LL.beforeNode(45, 12)
LL.printData()
print('\nDelete first node')
LL.deleteBegin()
LL.printData()
print('\nDelete last node')
LL.deleteEnd()
LL.printData()
print('\nDelete node 25')
LL.deleteInbetween(25)
LL.printData()