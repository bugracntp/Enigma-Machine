import pygame

class Plugboard:
    def __init__(self, pairs):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rigth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pair in pairs:
            A = pair[0]
            B = pair[1]
            pos_A = self.left.find(A)
            pos_B = self.left.find(B)
            self.left = self.left[:pos_A] + B + self.left[pos_A+1:]
            self.left = self.left[:pos_B] + A + self.left[pos_B+1:]

    def forward(self, signal):
        letter = self.rigth[signal]
        signal = self.left.find(letter)
        return signal

    def backward(self, signal):
        letter = self.left[signal]
        signal = self.rigth.find(letter)
        return signal

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
            sc.blit(letter, text_box)

            # rigth hand side
            letter = self.rigth[i]
            letter = font.render(letter, True, "grey ")
            text_box = letter.get_rect(center=(x+w*3/4, y+(i+1)*h/27))
            sc.blit(letter, text_box)

