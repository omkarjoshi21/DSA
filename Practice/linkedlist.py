class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# class Linkedlist:
#     def __init__(self):
#         self.head=None
node1=Node(10)
node2=Node(20)
node3=Node(30)

node1.next=node2
node2.next=node3

cur=node1
while cur is not None:
    print(cur.data, end="->")
    cur=cur.next
