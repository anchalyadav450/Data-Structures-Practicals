import heapq
from collections import Counter

# Node class
class TreeNode:
    def __init__(self, symbol=None, count=None):
        self.symbol = symbol
        self.count = count
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.count < other.count


# Build Huffman Tree
def create_tree(freq):
    priority_queue = [TreeNode(ch, fr) for ch, fr in freq.items()]
    heapq.heapify(priority_queue)

    print("\nBuilding Huffman Tree:")

    while len(priority_queue) > 1:
        first = heapq.heappop(priority_queue)
        second = heapq.heappop(priority_queue)

        print(f"Combining {first.symbol} ({first.count}) and {second.symbol} ({second.count})")

        parent = TreeNode(count=first.count + second.count)
        parent.left = first
        parent.right = second

        heapq.heappush(priority_queue, parent)

    return priority_queue[0]


# Generate Huffman Codes
def create_codes(root, current="", codes=None):
    if codes is None:
        codes = {}

    if root:
        if root.symbol is not None:
            codes[root.symbol] = current
            print(f"Character '{root.symbol}' -> {current}")

        create_codes(root.left, current + "0", codes)
        create_codes(root.right, current + "1", codes)

    return codes


# Encoding
def encode(message):
    if message == "":
        return "", {}

    frequency = Counter(message)

    print("Character Frequency:")
    print(dict(frequency))

    tree = create_tree(frequency)
    code_table = create_codes(tree)

    binary = ""

    for ch in message:
        binary += code_table[ch]

    print("\nEncoded Binary:")
    print(binary)

    return binary, code_table


# Decoding
def decode(binary, code_table):
    reverse = {v: k for k, v in code_table.items()}

    text = ""
    temp = ""

    print("\nDecoding Process:")

    for bit in binary:
        temp += bit
        if temp in reverse:
            print(temp, "->", reverse[temp])
            text += reverse[temp]
            temp = ""

    return text


# Main Program
if __name__ == "__main__":

    print("===== HUFFMAN CODING PROGRAM =====")

    user_text = input("Enter any text: ")

    encoded_text, table = encode(user_text)

    print("\nHuffman Code Table:")
    print(table)

    decoded_text = decode(encoded_text, table)

    print("\nOriginal Text :", user_text)
    print("Decoded Text  :", decoded_text)

    if user_text == decoded_text:
        print("\nResult: Encoding and Decoding Successful.")
    else:
        print("\nResult: Something went wrong.")
