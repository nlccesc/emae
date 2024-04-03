class Rotor:
    def __init__(self, wiring, ring_setting, initial_position, notch_positions=None):
        self.wiring = wiring
        self.inverse_wiring = ''.join(chr(i + ord('A')) for i in sorted(range(26), key=wiring.__getitem__))
        self.ring_setting = ring_setting % 26  # Ensure ring_setting is within 0-25
        self.position = initial_position % 26  # Ensure initial_position is within 0-25
        self.notch_positions = notch_positions if notch_positions is not None else []

    def process(self, char, reverse=False):
        if not char.isalpha() or not char.isupper():
            raise ValueError("Rotor can only process uppercase alphabetic characters.")
        
        wiring = self.inverse_wiring if reverse else self.wiring
        # Adjust for ring setting and position
        index = (ord(char) - ord('A') + self.position - self.ring_setting) % 26
        result = wiring[index]
        # Reverse the adjustment for ring setting and position
        unshifted_index = (ord(result) - ord('A') - self.position + self.ring_setting) % 26
        return chr(unshifted_index + ord('A'))

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position in self.notch_positions  # Return True if the rotor hits a notch position

    def set_position(self, position):
        self.position = position % 26

    def set_ring_setting(self, setting):
        self.ring_setting = setting % 26
