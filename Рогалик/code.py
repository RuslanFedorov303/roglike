import pygame.font
from classes import *



player_img = pygame.image.load("Green_tank.png")
player_image = pygame.transform.scale(player_img, (70, 70))
player = Entiti(0, 200, 30, 30, player_image, 10000, 30, "green", "right")


tank_img = pygame.image.load("Red_tank.png")
tank_image = pygame.transform.scale(tank_img, (70, 70))
# tank1 = Bot(1000, 200, 30, 30, tank_image, 100, 30, "red")
# tank2 = Bot(1000, 300, 30, 30, tank_image, 100, 30, "red")
# tank3 = Bot(1000, 400, 30, 30, tank_image, 100, 30, "red")




wall_img = pygame.image.load("Wall.png")
wall_image = pygame.transform.scale(wall_img, (40, 40))
wall1 = Object(500, 300, 1, 1, wall_image)

walls = [wall1]


img_fon = pygame.image.load("BG.jpg")
fon = Object(0, 0, 1000, 1000, img_fon)



# button_menu = Button(600, 350, "Вийти в меню", 40)


tanks = [
    [1000, 200, 30, 30, tank_image, 100, 30, "red"],
    [1000, 300, 30, 30, tank_image, 100, 30, "red"],
    [1000, 400, 30, 30, tank_image, 100, 30, "red"]
]

round1 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 30, "red"],
    [1000, 300, 30, 30, tank_image, 100, 30, "red"],
    [1000, 400, 30, 30, tank_image, 100, 30, "red"],
    [800, 200, 30, 30, tank_image, 100, 30, "red"],
    [800, 300, 30, 30, tank_image, 100, 30, "red"],
    [800, 400, 30, 30, tank_image, 100, 30, "red"]
    ],
    (
    (500, 300),
    (500, 350),
    (500, 400),
    (500, 450),
    (500, 500)
    ), player, fon, wall_image, player_image)


round2 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 30, "red"],
    [1000, 300, 30, 30, tank_image, 100, 30, "red"],
    [1000, 400, 30, 30, tank_image, 100, 30, "red"]
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


round3 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 30, "red"]
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


button_start = Button(600, 300, "START", 50)
button_start.onclick(round3.game())

player.bufs = []


running = True
while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # game_part_round()
    fon.draw(screen)

    button_start.update()
    button_start.draw(screen)

    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(50)



pygame.quit()
