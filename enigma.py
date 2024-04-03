class Enigma:
    def __init__(self, plugboard, rotors, reflector):
        self.plugboard = plugboard
        self.rotors = rotors
        self.reflector = reflector

    def encrypt(self, char):
        for rotor in self.rotors:
            if rotor.rotate():
                break
        char = self.plugboard.process(char)
        for rotor in self.rotors:
            char = rotor.process(char)
        char = self.reflector.process(char)
        for rotor in reversed(self.rotors):
            char = rotor.process(char, reverse=True)
        char = self.plugboard.process(char)
        return char