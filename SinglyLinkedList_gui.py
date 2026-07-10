import tkinter as tk
from tkinter import messagebox


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None


    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node


    def insert_position(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                return
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    def delete_value(self, data):
        temp = self.head
        prev = None

        while temp:
            if temp.data == data:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next
                return True

            prev = temp
            temp = temp.next

        return False


    def delete_position(self, pos):

        if self.head is None:
            return False

        if pos == 0:
            self.head = self.head.next
            return True

        temp = self.head

        for i in range(pos - 1):
            if temp.next is None:
                return False
            temp = temp.next

        temp.next = temp.next.next
        return True


    def display(self):
        result = ""
        temp = self.head

        while temp:
            result += str(temp.data) + " -> "
            temp = temp.next

        return result + "NULL"



# GUI Code
class LinkedListGUI:

    def __init__(self, root):

        self.list = LinkedList()

        root.title("Singly Linked List GUI")
        root.geometry("450x500")


        tk.Label(
            root,
            text="Singly Linked List",
            font=("Arial", 18, "bold")
        ).pack(pady=10)


        self.entry = tk.Entry(root)
        self.entry.pack()


        self.position = tk.Entry(root)
        self.position.pack()

        self.position.insert(0, "Position")


        tk.Button(
            root,
            text="Insert Beginning",
            command=self.insert_begin
        ).pack(pady=5)


        tk.Button(
            root,
            text="Insert End",
            command=self.insert_end
        ).pack(pady=5)


        tk.Button(
            root,
            text="Insert Position",
            command=self.insert_pos
        ).pack(pady=5)


        tk.Button(
            root,
            text="Delete Value",
            command=self.delete_value
        ).pack(pady=5)


        tk.Button(
            root,
            text="Delete Position",
            command=self.delete_pos
        ).pack(pady=5)


        tk.Button(
            root,
            text="Display List",
            command=self.show
        ).pack(pady=5)


        self.output = tk.Label(
            root,
            text="",
            font=("Arial", 12)
        )

        self.output.pack(pady=20)



    def get_value(self):
        return int(self.entry.get())


    def insert_begin(self):
        self.list.insert_beginning(self.get_value())
        messagebox.showinfo("Success", "Inserted at Beginning")


    def insert_end(self):
        self.list.insert_end(self.get_value())
        messagebox.showinfo("Success", "Inserted at End")


    def insert_pos(self):
        value = self.get_value()
        pos = int(self.position.get())

        self.list.insert_position(value, pos)

        messagebox.showinfo("Success", "Inserted")


    def delete_value(self):
        value = self.get_value()

        if self.list.delete_value(value):
            messagebox.showinfo("Deleted", "Node Deleted")
        else:
            messagebox.showinfo("Error", "Value not found")


    def delete_pos(self):

        pos = int(self.position.get())

        if self.list.delete_position(pos):
            messagebox.showinfo("Deleted", "Node Deleted")
        else:
            messagebox.showinfo("Error", "Invalid Position")


    def show(self):

        self.output.config(
            text=self.list.display()
        )



root = tk.Tk()

app = LinkedListGUI(root)

root.mainloop()
