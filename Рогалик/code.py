import random
import pygame
from classes import *



# ---------- Створюємо все не обхідне для гри ---------- #
player_img = pygame.image.load("Green_tank.png")
player_image = pygame.transform.scale(player_img, (70, 70))
player = Entiti(0, 200, 30, 30, player_image, 100, 2, 30, "green", "right")
player.max_hp = player.hp


tank_img = pygame.image.load("Red_tank.png")
tank_image = pygame.transform.scale(tank_img, (70, 70))


wall_img = pygame.image.load("Wall.png")
wall_image = pygame.transform.scale(wall_img, (40, 40))


img_fon = pygame.image.load("BG.jpg")
fon = Object(0, 0, 1000, 1000, img_fon)



# ---------- Створюємо саму гру ---------- #
round1 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 1.5, 30, "red", "left"]
    ],
    (
    (500, 300),
    (500, 340),
    (500, 380),
    (500, 420),
    (500, 460)
    ), player, fon, wall_image, player_image)



round2 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 3, 30, "red", "left"],
    [1000, 300, 30, 30, tank_image, 100, 3, 30, "red", "left"],
    [1000, 400, 30, 30, tank_image, 100, 4, 30, "red", "left"]
    ],
    (
    (500, 300),
    (500, 340),
    (500, 380),
    (500, 420),
    (550, 460)
    ), player, fon, wall_image, player_image)



round3 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 3, 30, "red", "left"],
    [1000, 200, 30, 30, tank_image, 100, 3, 30, "red", "left"],
    [1000, 200, 30, 30, tank_image, 100, 4, 30, "red", "left"],
    [1000, 200, 30, 30, tank_image, 100, 5, 30, "red", "left"]
    ],
    (
    (500, 300),
    (500, 350),
    (500, 400),
    (500, 450),
    (550, 300),
    (550, 350),
    (550, 400),
    (550, 450),
    (600, 300),
    (600, 350),
    (600, 400),
    (600, 450)
    ), player, fon, wall_image, player_image)



bufs = {
    "hp": [10, 30, 70, 80, 110, 150, 200],
    "speed": [1, 1.5, 2, 2.5, 3],
    "damage": [10, 20, 30, 40, 50, 70]
}



game1 = Game([round1, round2, round3], bufs, fon, player)



button_start = Button(550, 300, "START", 200)
button_start.onclick(game1.cycle)



# ---------- Меню ---------- #
running = True
while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        button_start.update(event)

    fon.draw(screen)
    button_start.draw(screen)


    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(50)



pygame.quit()
