import tkinter as tk
from tkinter import scrolledtext
import heapq

# ---------------- AVL TREE ----------------

class Node:
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None


class AVL:

    def insert(self, root, value):

        if root is None:
            return Node(value)

        if value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, x):

        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        output.insert(tk.END, f"Left Rotation on {x.value}\n")

        return y

    def right_rotate(self, y):

        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        output.insert(tk.END, f"Right Rotation on {y.value}\n")

        return x

    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right) if node else 0

    def preorder(self, root):
        if root:
            output.insert(tk.END, str(root.value) + " ")
            self.preorder(root.left)
            self.preorder(root.right)


# ---------------- BUTTON FUNCTION ----------------

def run_demo():

    output.delete("1.0", tk.END)

    output.insert(tk.END, "===== AVL TREE =====\n\n")

    tree = AVL()
    root = None

    values = [35, 18, 60, 10, 25, 50, 75, 5]

    for i in values:
        output.insert(tk.END, f"Inserting {i}\n")
        root = tree.insert(root, i)

    output.insert(tk.END, "\nPreorder Traversal:\n")
    tree.preorder(root)

    output.insert(tk.END, "\n\n\n===== MIN HEAP =====\n")

    numbers = [12, 7, 25, 3, 18, 9]

    minheap = numbers.copy()
    heapq.heapify(minheap)

    output.insert(tk.END, str(minheap) + "\n")

    output.insert(tk.END, "\n===== MAX HEAP =====\n")

    maxheap = [-i for i in numbers]
    heapq.heapify(maxheap)

    output.insert(tk.END, str([-i for i in maxheap]) + "\n")

    output.insert(tk.END, "\n===== PRIORITY QUEUE =====\n")

    pq = []

    heapq.heappush(pq, (3, "Send Email Reports"))
    heapq.heappush(pq, (1, "Attend Emergency Meeting"))
    heapq.heappush(pq, (2, "Complete Documentation"))
    heapq.heappush(pq, (4, "System Cleanup"))

    while pq:
        p, task = heapq.heappop(pq)
        output.insert(tk.END, f"Priority {p} : {task}\n")


# ---------------- GUI ----------------

root = tk.Tk()
root.title("AVL Tree, Heap and Priority Queue")
root.geometry("800x650")
root.configure(bg="#d9f2ff")

heading = tk.Label(
    root,
    text="AVL TREE | MIN HEAP | MAX HEAP | PRIORITY QUEUE",
    font=("Arial", 17, "bold"),
    bg="#003366",
    fg="white",
    pady=10
)

heading.pack(fill="x")

btn = tk.Button(
    root,
    text="Run Simulation",
    font=("Arial", 13, "bold"),
    bg="green",
    fg="white",
    command=run_demo
)

btn.pack(pady=10)

output = scrolledtext.ScrolledText(
    root,
    width=95,
    height=30,
    font=("Consolas", 10)
)

output.pack(padx=10, pady=10)

root.mainloop()
