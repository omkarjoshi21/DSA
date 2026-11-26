# Delete
# Binary Search Tree
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                elif new_node.data > temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    def inorder(self, temp):  # Recursive
        if temp is None:
            return
        else:
            self.inorder(temp.left)
            print(temp.data, end=" ")
            self.inorder(temp.right)
    def del_node(self,rt,val):
            if rt is None:
                return rt
            if val<rt.data:
                rt.left=self.del_node(rt.left, val)
            elif val>rt.data:
                rt.right=self.del_node(rt.right, val)
            else:
                if rt.left is None:  #Node with right child only
                    return rt.right
                if rt.right is None:  #Node with left child only
                    return rt.left
                # Node having both left and right children
                succ=self.get_successor(rt)
                rt.data=succ.data
                rt.right=self.del_node(rt.right, succ.data)
                return rt
    def get_successor(self, temp):
        temp=temp.right
        while temp.left is not None:
            temp=temp.left
        return temp


btree = BST()
btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))
btree.inorder(btree.root)
btree.del_node(btree.root,2)
print("\n After Deletion: ", end=" ")
