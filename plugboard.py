import string

class PlugBoard:
    def __init__(self, cables):
        if not all(len(cable) == 2 and cable[0] != cable[1] for cable in cables):
            raise ValueError("Each cable must be a pair of distinct characters.")
        if len(set(char for cable in cables for char in cable)) != 2 * len(cables):
            raise ValueError("Cables must not overlap.")
        self.mapping = {c: c for c in string.ascii_uppercase}
        for cable in cables:
            a, b = cable
            self.mapping[a] = b
            self.mapping[b] = a
    
    def process(self, char):
        try:
            return self.mapping[char]
        except KeyError:
            raise ValueError(f"Invalid character: {char}")

    def process_string(self, s):
        return ''.join(self.process(char) for char in s)