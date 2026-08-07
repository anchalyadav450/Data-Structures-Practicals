import tkinter as tk
from tkinter import scrolledtext
import heapq
from collections import Counter


# ---------------- Node Class ----------------
class TreeNode:
    def __init__(self, symbol=None, count=None):
        self.symbol = symbol
        self.count = count
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.count < other.count


# ---------------- Build Huffman Tree ----------------
def create_tree(freq):
    heap = [TreeNode(ch, fr) for ch, fr in freq.items()]
    heapq.heapify(heap)

    log_box.insert(tk.END, "\nBuilding Huffman Tree:\n")

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        log_box.insert(
            tk.END,
            f"Combining {left.symbol} ({left.count}) and {right.symbol} ({right.count})\n"
        )

        parent = TreeNode(count=left.count + right.count)
        parent.left = left
        parent.right = right

        heapq.heappush(heap, parent)

    return heap[0]


# ---------------- Generate Codes ----------------
def create_codes(root, code="", table=None):
    if table is None:
        table = {}

    if root:
        if root.symbol is not None:
            table[root.symbol] = code
            log_box.insert(tk.END, f"Character '{root.symbol}' -> {code}\n")

        create_codes(root.left, code + "0", table)
        create_codes(root.right, code + "1", table)

    return table


# ---------------- Encode ----------------
def encode_text():
    text = entry.get()

    if text == "":
        result_box.delete("1.0", tk.END)
        result_box.insert(tk.END, "Please enter some text.")
        return

    freq = Counter(text)

    log_box.delete("1.0", tk.END)
    result_box.delete("1.0", tk.END)

    log_box.insert(tk.END, "Character Frequency:\n")
    log_box.insert(tk.END, str(dict(freq)) + "\n")

    tree = create_tree(freq)
    codes = create_codes(tree)

    encoded = ""

    for ch in text:
        encoded += codes[ch]

    result_box.insert(tk.END, "Original Text:\n")
    result_box.insert(tk.END, text + "\n\n")

    result_box.insert(tk.END, "Encoded Binary:\n")
    result_box.insert(tk.END, encoded + "\n\n")

    result_box.insert(tk.END, "Huffman Codes:\n")
    result_box.insert(tk.END, str(codes) + "\n\n")

    decoded = decode(encoded, codes)

    result_box.insert(tk.END, "Decoded Text:\n")
    result_box.insert(tk.END, decoded)


# ---------------- Decode ----------------
def decode(binary, codes):
    reverse = {v: k for k, v in codes.items()}

    temp = ""
    output = ""

    log_box.insert(tk.END, "\nDecoding:\n")

    for bit in binary:
        temp += bit

        if temp in reverse:
            log_box.insert(tk.END, f"{temp} -> {reverse[temp]}\n")
            output += reverse[temp]
            temp = ""

    return output


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Huffman Coding Visualizer")
root.geometry("750x650")
root.configure(bg="#dfefff")

title = tk.Label(
    root,
    text="HUFFMAN CODING USING PYTHON",
    font=("Arial", 18, "bold"),
    bg="#003366",
    fg="white",
    pady=10
)
title.pack(fill="x")

frame = tk.Frame(root, bg="#dfefff")
frame.pack(pady=10)

tk.Label(frame, text="Enter Text:", font=("Arial", 12), bg="#dfefff").grid(row=0, column=0)

entry = tk.Entry(frame, width=40, font=("Arial", 12))
entry.grid(row=0, column=1, padx=10)

btn = tk.Button(
    frame,
    text="Encode & Decode",
    font=("Arial", 11, "bold"),
    bg="green",
    fg="white",
    command=encode_text
)
btn.grid(row=0, column=2)

tk.Label(root, text="Process Log", font=("Arial", 13, "bold"), bg="#dfefff").pack()

log_box = scrolledtext.ScrolledText(root, width=85, height=12)
log_box.pack(pady=5)

tk.Label(root, text="Result", font=("Arial", 13, "bold"), bg="#dfefff").pack()

result_box = scrolledtext.ScrolledText(root, width=85, height=12)
result_box.pack(pady=5)

root.mainloop()
