from tkinter import *
from tkinter import messagebox

class PriorityQueue:
    def __init__(self, size):
        self.size = size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def enqueue(self, item, priority):
        if self.is_full():
            messagebox.showerror("Error", "Queue is Full")
            return

        self.queue.append((item, priority))
        self.queue.sort(key=lambda x: x[1])
        messagebox.showinfo("Success", f"{item} Inserted Successfully")

    def dequeue(self):
        if self.is_empty():
            messagebox.showerror("Error", "Queue is Empty")
            return

        item = self.queue.pop(0)
        messagebox.showinfo("Removed", f"{item[0]} Removed Successfully")

    def display(self):
        output.delete("1.0", END)

        if self.is_empty():
            output.insert(END, "Queue is Empty")
            return

        output.insert(END, "Priority Queue\n")
        output.insert(END, "-------------------------\n")
        output.insert(END, "Item\tPriority\n")
        output.insert(END, "-------------------------\n")

        for item, priority in self.queue:
            output.insert(END, f"{item}\t{priority}\n")

    def highest(self):
        if self.is_empty():
            messagebox.showinfo("Info", "Queue is Empty")
        else:
            messagebox.showinfo("Highest Priority",
                                self.queue[0][0])

    def lowest(self):
        if self.is_empty():
            messagebox.showinfo("Info", "Queue is Empty")
        else:
            messagebox.showinfo("Lowest Priority",
                                self.queue[-1][0])


def create_queue():
    global pq

    try:
        size = int(capacity_entry.get())
        pq = PriorityQueue(size)
        messagebox.showinfo("Success", "Queue Created Successfully")
    except:
        messagebox.showerror("Error", "Enter Valid Capacity")


def enqueue_item():
    item = item_entry.get()

    try:
        priority = int(priority_entry.get())
        pq.enqueue(item, priority)
    except:
        messagebox.showerror("Error", "Enter Valid Priority")


def dequeue_item():
    pq.dequeue()


def display_queue():
    pq.display()


def check_empty():
    if pq.is_empty():
        messagebox.showinfo("Status", "Queue is Empty")
    else:
        messagebox.showinfo("Status", "Queue is Not Empty")


def check_full():
    if pq.is_full():
        messagebox.showinfo("Status", "Queue is Full")
    else:
        messagebox.showinfo("Status", "Queue is Not Full")


def highest():
    pq.highest()


def lowest():
    pq.lowest()


root = Tk()
root.title("Priority Queue")
root.geometry("500x550")
root.resizable(False, False)

Label(root, text="Priority Queue",
      font=("Arial", 18, "bold")).pack(pady=10)

Label(root, text="Queue Capacity").pack()
capacity_entry = Entry(root)
capacity_entry.pack()

Button(root, text="Create Queue",
       command=create_queue).pack(pady=5)

Label(root, text="Item").pack()
item_entry = Entry(root)
item_entry.pack()

Label(root, text="Priority").pack()
priority_entry = Entry(root)
priority_entry.pack()

Button(root, text="Enqueue", width=20,
       command=enqueue_item).pack(pady=5)

Button(root, text="Dequeue", width=20,
       command=dequeue_item).pack(pady=5)

Button(root, text="Display", width=20,
       command=display_queue).pack(pady=5)

Button(root, text="Check Empty", width=20,
       command=check_empty).pack(pady=5)

Button(root, text="Check Full", width=20,
       command=check_full).pack(pady=5)

Button(root, text="Highest Priority", width=20,
       command=highest).pack(pady=5)

Button(root, text="Lowest Priority", width=20,
       command=lowest).pack(pady=5)

Button(root, text="Exit", width=20,
       command=root.destroy).pack(pady=5)

output = Text(root, width=45, height=10)
output.pack(pady=10)

root.mainloop()
