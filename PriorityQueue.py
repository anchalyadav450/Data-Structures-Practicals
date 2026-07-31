class PriorityQueue:

    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, item, priority):
        if self.is_full():
            print("Queue is Full.")
            return

        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
        print(item, "Inserted Successfully.")

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty.")
            return

        item = self.queue.pop(0)
        print(item[0], "Removed Successfully.")

    def display(self):
        if self.is_empty():
            print("Queue is Empty.")
            return

        print("\nPriority Queue")
        print("-------------------------")
        print("Item\tPriority")
        print("-------------------------")

        for item, priority in self.queue:
            print(item, "\t", priority)

    def highest(self):
        if self.is_empty():
            print("Queue is Empty.")
        else:
            print("Highest Priority Item :", self.queue[0][0])

    def lowest(self):
        if self.is_empty():
            print("Queue is Empty.")
        else:
            print("Lowest Priority Item :", self.queue[-1][0])


def main():

    size = int(input("Enter Queue Capacity : "))
    pq = PriorityQueue(size)

    while True:

        print("\n===== Priority Queue =====")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Check Empty")
        print("5. Check Full")
        print("6. Highest Priority")
        print("7. Lowest Priority")
        print("8. Exit")

        choice = int(input("Enter Choice : "))

        if choice == 1:
            item = input("Enter Item : ")
            priority = int(input("Enter Priority : "))
            pq.enqueue(item, priority)

        elif choice == 2:
            pq.dequeue()

        elif choice == 3:
            pq.display()

        elif choice == 4:
            if pq.is_empty():
                print("Queue is Empty.")
            else:
                print("Queue is Not Empty.")

        elif choice == 5:
            if pq.is_full():
                print("Queue is Full.")
            else:
                print("Queue is Not Full.")

        elif choice == 6:
            pq.highest()

        elif choice == 7:
            pq.lowest()

        elif choice == 8:
            print("Program Closed.")
            break

        else:
            print("Invalid Choice.")


if __name__ == "__main__":
    main()
