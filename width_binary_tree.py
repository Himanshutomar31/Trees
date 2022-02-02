from binaryTree import BinaryTree


def width_binary_tree(root, h, lst):
    if root == None:
        return
    lst[0] = min(lst[0],h)
    lst[1] = max(lst[1],h)
    width_binary_tree(root.left, h-1, lst)
    width_binary_tree(root.right, h+1, lst)


tree = BinaryTree()
tree.insert(7)
tree.insert(11)
tree.insert(10)
tree.insert(15)
tree.insert(9)
tree.insert(8)
lst = [0,0]
width_binary_tree(tree.root, 0, lst)
res = abs(lst[0]) + lst[1] + 1
print(res)
