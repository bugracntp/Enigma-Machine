import pygame

class Reflec:

    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.rigth = wiring

    def reflect(self, signal):
        letter = self.rigth[signal]
        signal = self.left.find(letter)
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




