import random
import pygame
from classes import *



player_img = pygame.image.load("Green_tank.png")
player_image = pygame.transform.scale(player_img, (70, 70))
# player_defoult[0, 200, 30, 30, player_image, 100, 2, 1000, "green", "right"]
player = Entiti(0, 200, 30, 30, player_image, 100, 2, 1000, "green", "right")


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



round1 = Round(
    [
    [1000, 200, 30, 30, tank_image, 100, 1.5, 30, "red", "left"],
    [1000, 300, 30, 30, tank_image, 100, 2, 30, "red", "left"]
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
        "hp": 10,
        "hp": 70,
        "hp": 110,
        "hp": 200,

        "speed": 1,
        "speed": 2,
        "speed": 3,

        "damage": 10,
        "damage": 20,
        "damage": 30,
        "damage": 70
}



game = Game([round1, round2, round3, round2], bufs, fon, player)
game.csicle()


button_start = Button(600, 300, "START", 50)
button_start.onclick(round1.game())


running = True
while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    fon.draw(screen)

    win1, win2, win3 = False, False, False

    button_start.update()
    win1 = round1.game()
    if win1:
        buf, buf2 = random.choice(list(bufs.items()))
        print(buf, buf2)
        if buf == "hp":     player.hp += buf2
        if buf == "speed":  player.speed += buf2
        if buf == "damage": player.damage += buf2

        win2 = round2.game()
        if win2:
            buf, buf2 = random.choice(list(bufs.items()))
            print(buf, buf2)
            if buf == "hp":     player.hp += buf2
            if buf == "speed":  player.speed += buf2
            if buf == "damage": player.damage += buf2

            win3 = round1.game()

    # оновлення дисплея та обмеження частоти
    pygame.display.flip()
    clock.tick(50)



pygame.quit()
