import random

class AdaptiveEnigma:

    def __init__(self, enigma):
        self.enigma = enigma
        self.char_count = {}
        self.adaptive_plugboard = {chr(i): chr(i) for i in range(256)}
        self.history = []  # keep track of last N letters
        self.initial_state = (self.adaptive_plugboard.copy(), [rotor.position for rotor in self.enigma.rotors])

    def reset(self):
        self.adaptive_plugboard, rotor_positions = self.initial_state
        for rotor, position in zip(self.enigma.rotors, rotor_positions):
            rotor.set_position(position)
    
    def get_state(self):
        return self.adaptive_plugboard.copy(), [rotor.position for rotor in self.enigma.rotors]
    
    def set_state(self, state):
        self.adaptive_plugboard, rotor_positions = state
        for rotor, position in zip(self.enigma.rotors, rotor_positions):
            rotor.set_position(position)

    # simple div algo
    def is_prime_div_algo(self, n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))

    def complex_predictive_logic(self, char):
        # Mimic complex predictive logic using character patterns and frequency
        pattern_found = False
        if len(self.history) >= 3:  # Example: check for repeating patterns in the last 3 characters
            pattern_found = self.history[-1] == self.history[-3] and self.history[-2] == char
        return pattern_found or ord(char) % 7 == 0  # More complex condition

    def advanced_adapt_plugboard(self, char):
        # More complex adaptive logic for the plugboard
        if char in self.char_count and self.char_count[char] % 15 == 0:  # Adjust frequency for changes
            # Swap with a character that is not adjacent in ASCII to avoid predictable patterns
            next_char = chr((ord(char) + random.randint(2, 5)) % 256)  # Random offset to increase unpredictability
            self.adaptive_plugboard[char], self.adaptive_plugboard[next_char] = next_char, self.adaptive_plugboard[char]

    def encrypt(self, char):
    # Save the current state before processing the character
        self.history.append((self.adaptive_plugboard.copy(), [rotor.position for rotor in self.enigma.rotors]))
    
    # Apply adaptive logic
        self.advanced_adapt_plugboard(char)
    
    # Encrypt the character
        encrypted_char = self.enigma.encrypt(self.adaptive_plugboard[char])
    
    # Update character count
        self.char_count[char] = self.char_count.get(char, 0) + 1
    
    # Check if the ASCII value of the character is prime
        if self.is_prime(ord(char)):
        # If it's prime, rotate the rotors
            for rotor in self.enigma.rotors:
                rotor.rotate()

        return encrypted_char

def decrypt(self, encrypted_char):
    if not self.history:
        raise ValueError("No more characters to decrypt")

    # Save the current state
    current_state = self.get_state()

    # Restore the state before processing the character
    adaptive_plugboard, rotor_positions = self.history.pop()
    self.adaptive_plugboard = adaptive_plugboard
    for rotor, position in zip(self.enigma.rotors, rotor_positions):
        rotor.set_position(position)

    # Decrypt the character
    decrypted_char = self.enigma.decrypt(encrypted_char)

    # Check if the ASCII value of the decrypted character is prime
    if self.is_prime(ord(decrypted_char)):
        # If it's prime, rotate the rotors
        for rotor in self.enigma.rotors:
            rotor.rotate()

    # Restore the current state
    self.set_state(current_state)

    return self.adaptive_plugboard[decrypted_char]