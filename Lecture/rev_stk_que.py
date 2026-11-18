class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data

    def display(self):
        temp = self.front
        print("Queue elements: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


class stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        temp = self.top
        val = temp.data
        print("Popped element: ", val)
        self.top = self.top.next
        return val

    def print(self):
        temp = self.top
        print("Stack elements...")
        while temp:
            print(temp.data)
            temp = temp.next

    def reverseString(self, s):
        temp_stack = stack()
        for ch in s:
            temp_stack.push(ch)

        rev = ""
        while not temp_stack.isempty():
            rev += temp_stack.pop()
        return rev


def reverse_stack(s1):
    q1 = Queue()
    while not s1.isempty():
        q1.enqueue(s1.pop())
    while not q1.is_empty():
        s1.push(q1.dequeue())


que = Queue()
que.enqueue(20)
que.enqueue(30)
que.enqueue(40)
que.enqueue(50)
que.enqueue(60)
que.display()

st = stack()
st.push(10)
st.push(100)
st.push(45)
st.push(78)
st.push(90)

st.print()
st.pop()
st.print()

print("Reversed:", st.reverseString("OMKAR"))