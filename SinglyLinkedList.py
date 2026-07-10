# Singly Linked List Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    # Insert at position
    def insert_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    # Delete by value
    def delete_value(self, data):
        temp = self.head
        previous = None

        while temp:

            if temp.data == data:
                if previous is None:
                    self.head = temp.next
                else:
                    previous.next = temp.next

                print("Node deleted")
                return

            previous = temp
            temp = temp.next

        print("Value not found")


    # Delete by position
    def delete_position(self, position):

        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.head = self.head.next
            print("Node deleted")
            return

        temp = self.head

        for i in range(position-1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
        print("Node deleted")


    # Traversal
    def display(self):

        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        print("Linked List:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")



def menu():

    print("\n===== Singly Linked List =====")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete by Value")
    print("5. Delete by Position")
    print("6. Display List")
    print("7. Exit")


def main():

    list1 = SinglyLinkedList()

    while True:

        menu()

        choice = int(input("Enter choice: "))


        if choice == 1:
            value = int(input("Enter value: "))
            list1.insert_beginning(value)


        elif choice == 2:
            value = int(input("Enter value: "))
            list1.insert_end(value)


        elif choice == 3:
            value = int(input("Enter value: "))
            pos = int(input("Enter position: "))
            list1.insert_position(value, pos)


        elif choice == 4:
            value = int(input("Enter value to delete: "))
            list1.delete_value(value)


        elif choice == 5:
            pos = int(input("Enter position to delete: "))
            list1.delete_position(pos)


        elif choice == 6:
            list1.display()


        elif choice == 7:
            print("Program Ended")
            break


        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
