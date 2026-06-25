class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll No:", self.roll)


student = None

while True:
    print("\n===== Student ADT =====")
    print("1. Create Student")
    print("2. Update Student")
    print("3. Display Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll = input("Enter Roll No: ")
        student = Student(name, roll)
        print("Student Created Successfully!")

    elif choice == "2":
        if student:
            student.name = input("Enter New Name: ")
            student.roll = input("Enter New Roll No: ")
            print("Student Updated Successfully!")
        else:
            print("No Student Record Found!")

    elif choice == "3":
        if student:
            student.display()
        else:
            print("No Student Record Found!")

    elif choice == "4":
        student = None
        print("Student Record Deleted!")

    elif choice == "5":
        print("Program Exited.")
        break

    else:
        print("Invalid Choice!")
