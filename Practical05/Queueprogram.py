import time

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def insert(self):
        if self.is_full():
            print("\nQueue Overflow! Cannot insert more elements.")
        else:
            item = input("Enter Element: ")
            self.queue.append(item)
            print(item, "inserted successfully")
            time.sleep(1)

    def delete(self):
        if self.is_empty():
            print("\nQueue Underflow! Queue is empty.")
        else:
            item = self.queue.pop(0)
            print("Deleted Element:", item)
            time.sleep(1)

    def traversal(self):
        if self.is_empty():
            print("\nQueue is Empty")
        else:
            print("\nQueue Elements are:")
            for i in self.queue:
                print(i)


size = int(input("Enter Queue Size: "))

q = Queue(size)

while True:
    print("\n----- Queue Menu -----")
    print("1. Insert")
    print("2. Delete")
    print("3. Traversal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        q.insert()

    elif choice == 2:
        q.delete()

    elif choice == 3:
        q.traversal()

    elif choice == 4:
        print("Program Exit")
        break

    else:
        print("Invalid Choice")
