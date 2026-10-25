class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        # Fixed: check if head is empty, otherwise traverse to find the last node
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        if pos == 1:  # inserting at first position
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head  # Fixed: initialized temp
            p = 1
            while temp and p != pos - 1:  # Fixed: added safety check for temp
                temp = temp.next  
                p = p + 1

            if temp:  # Fixed: ensure temp is not None before linking
                new_node.next = temp.next
                temp.next = new_node
    
    def print(self):
        temp = self.head
        while temp:
            __builtins__.print(temp.data)  # Fixed: used __builtins__.print to avoid recursion conflict with the method name
            temp = temp.next

list = LinkedList()
n1 = Node(10)
n2 = Node(20) 
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(55))
list.append(Node(48))
list.print()
list.insert(Node(100), 1)
list.print()
list.insert(Node(66), 7)
list.print()
list.insert(Node(99), 8)
list.print()