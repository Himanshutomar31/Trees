class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printNodes(node):
    if node == None:
        return
    print(str(node.data) + "->", end="")
    if node.left != None:
        print(node.left.data, end="")
    if node.right != None:
        print(node.right.data, end="")
    print()

    printNodes(node.left)
    printNodes(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
printNodes(root)

#The maximum number of nodes at level ‘l’ of a binary tree is 2l.
#The Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1.
#In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is? Log2(N+1) ?


