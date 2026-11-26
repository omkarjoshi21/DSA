# DSA Graded Assignment 25-11-2026 

# 1. Create a BST using product IDs.
# Insert the following product IDs:
# 150, 100, 200, 75, 125, 175, 250, 60, 90, 110.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data>root.data:
            root.right = self.insert(root.right, data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        return root

#2. Display product IDs in ascending order.

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

#3. Search for product ID 175 exists.

    def search(self,root,key):
        if root is None:
            return False
        if root.data==key:
            return True
        if key<root.data:
            return self.search(root.left,key)
        return self.search(root.right,key)
    

#5.Display the BST using inorder, preorder, and postorder traversals.

    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)
            
    def preorder(self, root):
        if root is not None:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")


#6. Find the minimum and maximum product IDs.

    def minimum(self,root):
        while root.left:
            root=root.left
        return root.data

    def maximum(self,root):
        while root.right:
            root=root.right
        return root.data


obj=BST()
root = None 
root= obj.insert(root, 150)
root= obj.insert(root, 100)
root= obj.insert(root, 200)
root= obj.insert(root, 75)
root= obj.insert(root, 125)
root= obj.insert(root, 175)
root= obj.insert(root, 250)
root= obj.insert(root, 60)
root= obj.insert(root, 90)
root= obj.insert(root, 110)

print("Ascending order= ")
obj.inorder(root)
print()

print("\nProduct id 175 =")
print(obj.search(root,175))

print("Inorder= ")
obj.inorder(root)
print()

print("Preorder= ")
obj.preorder(root)
print()

print("Postorder= ")
obj.postorder(root)
print()

print("Minimum= ")
print(obj.minimum(root))

print("Maximum= ")
print(obj.maximum(root))
