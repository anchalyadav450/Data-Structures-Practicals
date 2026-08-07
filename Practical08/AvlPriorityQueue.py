import heapq

# ----------------------------
# AVL Tree Implementation
# ----------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVL:

    def insert_node(self, root, value):

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert_node(root.left, value)
        else:
            root.right = self.insert_node(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        # Left Left
        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)

        # Right Right
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)

        # Left Right
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right Left
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_left(self, x):

        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        print("Left Rotation on", x.value)

        return y

    def rotate_right(self, y):

        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        print("Right Rotation on", y.value)

        return x

    def height(self, node):
        if node:
            return node.height
        return 0

    def balance(self, node):
        if node:
            return self.height(node.left) - self.height(node.right)
        return 0

    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)


# ----------------------------
# Min Heap
# ----------------------------

def show_min_heap(numbers):
    heap = numbers.copy()
    heapq.heapify(heap)
    print("\nMin Heap:", heap)


# ----------------------------
# Max Heap
# ----------------------------

def show_max_heap(numbers):
    heap = [-i for i in numbers]
    heapq.heapify(heap)

    result = [-i for i in heap]

    print("Max Heap:", result)


# ----------------------------
# Priority Queue Example
# ----------------------------

class PriorityTasks:

    def __init__(self):
        self.tasks = []

    def add(self, priority, work):
        heapq.heappush(self.tasks, (priority, work))

    def execute(self):

        print("\nTask Execution Order:")

        while self.tasks:
            p, job = heapq.heappop(self.tasks)
            print("Priority", p, ":", job)


# ----------------------------
# Main Program
# ----------------------------

if __name__ == "__main__":

    print("===== AVL TREE DEMO =====")

    tree = AVL()
    root = None

    values = [35, 18, 60, 10, 25, 50, 75, 5]

    for num in values:
        print("Inserting:", num)
        root = tree.insert_node(root, num)

    print("\nPreorder Traversal:")
    tree.preorder(root)

    print("\n\n===== HEAP DEMO =====")

    heap_data = [12, 7, 25, 3, 18, 9]

    show_min_heap(heap_data)
    show_max_heap(heap_data)

    print("\n\n===== PRIORITY QUEUE DEMO =====")

    scheduler = PriorityTasks()

    scheduler.add(3, "Send Email Reports")
    scheduler.add(1, "Attend Emergency Meeting")
    scheduler.add(2, "Complete Project Documentation")
    scheduler.add(4, "System Cleanup")

    scheduler.execute()
