from collections import Counter
from heapq import heapify, heappop, heappush

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq
    
class HuffmanTree:
    def __init__(self, message):
        self.root = self.build_huffman_tree(message)

    def build_huffman_tree(self, message):
        freq = Counter(message)
        heap = [Node(char, freq) for char, freq in freq.items()]
        heapify(heap)

        while len(heap) > 1:
            left = heappop(heap)
            right = heappop(heap)
            merged = Node(None, left.freq + right.freq, left, right)
            heappush(heap, merged)

        return heap[0]
    
    def generate_huffman_code(self, root=None, code=''):
        if root is None:
            root = self.root

        if root.char is not None:
            return {root.char: code}
        
        codes = {}
        if root.left:
            codes.update(self.generate_huffman_code(root.left, code + '0'))
        if root.right:
            codes.update(self.generate_huffman_code(root.right, code + '0'))
        return codes
    
    def encode(self, message):
        codes = self.generate_huffman_code()
        return ''.join(codes[char] for char in message)
    
    def decode(self, encoded_message):
        decoded_message = []
        current = self.root

        for bit in encoded_message:
            if bit == '0':
                current = current.left
            else: 
                current = current.right
            
            if current.char is not None:
                decoded_message.append(current.char)
                current = self.root

        return ''.join(decoded_message)
            

        