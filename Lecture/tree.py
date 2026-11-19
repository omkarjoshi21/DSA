#Binary Search Tree
class Node:
    def __init__(self, value):
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self, new_node):
        if self.root is None:
            self.root=new_node
            return
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data:
                    if temp.left is None:
                        temp.left=new_node
                    else:
                        temp=temp.left