class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create_list(self, values):
        for value in values:
            self.add_last(value)

    def add_last(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # 2. Traverse and Print Node Values
    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert Node at Specific Position
    def insert(self, data, pos):
        new_node = Node(data)

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 4. Find Middle Node
    def middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)

    # 5. Delete Node at Specific Position
    def delete(self, pos):
        if self.head is None:
            print("List is empty")
            return

        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        count = 1

        while temp.next is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # 6. Reverse Linked List
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # 7. Sum Every Two Consecutive Nodes
    def sum(self):
        temp = self.head

        if temp is None or temp.next is None:
            print("Two nodes required")
            return

        while temp is not None and temp.next is not None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next


list1 = LinkedList()

list1.create_list([10, 20, 30, 40, 50])
list1.display()

list1.insert(25, 3)
list1.display()

list1.middle()

list1.delete(2)
list1.display()

list1.reverse()
list1.display()

list1.sum()