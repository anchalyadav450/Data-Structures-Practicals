from tkinter import *
from tkinter import messagebox

student = {"name": "", "roll": ""}

def create_student():
    student["name"] = name_entry.get()
    student["roll"] = roll_entry.get()

    messagebox.showinfo("Success", "Student Created Successfully!")

def update_student():
    student["name"] = name_entry.get()
    student["roll"] = roll_entry.get()

    messagebox.showinfo("Success", "Student Updated Successfully!")

def display_student():
    if student["name"] == "":
        messagebox.showwarning("Warning", "No Student Record Found!")
    else:
        messagebox.showinfo(
            "Student Details",
            f"Name: {student['name']}\nRoll No: {student['roll']}"
        )

def delete_student():
    student["name"] = ""
    student["roll"] = ""

    name_entry.delete(0, END)
    roll_entry.delete(0, END)

    messagebox.showinfo("Success", "Student Record Deleted!")

root = Tk()
root.title("Student ADT GUI")
root.geometry("400x300")

Label(root, text="Student Name").pack(pady=5)

name_entry = Entry(root, width=30)
name_entry.pack()

Label(root, text="Roll Number").pack(pady=5)

roll_entry = Entry(root, width=30)
roll_entry.pack()

Button(root, text="Create", width=15,
       command=create_student).pack(pady=5)

Button(root, text="Update", width=15,
       command=update_student).pack(pady=5)

Button(root, text="Display", width=15,
       command=display_student).pack(pady=5)

Button(root, text="Delete", width=15,
       command=delete_student).pack(pady=5)

root.mainloop()
