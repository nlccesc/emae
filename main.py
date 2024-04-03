import string
import random
from rotor import Rotor
from plugboard import PlugBoard
from reflector import Reflector
from adaptive_encryption import AdaptiveEnigma
from enigma import Enigma

# Usage
plugboard = PlugBoard([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')])
rotors = [
    Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 0, 0),
    Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 0, 0),
    Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 0, 0),
    Rotor('ESOVPZJAYQUIRHXLNFTGKDCMWB', 0, 0)  # Fourth rotor
]
reflector = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
enigma = Enigma(plugboard, rotors, reflector)

adaptive_enigma = AdaptiveEnigma(enigma)

# Encrypt a message
plaintext = "Your mudda gae"
plaintext = plaintext.replace(" ", "").upper()
print(f"Original Text: {plaintext}")
ciphertext = "".join(adaptive_enigma.encrypt(char) for char in plaintext)
print(f"Ciphertext: {ciphertext}")

# Reset the machine to its initial state before decrypting
adaptive_enigma.reset()

# Decrypt the message
decrypted_text = "".join(adaptive_enigma.decrypt(char) for char in ciphertext[:len(plaintext)])
print(f"Decrypted text: {decrypted_text}")