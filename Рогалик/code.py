import random
import pygame
from classes import *



# ---------- Створюємо усі не обхідні картинки для гри ---------- #
# Player
player_img = pygame.image.load("Images/Green_tank.png")
player_image = pygame.transform.scale(player_img, (70, 70))
player = Entiti(50, 320, 30, 30, player_image, 100, 2, 30, "green", "right")
defoult_player = (player.hp, player.speed, player.damage)


# Танки
tank_img1 = pygame.image.load("Images/Red_tank.png")
tank_image1 = pygame.transform.scale(tank_img1, (70, 70))

tank_img2 = pygame.image.load("Images/Red_tank2.png")
tank_image2 = pygame.transform.scale(tank_img2, (70, 70))

tank_img3 = pygame.image.load("Images/Red_tank3.png")
tank_image3 = pygame.transform.scale(tank_img3, (70, 70))

tank_img4 = pygame.image.load("Images/Red_tank4.png")
tank_image4 = pygame.transform.scale(tank_img4, (70, 70))

tank_img5 = pygame.image.load("Images/Red_tank5.png")
tank_image5 = pygame.transform.scale(tank_img5, (70, 70))


wall_img1 = pygame.image.load("Images/Wall.png")
wall_image1 = pygame.transform.scale(wall_img1, (40, 40))


# Фони
fon_image1 = pygame.image.load("Images/BG.jpg")
fon1 = Object(-1, 0, 1000, 1000, fon_image1)

fon_image2 = pygame.image.load("Images/BG2.jpg")
fon2 = Object(-1, 0, 1000, 1000, fon_image2)

fon_image3 = pygame.image.load("Images/BG3.jpg")
fon_image3 = pygame.transform.scale(fon_image3, (1300, 700))
fon3 = Object(0, 0, 1000, 1000, fon_image3)

fon_image4 = pygame.image.load("Images/BG4.png")
fon4 = Object(-1, 0, 1000, 1000, fon_image4)


tree_img1 = pygame.image.load("Images/Tree.png")
tree_image1 =  pygame.transform.scale(tree_img1, (100, 100))

tree_img2 = pygame.image.load("Images/Tree2.png")
tree_image2 =  pygame.transform.scale(tree_img2, (100, 100))

tree_img3 = pygame.image.load("Images/Tree3.png")
tree_image3 =  pygame.transform.scale(tree_img3, (100, 100))

tree_img4 = pygame.image.load("Images/Tree4.png")
tree_image4 =  pygame.transform.scale(tree_img4, (100, 100))



# ---------- Створюємо раунди для гри ---------- #
round1 = Round(
    [
        (1000, 200, 20, 20, tank_image1, 100, 1.5, 30, "red", "left")
    ],
    (
        (500, -40),
        (500, 0),
        (500, 40),
        (500, 80),
        (500, 120),
        (500, 160),
        (800, 500),
        (800, 540),
        (800, 580),
        (800, 620),
        (800, 660),
        (800, 700)
    ),
    (
        (500, 170, 35, tree_image1),
        (600, 500, 125, tree_image1),
        (680, 520, 190, tree_image1),
        (650, 250, 220, tree_image1)
    ),
    player, fon1, wall_image1, player_image)


round2 = Round(
    [
        (1000, 200, 30, 30, tank_image1, 100, 2, 50, "red", "left"),
        (1000, 300, 30, 30, tank_image1, 150, 2, 40, "red", "left")
    ],
    (
        (460, 460),
        (500, 300),
        (500, 340),
        (500, 380),
        (500, 420),
        (500, 460),
        (540, 300),
        (580, 300),
        (620, 300),
        (660, 300),
        (700, 300),
        (700, 340),
        (700, 380),
        (700, 420)
    ),
    (
        (300, 200, 35, tree_image1),
        (400, 150, 125, tree_image1),
        (330, 400, 265, tree_image1),
        (580, 380, 345, tree_image1)
    ),
    player, fon1, wall_image1, player_image)


round3 = Round(
    [
        (1000, 200, 30, 30, tank_image1, 150, 4, 50, "red", "left"),
        (1000, 300, 30, 30, tank_image2, 200, 3, 70, "red", "left")
    ],
    (
        (400, 300),
        (440, 300),
        (480, 300),
        (520, 300),
        (560, 300),
        (600, 300),
        (640, 300),
        (640, 260),
        (640, 220),
        (640, 180),
        (640, 140),
        (800, 640),
        (800, 600),
        (800, 560),
        (800, 520),
        (760, 520)
    ),
    (
        (300, 200, 35, tree_image1),
        (400, 150, 125, tree_image2),
        (330, 400, 265, tree_image2),
        (580, 380, 345, tree_image2),
        (1000, 600, 325, tree_image1),
        (800, 400, 155, tree_image2),
        (730, 180, 165, tree_image2),
        (880, 90, 365, tree_image2)
    ),
    player, fon2, wall_image1, player_image)


round4 = Round(
    [
        (1000, 200, 30, 30, tank_image2, 150, 4, 70, "red", "left"),
        (1000, 300, 30, 30, tank_image2, 200, 3, 70, "red", "left"),
        (1000, 400, 30, 30, tank_image4, 250, 4, 100, "red", "left")
    ],
    (
        (400, 300),
        (440, 300),
        (480, 300),
        (520, 300),
        (560, 300),
        (600, 300),
        (640, 300),
        (640, 260),
        (640, 220),
        (640, 180),
        (640, 140),
        (360, 220),
        (320, 220),
        (280, 220),
        (240, 220)
    ),
    (
        (370, 250, 135, tree_image2),
        (480, 170, 125, tree_image1),
        (360, 430, 265, tree_image1),
        (530, 340, 145, tree_image2),
        (500, 520, 125, tree_image2),
        (840, 430, 145, tree_image1),
        (720, 140, 175, tree_image2),
        (890, 90, 325, tree_image2)
    ),
    player, fon2, wall_image1, player_image)


