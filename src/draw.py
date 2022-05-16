import pygame

# drawing the hole machine
def draw_enigma(enigma,  path, sc, width, heigth, mar, gap, font):
    TITLE_FONT = pygame.font.SysFont("FreeMono", 30, bold=True)
    massage_FONT = pygame.font.SysFont("FreeMono", 17, bold=True)

    # width and heigth of components
    w = (width - mar["left"] - mar["right"] - 5 * gap) / 6
    h = heigth - mar["top"] - mar["bottom"]

    # path coordinates
    y = [mar["top"]+(signal+1)*h/27 for signal in path] # y coordinates
    x = [width-mar["right"]-w/2] # keyboard

    for i in [4, 3, 2, 1, 0]: # forward pass
        x.append(mar["left"]+i*(w+gap)+w*3/4)
        x.append(mar["left"]+i*(w+gap)+w*1/4)

    x.append(mar["left"]+w/2) # reflector

    for i in [1, 2, 3, 4]: # backward pass
        x.append(mar["left"]+i*(w+gap)+w*1/4)
        x.append(mar["left"]+i*(w+gap)+w*3/4)

    x.append(width-mar["right"]-w/2) # lamboard

    # draw the path
    if len(path) > 0:
        for i in range(1, 21):
            if i < 10:
                color = "#43aa3b"
            elif i < 12:
                color = "#f9c74f"
            else:
                color = "#e63946"
            start = (x[i-1], y[i-1])
            end = (x[i], y[i])
            pygame.draw.line(sc, color, start, end, width=3)

    # base coordinates
    x = mar["left"]
    y = mar["top"]

    # draw enigma components
    for comp in [enigma.re, enigma.r1, enigma.r2, enigma.r3, enigma.pb, enigma.kb]:
        comp.draw(sc, x, y, w, h, font)
        x += w + gap

    # Applications messages

    # Application name
    x = width/2
    y = 20
    message = TITLE_FONT.render("ENIGMA SIMULATION", True, "white")
    text_box = message.get_rect(center=(x, y))
    sc.blit(message, text_box)

    # exit info
    x = width-300
    y = heigth-20
    message = massage_FONT.render("PRESS ESC BUTTON TO EXİT THE APP.", True, "white")
    text_box = message.get_rect(center=(x, y))
    sc.blit(message, text_box)

    # text cleaning info
    x = width - 300
    y = heigth - 40
    message= massage_FONT.render("PRESS BACKSPACE BUTTON TO DELLETE THE MESSAGE.", True, "white")
    text_box = message.get_rect(center=(x, y))
    sc.blit(message, text_box)


    # write the names of components
    names = ["Reflector", "Left", "Middle", "Right", "Plugboard", "Key/Lamb"]
    y = mar["top"]*0.8
    for i in range(len(names)):
        x = mar["left"] + w/2 + i*(w+gap)
        title = font.render(names[i], True, "white")
        text_box = title.get_rect(center=(x, y))
        sc.blit(title, text_box)



