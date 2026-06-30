# Stack Implementation using List

stack = []

def push():
    value = int(input("Enter value: "))
    stack.append(value)
    print(value, "inserted into stack.")

def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Deleted Element:", stack.pop())

def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Top Element:", stack[-1])

def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack Elements (Top to Bottom):")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

def delimiter_matching():
    expression = input("Enter expression: ")
    s = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expression:
        if ch in "({[":
            s.append(ch)
        elif ch in ")}]":
            if not s or s.pop() != pairs[ch]:
                print("Not Balanced")
                return

    if not s:
        print("Balanced Expression")
    else:
        print("Not Balanced")

def prefix_to_postfix():
    prefix = input("Enter Prefix Expression: ")
    s = []

    for ch in reversed(prefix):
        if ch.isalnum():
            s.append(ch)
        else:
            op1 = s.pop()
            op2 = s.pop()
            s.append(op1 + op2 + ch)

    print("Postfix Expression:", s[-1])

def evaluate_prefix():
    prefix = input("Enter Prefix Expression: ")
    s = []

    for ch in reversed(prefix):
        if ch.isdigit():
            s.append(int(ch))
        else:
            a = s.pop()
            b = s.pop()

            if ch == '+':
                s.append(a + b)
            elif ch == '-':
                s.append(a - b)
            elif ch == '*':
                s.append(a * b)
            elif ch == '/':
                s.append(a // b)

    print("Result =", s[-1])

while True:
    print("\n------ STACK MENU ------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Delimiter Matching")
    print("6. Prefix to Postfix")
    print("7. Evaluate Prefix")
    print("8. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        delimiter_matching()
    elif choice == 6:
        prefix_to_postfix()
    elif choice == 7:
        evaluate_prefix()
    elif choice == 8:
        print("Program Ended.")
        break
    else:
        print("Invalid Choice")
