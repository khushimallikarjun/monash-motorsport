class binarysearchtree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
       if root is None:
        root = binarysearchtree(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

def search(root, value):
    if root is None:
        return False
    elif root.data == value:
        return True
    elif root.data > value:
        return search(root.leftChild, value)
    else:
        return search(root.rightChild, value)

def minValueNode(node):
    current = node
    while current.leftChild is not None:
        current = current.leftChild
 
    return current
 

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.leftChild, key)
    elif(key > root.key):
        root.right = deleteNode(root.rightChild, key)
    else:
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
 
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
 
        temp = minValueNode(root.rightChild)

        root.key = temp.key

        root.rightChild = deleteNode(root.rightChild, temp.key)
 
    return root
