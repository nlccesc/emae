import random

class AdaptiveEnigma:

    def __init__(self, enigma):
        self.enigma = enigma
        self.char_count = {}
        self.adaptive_plugboard = {chr(i): chr(i) for i in range(256)}
        self.history = []  # To keep track of the last N characters
        self.initial_state = (self.adaptive_plugboard.copy(), [rotor.position for rotor in self.enigma.rotors])

    def reset(self):
        self.adaptive_plugboard, rotor_positions = self.initial_state
        for rotor, position in zip(self.enigma.rotors, rotor_positions):
            rotor.set_position(position)
# simple div algo
    def is_prime_div_algo(self, n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def complex_predictive_logic(self, char):
        pattern_found = False
        if len(self.history) >= 3:  
            pattern_found = self.history[-1] == self.history[-3] and self.history[-2] == char
        return pattern_found or ord(char) % 7 == 0  

    def advanced_adapt_plugboard(self, char):
        if char in self.char_count and self.char_count[char] % 15 == 0:  
            next_char = chr((ord(char) + random.randint(2, 5)) % 256)  
            self.adaptive_plugboard[char], self.adaptive_plugboard[next_char] = next_char, self.adaptive_plugboard[char]

def generate_huffman_codes(self, root, code, huffman_codes):
        if root is None:
            return

        if root.char is not None:
            huffman_codes[root.char] = code

        self.generate_huffman_codes(root.left, code + '0', huffman_codes)
        self.generate_huffman_codes(root.right, code + '1', huffman_codes)

    def huffman_encode(self, message):
        root = self.build_huffman_tree(message)
        huffman_codes = {}
        self.generate_huffman_codes(root, '', huffman_codes)
        return ''.join(huffman_codes[char] for char in message)

    def huffman_decode(self, encoded_message, root):
        decoded_message = []
        current = root

        for bit in encoded_message:
            if bit == '0':
                current = current.left
            else:  # bit == '1'
                current = current.right

            if current.char is not None:
                decoded_message.append(current.char)
                current = root

        return ''.join(decoded_message)
    
    def encrypt(self, char):
        self.char_count[char] = self.char_count.get(char, 0) + 1
        if len(self.history) > 10:  
            self.history.pop(0)

        state = (self.adaptive_plugboard.copy(), [rotor.position for rotor in self.enigma.rotors])
        self.history.append(state)

        char = self.adaptive_plugboard[char]
        self.advanced_adapt_plugboard(char)

        if self.complex_predictive_logic(char):
            for rotor in self.enigma.rotors:
                rotor.rotate()

        if self.is_prime(ord(char)):
            for _ in range(random.randint(1, 10)):
                for rotor in self.enigma.rotors:
                    rotor.rotate()

        if self.char_count[char] > 10:
            self.char_count[char] = 0

        return self.enigma.encrypt(char)

    def decrypt(self, char):
        if not self.history:
            raise ValueError("No more characters to decrypt")

        adaptive_plugboard, rotor_positions = self.history.pop()
        self.adaptive_plugboard = adaptive_plugboard
        for rotor, position in zip(self.enigma.rotors, rotor_positions):
            rotor.set_position(position)

        decrypted_char = self.enigma.decrypt(char)

        if self.is_prime(ord(decrypted_char)):
            for _ in range(random.randint(1, 10)):
                for rotor in self.enigma.rotors:
                    rotor.rotate()

        return decrypted_char
