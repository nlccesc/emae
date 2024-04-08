import string
import random
from rotor import Rotor
from plugboard import PlugBoard
from reflector import Reflector
from adaptive_encryption import AdaptiveEnigma
from enigma import Enigma

# Usage
plugboard = PlugBoard([('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'), ('I', 'J')])

# Define a wiring string that includes all printable ASCII characters
wiring = string.printable

rotors = [
    Rotor(wiring, 0, 0),
    Rotor(wiring, 0, 0),
    Rotor(wiring, 0, 0),
    Rotor(wiring, 0, 0)
]

def generate_reciprocal_mapping(chars):
    # Shuffle the characters
    random.shuffle(chars)
    
    # Split the characters into two halves
    half_length = len(chars) // 2
    first_half = chars[:half_length]
    second_half = chars[half_length:]
    
    # Create a reciprocal mapping between the two halves
    mapping = {first_half[i]: second_half[i] for i in range(half_length)}
    mapping.update({second_half[i]: first_half[i] for i in range(half_length)})
    
    # Create a string of characters according to the mapping
    wiring = ''.join([mapping[char] for char in chars])
    
    return wiring

# Create a list of all printable ASCII characters
all_chars = list(string.digits + string.ascii_letters + string.punctuation)

# Generate a reciprocal mapping
reflector_wiring = generate_reciprocal_mapping(all_chars)

reflector = Reflector(reflector_wiring)
enigma = Enigma(plugboard, rotors, reflector)

adaptive_enigma = AdaptiveEnigma(enigma)

# Encrypt a message
plaintext = "message1"
plaintext = plaintext.replace(" ", "").upper()
print(f"Original Text: {plaintext}")
ciphertext = "".join(adaptive_enigma.encrypt(char) for char in plaintext)
print(f"Ciphertext: {ciphertext}")

# Reset the machine to its initial state before decrypting
adaptive_enigma.reset()

# Decrypt the message
decrypted_text = "".join(adaptive_enigma.decrypt(char) for char in ciphertext[:len(plaintext)])
print(f"Decrypted text: {decrypted_text}")
