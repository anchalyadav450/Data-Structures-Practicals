# Aim: Implement Doubly Linked List with various operations


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp


    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            self.insert_at_beginning(data)
            return

        temp = self.head

        for i in range(position - 1):
            temp = temp.next

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node


    def delete_at_beginning(self):

        if self.head is not None:
            self.head = self.head.next

            if self.head:
                self.head.prev = None


    def delete_at_end(self):

        if self.head is None:
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None


    def delete_at_position(self, position):

        temp = self.head

        for i in range(position):
            temp = temp.next

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev


    def display(self):

        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


    def search(self, data):

        temp = self.head

        while temp:
            if temp.data == data:
                return True

            temp = temp.next

        return False


    def length(self):

        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        return count



# Main Program

dll = DoublyLinkedList()

dll.insert_at_beginning(20)
dll.insert_at_beginning(10)
dll.insert_at_end(30)
dll.insert_at_end(40)

print("Doubly Linked List:")
dll.display()

dll.insert_at_position(25, 2)

print("After inserting 25 at position 2:")
dll.display()

dll.delete_at_beginning()

print("After deleting first node:")
dll.display()

dll.delete_at_end()

print("After deleting last node:")
dll.display()

print("Search 30:", dll.search(30))

print("Length of List:", dll.length())
