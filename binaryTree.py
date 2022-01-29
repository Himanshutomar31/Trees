class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            queue = []
            queue.append(self.root)
            while len(queue) != 0:
                temp = queue.pop(0)
                if temp.left == None:
                    temp.left = newNode
                    break
                else:
                    queue.append(temp.left)
                if temp.right == None:
                    temp.right = newNode
                    break
                else:
                    queue.append(temp.right)



def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

tree = BinaryTree()
tree.insert(7)
tree.insert(11)
tree.insert(10)
tree.insert(15)
tree.insert(9)
tree.insert(8)

print("Inorder traversal before insertion:", end=" ")
inorder(tree.root)

key = 12
tree.insert(12)


print()
print("Inorder traversal after insertion:", end=" ")
inorder(tree.root)









