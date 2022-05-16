import pygame

class Rotor:

    def __init__(self, wiring, notch):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rigth = wiring
        self.notch = notch

    def forward(self, signal):
        letter = self.rigth[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.rigth.find(letter)
        return signal

    def rotate(self, n=1, forward=True):
        for i in range(n):
            if forward:
                self.left = self.left[1:]+self.left[0]
                self.rigth = self.rigth[1:]+self.rigth[0]
            else:
                self.left = self.left[25]+self.left[:25]
                self.rigth = self.rigth[25]+self.rigth[:25]

    def de_rotate(self, counter, forward=True):
        for i in range(counter):
            if not forward:
                self.left = self.left[1:]+self.left[0]
                self.rigth = self.rigth[1:]+self.rigth[0]
            else:
                self.left = self.left[25]+self.left[:25]
                self.rigth = self.rigth[25]+self.rigth[:25]



    def rotate_to_letter(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, n):

        # rotate rotor backward
        self.rotate(n-1, forward=False)

        # adjust the turnover natch in relationship to the wiring
        n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(self.notch)
        self.notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch-n) % 26]

    def draw(self, sc, x, y, w, h, font):

        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(sc, "white", r, width=2, border_radius=18)

        # letters
        for i in range(26):

            # left hand side
            letter = self.left[i]
            letter = font.render(letter, True, "grey ")
            text_box = letter.get_rect(center=(x+w/4, y+(i+1)*h/27))

            # highlight top letter
            if i == 0:
                pygame.draw.rect(sc, "teal", text_box, border_radius=3)

            # highlight top turnover notch
            if self.left[i] == self.notch:
                letter = font.render(self.notch, True, "#333333")
                pygame.draw.rect(sc, "white", text_box, border_radius=3)

            sc.blit(letter, text_box)

            # rigth hand side
            letter = self.rigth[i]
            letter = font.render(letter, True, "grey ")
            text_box = letter.get_rect(center=(x+w*3/4, y+(i+1)*h/27))
            sc.blit(letter, text_box)
