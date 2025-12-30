class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class tree:
    def inorder(root):
        if root!=None:
            tree.inorder(root.left)
            print(root.data,end=" ")
            tree.inorder(root.right)
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
tree.inorder(root)
