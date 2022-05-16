"""
kullanıcıdan alınan harflerin ve indeksleri rahatca bulabilmek için kullanılan class

"""
import pygame
class Keyboard:

    def forward(self, letter):  # klavyeden gelen harflerin indexsini aldık
        signal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        return signal

    def backward(self, signal):  # gelen indekse denk gelen harfleri döndürdük
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[signal]
        return letter

    def draw(self, sc, x, y, w, h, font):

        # rectangle
        r = pygame.Rect(x, y, w, h)
        pygame.draw.rect(sc, "white", r, width=2, border_radius=18)

        # letters
        for i in range(26):
            letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i]
            letter = font.render(letter, True, "grey ")
            text_box = letter.get_rect(center=(x+w/2, y+(i+1)*h/27))
            sc.blit(letter, text_box)