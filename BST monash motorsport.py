test_loop_count = 0

class binarynode: #
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
    global test_loop_count
    test_loop_count += 1
    if root is None: #if the first node is empty
        root = binarynode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    elif newValue > root.data:
        root.rightChild = insert(root.rightChild, newValue)
    return root
#The worst case scenario is O(n) because it calls itself n times

def search(root, value):
    global test_loop_count
    test_loop_count += 1
    if root is None:
        return False
    elif root.data == value:
        return True
    elif root.data > value:
        return search(root.leftChild, value)
    else:
        return search(root.rightChild, value)

def minValueNode(node):
    global test_loop_count
    test_loop_count += 1
    current = node
    while current.leftChild is not None:
        current = current.leftChild
 
    return current
 

def delete(root, key):
    global test_loop_count
    test_loop_count += 1
    if root is None:
        return root
    if key < root.key:
        root.left = delete(root.leftChild, key)
    elif key > root.key:
        root.right = delete(root.rightChild, key)
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

        root.rightChild = delete(root.rightChild, temp.key)
 
    return root

# Create binary tree
word_list = ["a", "b", "c"]
root = None
for w in word_list:
    root = insert(root, w)

#worst case: when all elements are in ascending/decending order therefore form a straight line in the bST

# Testing for insert
test_loop_count = 0
root = insert(root, "d")
print (test_loop_count)

test_loop_count = 0
root = search(root, "c")
print (test_loop_count)

test_loop_count = 0
root = delete(root, "c")
print (test_loop_count)
