# libraries
import pygame
from keyboard import Keyboard
from plugboard import Plugboard
from reflector import Reflec
from rotor import Rotor
from enigma import Enigma
from draw import draw_enigma as draw
from buttons import Button
import sys

# setup pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("ENIGMA SIMULATION")

# create fonts
BOLD = pygame.font.SysFont("FreeMono", 20, bold=True)
MONO = pygame.font.SysFont("FreeMono", 20)
TEXT_FONT = pygame.font.SysFont("FreeMono", 18)
TITLE_FONT = pygame.font.SysFont("FreeMono", 30, bold=True)

# global descriptions
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGTH = infoObject.current_h
SCREEN = pygame.display.set_mode((WIDTH, HEIGTH))
MARGINS = {"top": 175, "bottom": 100, "left": 100, "right": 100}
GAP = 100
PATH = []

INPUT = ""
OUTPUT = ""

caps = False
# button description
info_img = pygame.image.load('../img/info.png').convert_alpha()

# historical Enigma rotors ve reflectors on WİKİPEDİA
I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflec("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflec("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflec("FVPJIAOYEDRZXWGCTKUQSBNMHL")

# descriptions the keyboard and plugboard values
KB = Keyboard()
PB = Plugboard(["AR", "GK", "OX"])
counter = 0
# creating ENİGMA machine with Enigma class
ENIGMA = Enigma(B, I, II, III, PB, KB)
# Rotor start
ENIGMA.set_key("AAA")

# Rings setting
ENIGMA.set_rings((1, 1, 1))


def multilineRender(screen, text, x, y, the_font, colour=(128, 128, 128), justification="left"):
    justification = justification[0].upper()
    text = text.strip().replace('\r', '').split('\n')
    max_width = 0
    text_bitmaps = []
    # Convert all the text into bitmaps, calculate the justification width
    for t in text:
        text_bitmap = the_font.render(t, True, colour)
        text_width = text_bitmap.get_width()
        text_bitmaps.append((text_width, text_bitmap))
        if (max_width < text_width):
            max_width = text_width
    # Paint all the text bitmaps to the screen with justification
    for (width, bitmap) in text_bitmaps:
        xpos = x
        width_diff = max_width - width
        if (justification == 'R'):  # right-justify
            xpos = x + width_diff
        elif (justification == 'C'):  # centre-justify
            xpos = x + (width_diff // 2)
        screen.blit(bitmap, (xpos, y))
        y += bitmap.get_height()


def main_menu():
    global INPUT, OUTPUT, PATH, caps, counter
    language_is_eng = True
    language_btn_img = "../img/eng.png"
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        # background color
        SCREEN.fill("#272626")

        # text input
        text_in = BOLD.render(INPUT, True, "white ")
        text_box = text_in.get_rect(center=(WIDTH / 2, MARGINS["top"] / 3))

        SCREEN.blit(text_in, text_box)
        # buttons
        info_button = Button(WIDTH - 105, 3, pygame.image.load("../img/info.png"), 45, 45)
        close_button = Button(WIDTH - 60, 10, pygame.image.load("../img/close.png"), 30, 30)
        language_button = Button(WIDTH - 145, 10, pygame.image.load(language_btn_img), 30, 30)

        for button in [info_button, close_button, language_button]:
            button.update(SCREEN)

        # text output
        text_out = BOLD.render(OUTPUT, True, "red")
        text_box = text_out.get_rect(center=(WIDTH / 2, MARGINS["top"] / 3 + 25))
        SCREEN.blit(text_out, text_box)

        # draw enigma machine  x y w h
        draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGTH, MARGINS, GAP, BOLD)

        # Keyboard controls and rotate controls
        for event in pygame.event.get():
            # keyboard events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    II.rotate()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    INPUT += " "
                    OUTPUT += " "
                elif event.key == pygame.K_BACKSPACE:
                    INPUT = ""
                    OUTPUT = ""
                    III.de_rotate(counter)
                    counter = 0
                elif event.key == pygame.K_LALT \
                        or event.key == pygame.K_TAB \
                        or event.key == pygame.K_LSHIFT \
                        or event.key == pygame.K_LCTRL \
                        or event.key == pygame.K_LSUPER \
                        or event.key == pygame.K_PRINTSCREEN:
                    pass
                elif event.key == pygame.K_CAPSLOCK:
                    if caps:
                        caps = False
                    else:
                        caps = True
                else:
                    counter += 1
                    key = event.unicode
                    if caps:
                        if key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                            letter = key.upper()
                            INPUT = INPUT + letter
                            PATH, cipher = ENIGMA.encipher(letter)
                            OUTPUT += cipher
                    elif not caps:
                        if key in "abcdefghijklmnoprstuvwxyz":
                            letter = key.upper()
                            INPUT = INPUT + letter
                            PATH, cipher = ENIGMA.encipher(letter)
                            OUTPUT += cipher
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if info_button.checkForInput(MENU_MOUSE_POS):
                    if language_is_eng:
                        Info_screen_eng()
                    else:
                        Info_screen_tr()
                elif language_button.checkForInput(MENU_MOUSE_POS):
                    if language_is_eng:
                        language_is_eng = False
                        language_btn_img = "../img/tr.png"
                        print("dil eng")
                    else:
                        language_is_eng = True
                        language_btn_img = "../img/eng.png"
                        print("dil tr")


                elif close_button.checkForInput(MENU_MOUSE_POS):
                    sys.exit()

        pygame.display.update()


def Info_screen_tr():

    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#272626")

        OPTIONS_BACK = Button(20, 20, pygame.image.load("../img/back.png"), 30, 30)

        # Application name
        message = TITLE_FONT.render("ENIGMA SIMULATION", True, "white")
        text_box = message.get_rect(center=(WIDTH / 2, 20))

        SCREEN.blit(message, text_box)
        # Info text upload
        text = open("information_tr.txt", "r", encoding="utf-8")
        text_read = text.read()

        multilineRender(SCREEN, text_read, 30, 100, TEXT_FONT, "white")

        # Enigma machine photo
        enigma1_png = pygame.transform.scale(pygame.image.load("../img/enigma1.png"), (300, 400))
        enigma2_png = pygame.transform.scale(pygame.image.load("../img/enigma2.png"), (300, 400))
        SCREEN.blit(enigma1_png, (1200, 450))
        SCREEN.blit(enigma2_png, (850, 450))
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()




def Info_screen_eng():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("#272626")

        OPTIONS_BACK = Button(20, 20, pygame.image.load("../img/back.png"), 30, 30)

        # Application name
        message = TITLE_FONT.render("ENIGMA SIMULATION", True, "white")
        text_box = message.get_rect(center=(WIDTH / 2, 20))

        SCREEN.blit(message, text_box)
        # Info text upload
        text = open("information_eng.txt", "r", encoding="utf-8")
        text_read = text.read()

        multilineRender(SCREEN, text_read, 30, 100, TEXT_FONT, "white")

        # Enigma machine photo
        enigma1_png = pygame.transform.scale(pygame.image.load("../img/enigma1.png"), (300, 400))
        enigma2_png = pygame.transform.scale(pygame.image.load("../img/enigma2.png"), (300, 400))
        SCREEN.blit(enigma1_png, (1200, 450))
        SCREEN.blit(enigma2_png, (850, 450))
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


main_menu()