round5 = Round(
    [
        (1000, 200, 30, 30, tank_image4, 250, 4, 100, "red", "left"),
        (1000, 300, 30, 30, tank_image5, 400, 2, 200, "red", "left"),
        (1000, 400, 30, 30, tank_image4, 250, 4, 100, "red", "left")
    ],
    (
        (400, 400),
        (400, 440),
        (500, 100),
        (500, 140),
        (300, 240),
        (300, 280)
    ),
    (
        (370, 250, 135, tree_image1),
        (900, 200, 155, tree_image3),
        (500, 400, 235, tree_image4),
        (200, 230, 135, tree_image3),
        (830, 290, 155, tree_image1),
        (700, 140, 235, tree_image4),
        (330, 290, 195, tree_image1),
        (350, 460, 185, tree_image1)
    ),
    player, fon3, wall_image1, player_image)


round6 = Round(
    [
        (1000, 200, 30, 30, tank_image4, 250, 4, 100, "red", "left"),
        (1000, 300, 30, 30, tank_image5, 400, 2, 200, "red", "left"),
        (1000, 400, 30, 30, tank_image2, 200, 3, 130, "red", "left"),
        (1000, 500, 30, 30, tank_image3, 450, 2, 150, "red", "left")
    ],
    (
        (400, 100),
        (400, 180),
        (400, 260),
        (400, 340),
        (400, 420),
        (400, 500)
    ),
    (
        (370, 250, 135, tree_image1),
        (350, 460, 185, tree_image1),
        (200, 230, 135, tree_image1),
        (830, 290, 155, tree_image1),
        (330, 290, 195, tree_image3),
        (500, 400, 235, tree_image3),
        (900, 200, 155, tree_image4),
        (700, 140, 235, tree_image4)
    ),
    player, fon3, wall_image1, player_image)


round7 = Round(
    [
        (1000, 200, 30, 30, tank_image4, 250, 6, 100, "red", "left"),
        (1000, 300, 30, 30, tank_image5, 400, 2, 200, "red", "left"),
        (1000, 400, 30, 30, tank_image3, 500, 1, 150, "red", "left"),
        (1000, 500, 30, 30, tank_image3, 450, 2, 150, "red", "left")
    ],
    (
        (400, 100),
        (440, 100),
        (480, 100),
        (520, 100),
        (560, 100),
        (600, 100),
        (640, 100),
        (680, 100),
        (720, 100),

        (400, 500),
        (440, 500),
        (480, 500),
        (520, 500),
        (560, 500),
        (600, 500),
        (640, 500),
        (680, 500),
        (720, 500),

        (400, 60),
        (400, 20),
        (400, -20),
        (400, -60),
        (720, 60),
        (720, 20),
        (720, -20),
        (720, -60),

        (400, 540),
        (400, 580),
        (400, 620),
        (400, 660),
        (720, 540),
        (720, 580),
        (720, 620),
        (720, 660)
    ),
    (
        (370, 100, 135, tree_image1),
        (600, 40, 165, tree_image1),
        (460, 20, 195, tree_image1),
        (460, 600, 295, tree_image1),
        (770, 550, 55, tree_image1),
        (520, 450, 265, tree_image4),
        (680, 230, 155, tree_image4),
        (680, 580, 235, tree_image4),
        (940, 320, 185, tree_image4)
    ),
    player, fon4, wall_image1, player_image)


round8 = Round(
    [
        (1000, 200, 30, 30, tank_image4, 350, 8, 100, "red", "left"),
        (1000, 300, 30, 30, tank_image5, 500, 2, 250, "red", "left"),
        (1000, 400, 30, 30, tank_image3, 550, 1, 200, "red", "left"),
        (1000, 500, 30, 30, tank_image3, 550, 2, 200, "red", "left"),
        (1000, 600, 30, 30, tank_image5, 500, 2, 250, "red", "left")
    ],
    (
        (100, 320),
        (-999, -999)
    ),
    (
        (390, 100, 135, tree_image1),
        (400, 40, 165, tree_image1),
        (260, 20, 195, tree_image1),
        (480, 600, 295, tree_image1),
        (730, 550, 55, tree_image1),
        (520, 450, 265, tree_image4),
        (480, 230, 155, tree_image4),
        (620, 580, 235, tree_image4),
        (990, 320, 185, tree_image4)
    ),
    player, fon4, wall_image1, player_image)












bufs = {
    "hp":     (10, 15, 20, 30, 70, 80, 110, 150, 200),
    "speed":  (1, 1.5, 2, 2.5, 3),
    "damage": (10, 20, 30, 40, 50, 70)
}



game1 = Game([round1, round2, round3, round4, round5, round6, round7, round8], bufs, fon1, player, defoult_player)



button_start = Button(550, 300, "START", 200)
button_start.onclick(game1.cycle)



# ---------- Меню ---------- #
pygame.mixer.music.stop()
pygame.mixer.music.load("Sounds/1gloom - Flute Buzz.mp3")
pygame.mixer.music.play()
running = True


while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        button_start.update(event)

    fon1.draw(screen)
    button_start.draw(screen)


    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(50)



pygame.quit()