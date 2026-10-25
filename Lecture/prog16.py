class LinkedList:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

    def append(self, new_node):
        self.head=new_node

    def insert(self, new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

        else:
            p=1
            while(p!=pos-1):
                temp=temp.next
                p+=1
            temp.next=new_node
            new_node.prev=temp
            new_node.next=temp.next
            if temp.next:
                temp.next.prev=new_node
    
    def print(self):
        temp=self.head
        print("\nlist elements :", end=" ")
        while temp:
            print(temp.data)
            print=temp.next
    

list1=LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.append(Node(78))
list1.print()
list1.insert(Node(5),4)
