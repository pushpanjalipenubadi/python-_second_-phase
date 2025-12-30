class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
class tree:
    def postorder(root):
        if root!=None:
            tree.postorder(root.left)
            tree.postorder(root.right)
            print(root.data,end=" ")
root=Node(10)
root.left=Node(20)
root.left.left=Node(40)
root.right=Node(30)
root.right.left=Node(50)
tree.postorder(root)
