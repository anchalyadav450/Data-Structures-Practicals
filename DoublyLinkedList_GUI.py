# Aim: Implement Doubly Linked List with GUI using Tkinter


import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp


    def delete_beginning(self):

        if self.head:
            self.head = self.head.next

            if self.head:
                self.head.prev = None


    def delete_end(self):

        if self.head is None:
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None


    def search(self, value):

        temp = self.head

        while temp:

            if temp.data == value:
                return True

            temp = temp.next

        return False


    def display(self):

        result = ""
        temp = self.head

        while temp:
            result += str(temp.data) + " "
            temp = temp.next

        return result



# GUI Program

dll = DoublyLinkedList()


def insert_begin():
    data = int(entry.get())
    dll.insert_beginning(data)
    show_list()


def insert_end():
    data = int(entry.get())
    dll.insert_end(data)
    show_list()


def delete_begin():
    dll.delete_beginning()
    show_list()


def delete_end():
    dll.delete_end()
    show_list()


def search_node():
    data = int(entry.get())

    if dll.search(data):
        messagebox.showinfo("Search", "Node Found")
    else:
        messagebox.showinfo("Search", "Node Not Found")


def show_list():

    output.delete(1.0, tk.END)

    output.insert(tk.END, "Doubly Linked List:\n")
    output.insert(tk.END, dll.display())



# Window

window = tk.Tk()
window.title("Doubly Linked List GUI")
window.geometry("400x400")


label = tk.Label(window, text="Enter Data")
label.pack()


entry = tk.Entry(window)
entry.pack()


btn1 = tk.Button(window, text="Insert Beginning",
                 command=insert_begin)
btn1.pack(pady=5)


btn2 = tk.Button(window, text="Insert End",
                 command=insert_end)
btn2.pack(pady=5)


btn3 = tk.Button(window, text="Delete Beginning",
                 command=delete_begin)
btn3.pack(pady=5)


btn4 = tk.Button(window, text="Delete End",
                 command=delete_end)
btn4.pack(pady=5)


btn5 = tk.Button(window, text="Search",
                 command=search_node)
btn5.pack(pady=5)


btn6 = tk.Button(window, text="Display",
                 command=show_list)
btn6.pack(pady=5)


output = tk.Text(window, height=8, width=35)
output.pack(pady=10)


window.mainloop()
