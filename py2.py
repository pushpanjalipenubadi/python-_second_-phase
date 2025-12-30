class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def preorder(root):
        if root!=None:
            print(root.data,end=" ")
            tree.preorder(root.left)
            tree.preorder(root.right)
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
tree.preorder(root)
