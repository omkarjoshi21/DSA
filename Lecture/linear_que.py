class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
class LinearQueue:
    def __init__(self):
        self.front=self.rear=None
    
    def enqueue (self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
        
    def dequeue(self):
        temp=self.front
        print("Deleted node is:",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Queue is empty")
            self.rear=None
        temp=None

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end=" ->")
            temp=temp.next
        print()

queue = LinearQueue()
queue.enqueue(Node(13))
queue.enqueue(Node(25))
queue.enqueue(Node(37))
queue.enqueue(Node(49))
queue.print()
queue.dequeue()