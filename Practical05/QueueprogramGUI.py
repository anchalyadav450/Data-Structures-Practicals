from tkinter import *
from tkinter import messagebox


class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size

    def insert(self, item):
        if self.is_full():
            messagebox.showerror("Error", "Queue Overflow! Queue is Full")
        else:
            self.queue.append(item)
            messagebox.showinfo("Success", item + " Inserted Successfully")

    def delete(self):
        if self.is_empty():
            messagebox.showerror("Error", "Queue Underflow! Queue is Empty")
        else:
            item = self.queue.pop(0)
            messagebox.showinfo("Deleted", item + " Deleted Successfully")

    def traversal(self):
        output.delete("1.0", END)

        if self.is_empty():
            output.insert(END, "Queue is Empty")
        else:
            output.insert(END, "Queue Elements:\n")
            output.insert(END, "----------------\n")

            for i in self.queue:
                output.insert(END, i + "\n")


def create_queue():
    global q

    try:
        size = int(size_entry.get())
        q = Queue(size)
        messagebox.showinfo("Success",
                            "Queue Created Successfully")

    except:
        messagebox.showerror("Error",
                             "Enter Valid Size")


def insert_element():
    item = item_entry.get()

    if item == "":
        messagebox.showerror("Error",
                             "Enter Element")
    else:
        q.insert(item)


def delete_element():
    q.delete()


def display_queue():
    q.traversal()


def check_empty():
    if q.is_empty():
        messagebox.showinfo("Status",
                            "Queue is Empty")
    else:
        messagebox.showinfo("Status",
                            "Queue is Not Empty")


def check_full():
    if q.is_full():
        messagebox.showinfo("Status",
                            "Queue is Full")
    else:
        messagebox.showinfo("Status",
                            "Queue is Not Full")


# Main Window

root = Tk()
root.title("Queue Implementation")
root.geometry("450x550")
root.resizable(False, False)


Label(root,
      text="Queue Implementation",
      font=("Arial",18,"bold")).pack(pady=10)


Label(root,text="Queue Size").pack()

size_entry = Entry(root)
size_entry.pack()


Button(root,
       text="Create Queue",
       width=20,
       command=create_queue).pack(pady=5)



Label(root,text="Enter Element").pack()

item_entry = Entry(root)
item_entry.pack()



Button(root,
       text="Insert",
       width=20,
       command=insert_element).pack(pady=5)


Button(root,
       text="Delete",
       width=20,
       command=delete_element).pack(pady=5)


Button(root,
       text="Traversal / Display",
       width=20,
       command=display_queue).pack(pady=5)


Button(root,
       text="Check Empty",
       width=20,
       command=check_empty).pack(pady=5)


Button(root,
       text="Check Full",
       width=20,
       command=check_full).pack(pady=5)


Button(root,
       text="Exit",
       width=20,
       command=root.destroy).pack(pady=5)



output = Text(root,
              width=40,
              height=10)

output.pack(pady=15)


q = None

root.mainloop()
