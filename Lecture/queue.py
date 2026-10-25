# Queue
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class LQueue:
    def __init__(self):
        self.front=self.rear=None
    def enqueue(self, new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        temp=self.front
        print("Deleted Node :",temp.data)
        self.front=self.front.next
        if self.front==None: # If there is only one node
            print("Queue Is Empty")
            self.rear=None
        temp=None
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
que=LQueue()
que.enqueue(Node(1))
que.enqueue(Node(2))
que.enqueue(Node(3))
que.enqueue(Node(4))
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()
que.dequeue()
que.print()