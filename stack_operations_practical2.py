import os
import time
from termcolor import colored, cprint


class Stack:

    def __init__(self):
        self.items = []


    def is_empty(self):
        return len(self.items) == 0


    def insert(self, item, position):

        if position < 0 or position > len(self.items):
            raise IndexError("Invalid position")

        self.items.insert(position, item)

        print(colored(
            f"'{item}' inserted at position {position}",
            "green"
        ))

        self.animate_insert(item)


    def delete(self, position):

        if position < 0 or position >= len(self.items):
            raise IndexError("Invalid position")

        item = self.items.pop(position)

        print(colored(
            f"'{item}' deleted from position {position}",
            "red"
        ))

        self.animate_delete(item)

        return item


    def peek(self):

        if self.is_empty():
            raise IndexError("Peek from empty stack")

        return self.items[-1]


    def size(self):

        return len(self.items)

    def traverse(self):

        if self.is_empty():
            raise IndexError("Stack is empty")

        return " <- ".join(self.items)


    def __str__(self):

        if self.items:
            return " <- ".join(reversed(self.items))

        return "Stack is empty"



    def animate_insert(self,item):

        for i in range(3):
            print(colored(
                f"Inserting {item}...",
                "yellow"
            ))

            time.sleep(0.3)

        self.clear_screen()



    def animate_delete(self,item):

        for i in range(3):
            print(colored(
                f"Deleting {item}...",
                "magenta"
            ))

            time.sleep(0.3)

        self.clear_screen()



    @staticmethod
    def clear_screen():

        os.system(
            'cls' if os.name=='nt' else 'clear'
        )



def stack_operations():

    stack = Stack()

    cprint(
        "Welcome to Stack Operations Program",
        "cyan",
        attrs=["bold"]
    )


    while True:

        print("\nCurrent Stack:",
              colored(stack,"blue"))


        print("""
1. Insert item
2. Delete item
3. Peek
4. Check Empty
5. Size
6. Traverse
7. Exit
""")


        try:

            choice=int(
                input(
                    colored(
                    "Enter choice: ",
                    "green")
                )
            )


        except:

            print("Enter number only")
            continue



        if choice==1:


            item=input(
                "Enter item: "
            )


            position=int(
                input(
                "Enter position: ")
            )


            try:

                stack.insert(item,position)

            except Exception as e:

                print(e)



        elif choice==2:


            position=int(
                input(
                "Enter delete position: ")
            )


            try:

                stack.delete(position)

            except Exception as e:

                print(e)



        elif choice==3:


            try:

                print(
                colored(
                "Top item: "+stack.peek(),
                "blue"))

            except Exception as e:

                print(e)



        elif choice==4:


            print(
            "Empty?",
            stack.is_empty()
            )



        elif choice==5:


            print(
            "Stack Size:",
            stack.size()
            )



        elif choice==6:


            try:

                print(
                "Stack:",
                stack.traverse()
                )

            except Exception as e:

                print(e)



        elif choice==7:

            print("Program Ended")
            break



        else:

            print("Invalid choice")



stack_operations()
