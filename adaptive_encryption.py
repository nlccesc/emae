import random

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
        self.char_count[char] = self.char_count.get(char, 0) + 1
        if len(self.history) > 10:  # Keep only the last 10 characters to analyze patterns
            self.history.pop(0)

        # Save the state before processing the character
        state = (self.adaptive_plugboard.copy(), [rotor.position for rotor in self.enigma.rotors])
        self.history.append(state)

        char = self.adaptive_plugboard[char]
        self.advanced_adapt_plugboard(char)

        if self.complex_predictive_logic(char):
            for rotor in self.enigma.rotors:
                rotor.rotate()

        if self.char_count[char] > 10:
            self.char_count[char] = 0

        return self.enigma.encrypt(char)

    def decrypt(self, char):
        if not self.history:
            raise ValueError("No more characters to decrypt")

        # Restore the state before processing the character
        adaptive_plugboard, rotor_positions = self.history.pop()
        self.adaptive_plugboard = adaptive_plugboard
        for rotor, position in zip(self.enigma.rotors, rotor_positions):
            rotor.set_position(position)

        return self.enigma.encrypt(char)