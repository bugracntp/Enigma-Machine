class Enigma:
    def __init__(self, re, r1, r2, r3, pb, kb):
        self.re = re
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.pb = pb
        self.kb = kb

    # Settings the rings
    def set_rings(self, rings):
        self.r1.set_ring(rings[0])
        self.r2.set_ring(rings[1])
        self.r3.set_ring(rings[2])

    # Setting the starting letters
    def set_key(self, key):
        self.r1.rotate_to_letter(key[0])
        self.r2.rotate_to_letter(key[1])
        self.r3.rotate_to_letter(key[2])

    # crtypting
    def encipher(self, letter):
        # rotorları döndürme
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.rotate()
            self.r2.rotate()
            self.r3.rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.rotate()
            self.r3.rotate()
        else:
            self.r3.rotate()

        # makineden sinyal geçirir
        signal = self.kb.forward(letter)
        path = [signal, signal]
        signal = self.pb.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.forward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.re.reflect(signal)
        path.append(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r1.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r2.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.r3.backward(signal)
        path.append(signal)
        path.append(signal)
        signal = self.pb.backward(signal)
        path.append(signal)
        path.append(signal)
        letter = self.kb.backward(signal)
        path.append(signal)
        path.append(signal)

        return path, letter

    def de_rotation(self):
        # rotorları döndürme
        if self.r2.left[0] == self.r2.notch and self.r3.left[0] == self.r3.notch:
            self.r1.de_rotate()
            self.r2.de_rotate()
            self.r3.de_rotate()
        elif self.r2.left[0] == self.r2.notch:
            self.r1.de_rotate()
            self.r2.de_rotate()
            self.r3.de_rotate()
        elif self.r3.left[0] == self.r3.notch:
            self.r2.de_rotate()
            self.r3.de_rotate()
        else:
            self.r3.de_rotate()