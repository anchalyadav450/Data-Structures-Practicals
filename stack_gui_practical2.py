from tkinter import *

stack = []

def push():
    value = entry.get()
    stack.append(value)
    result.config(text=value+" inserted")
    entry.delete(0,END)

def pop():
    if len(stack)==0:
        result.config(text="Stack Underflow")
    else:
        result.config(text="Deleted Element : "+stack.pop())

def peek():
    if len(stack)==0:
        result.config(text="Stack Empty")
    else:
        result.config(text="Top Element : "+stack[-1])
        
def display():
    if len(stack)==0:
        result.config(text="Stack Empty")
    else:
        result.config(text="Stack:\n"+"\n".join(stack[::-1]))

def delimiter_matching():
    exp = entry.get()
    s=[]

    pair={')':'(',']':'[','}':'{'}

    for ch in exp:
        if ch in "({[":
            s.append(ch)

        elif ch in ")}]":
            if not s or s.pop()!=pair[ch]:
                result.config(text="Not Balanced")
                return

    if len(s)==0:
        result.config(text="Balanced Expression")
    else:
        result.config(text="Not Balanced")


def prefix_to_postfix():

    prefix=entry.get()
    s=[]

    try:
        for ch in reversed(prefix):

            if ch.isalnum():
                s.append(ch)

            else:
                a=s.pop()
                b=s.pop()
                s.append(a+b+ch)

        result.config(text="Postfix : "+s[-1])

    except:
        result.config(text="Invalid Prefix")


def evaluate_prefix():

    exp=entry.get()
    s=[]

    try:

        for ch in reversed(exp):

            if ch.isdigit():
                s.append(int(ch))

            else:

                a=s.pop()
                b=s.pop()

                if ch=='+':
                    s.append(a+b)

                elif ch=='-':
                    s.append(a-b)

                elif ch=='*':
                    s.append(a*b)

                elif ch=='/':
                    s.append(a//b)


        result.config(text="Result : "+str(s[-1]))

    except:
        result.config(text="Invalid Expression")



# GUI Window

root=Tk()

root.title("Stack Implementation")
root.geometry("500x600")
root.config(bg="#dbeafe")


title=Label(root,
text="STACK IMPLEMENTATION USING GUI",
font=("Arial",18,"bold"),
bg="#2563eb",
fg="white")

title.pack(fill=X)


Label(root,
text="Enter Value / Expression",
bg="#dbeafe",
font=("Arial",12,"bold")).pack(pady=10)


entry=Entry(root,
font=("Arial",14),
width=30)

entry.pack()



Button(root,text="Push",
width=20,
command=push,
bg="green",
fg="white").pack(pady=5)


Button(root,text="Pop",
width=20,
command=pop,
bg="red",
fg="white").pack(pady=5)


Button(root,text="Peek",
width=20,
command=peek).pack(pady=5)


Button(root,text="Display",
width=20,
command=display).pack(pady=5)


Button(root,text="Delimiter Matching",
width=20,
command=delimiter_matching).pack(pady=5)


Button(root,text="Prefix To Postfix",
width=20,
command=prefix_to_postfix).pack(pady=5)


Button(root,text="Evaluate Prefix",
width=20,
command=evaluate_prefix).pack(pady=5)



result=Label(root,
text="Output",
bg="white",
fg="blue",
font=("Arial",14),
width=35,
height=6)

result.pack(pady=20)



root.mainloop()
