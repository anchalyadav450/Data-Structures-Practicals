from tkinter import *
from tkinter import messagebox

stack = []

def push():
    item = entry.get()

    if item == "":
        messagebox.showwarning("Warning", "Please enter an item")
        return

    stack.append(item)
    update_display()
    entry.delete(0, END)

def pop():
    if not stack:
        messagebox.showerror("Error", "Stack is Empty")
        return

    item = stack.pop()
    messagebox.showinfo("Popped Item", item)
    update_display()

def peek():
    if not stack:
        messagebox.showerror("Error", "Stack is Empty")
        return

    messagebox.showinfo("Top Item", stack[-1])

def size():
    messagebox.showinfo("Stack Size", str(len(stack)))

def is_empty():
    if len(stack) == 0:
        messagebox.showinfo("Status", "Stack is Empty")
    else:
        messagebox.showinfo("Status", "Stack is Not Empty")

def update_display():
    listbox.delete(0, END)

    for item in reversed(stack):
        listbox.insert(END, item)

root = Tk()
root.title("Stack ADT GUI")
root.geometry("400x400")

Label(root, text="Enter Item").pack(pady=5)

entry = Entry(root, width=30)
entry.pack(pady=5)

Button(root, text="Push", width=15, command=push).pack(pady=5)
Button(root, text="Pop", width=15, command=pop).pack(pady=5)
Button(root, text="Peek", width=15, command=peek).pack(pady=5)
Button(root, text="Size", width=15, command=size).pack(pady=5)
Button(root, text="Is Empty", width=15, command=is_empty).pack(pady=5)

Label(root, text="Stack Contents").pack(pady=5)

listbox = Listbox(root, width=30, height=10)
listbox.pack(pady=5)

root.mainloop()
