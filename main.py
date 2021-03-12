import pygame
import sys

width = 600
height = 400

sc = pygame.display.set_mode((width, height))

idle = pygame.image.load("image/idle.png")
idle = pygame.transform.scale(idle, (64, 64))

# Схема карты
# 0 - фон
# 1 - черный блок
# 55 - Персонаж


lvl = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
)
player = {
    "cord": {
        "speed": 2,
        "x": 128,
        "y": 128
    },
    "camera": {
        "x": 0,
        "y": 0
    },
    "move": {
        "top": True,
        "bottom": True,
        "left": True,
        "right": True
    }
}


def collision(shiftX, shiftY):
    global lvl
    global player

    for y, line in enumerate(lvl):
        for x, typ in enumerate(line):

            if typ == 1:
                objBlock = {
                    "left": (x * 64) + player["camera"]["x"],
                    "right": (x * 64) + player["camera"]["x"] + 64,
                    "top": (y * 64) + player["camera"]["y"],
                    "bottom": (y * 64) + player["camera"]["y"] + 64,
                }
                if player["cord"]["x"] + 64 + shiftX >= objBlock["left"] and \
                        player["cord"]["x"] + shiftX <= objBlock["right"] and \
                        player["cord"]["y"] + shiftY <= objBlock["bottom"] and \
                        player["cord"]["y"] + 64 + shiftY >= objBlock["top"]:
                    return False
    return True


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill((255, 255, 255))

    for y, line in enumerate(lvl):
        for x, typ in enumerate(line):
            if typ == 1:
                pygame.draw.rect(sc, (0, 0, 0),
                                 ((x * 64) + player["camera"]["x"], (y * 64) + player["camera"]["y"], 64, 64))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if player["cord"]["y"] >= 0 + 50:
            if collision(0, player["cord"]["speed"] * -1):
                player["cord"]["y"] -= player["cord"]["speed"]
        else:
            if collision(0, player["cord"]["speed"] * -1):
                player["camera"]["y"] += player["cord"]["speed"]

    if keys[pygame.K_s]:
        if player["cord"]["y"] + 64 <= height - 50:
            if collision(0, player["cord"]["speed"]):
                player["cord"]["y"] += player["cord"]["speed"]
        else:
            if collision(0, player["cord"]["speed"]):
                player["camera"]["y"] -= player["cord"]["speed"]

    if keys[pygame.K_a]:
        if player["cord"]["x"] >= 0 + 50:
            if collision(player["cord"]["speed"] * -1, 0):
                player["cord"]["x"] -= player["cord"]["speed"]
        else:
            if collision(player["cord"]["speed"] * -1, 0):
                player["camera"]["x"] += player["cord"]["speed"]

    if keys[pygame.K_d]:
        if player["cord"]["x"] + 64 <= width - 50:
            if collision(player["cord"]["speed"], 0):
                player["cord"]["x"] += player["cord"]["speed"]
        else:
            if collision(player["cord"]["speed"], 0):
                player["camera"]["x"] -= player["cord"]["speed"]

    # Ускорение
    if keys[pygame.K_LSHIFT]:
        player["cord"]["speed"] = 6
    else:
        player["cord"]["speed"] = 2

    sc.blit(idle, (player["cord"]["x"], player["cord"]["y"]))

    pygame.display.update()
    pygame.time.delay(25)
