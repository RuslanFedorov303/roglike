import random
import pygame
from classes import *



# ---------- Створюємо усі не обхідні картинки для гри ---------- #
player_img = pygame.image.load("Images/Green_tank.png")
player_image = pygame.transform.scale(player_img, (70, 70))
player = Entiti(0, 200, 30, 30, player_image, 1, 2, 300, "green", "right")
defoult_player = (player.hp, player.speed, player.damage)


tank_img1 = pygame.image.load("Images/Red_tank.png")
tank_image1 = pygame.transform.scale(tank_img1, (70, 70))


wall_img1 = pygame.image.load("Images/Wall.png")
wall_image1 = pygame.transform.scale(wall_img1, (40, 40))


fon_image1 = pygame.image.load("Images/BG.jpg")
fon1 = Object(-1, 0, 1000, 1000, fon_image1)

fon_image2 = pygame.image.load("Images/BG2.jpg")
fon2 = Object(-1, 0, 1000, 1000, fon_image2)

fon_image3 = pygame.image.load("Images/BG3.png")
# fon_image3 = pygame.transform.scale(fon_image3, (1200, 700))
fon3 = Object(0, 0, 1000, 1000, fon_image3)

# fon_image4 = pygame.image.load("Images/BG4.jpg")
# fon4 = Object(-1, 0, 1000, 1000, fon_image4)


tree_img1 = pygame.image.load("Images/Tree.png")
tree_image1 =  pygame.transform.scale(tree_img1, (100, 100))

tree_img2 = pygame.image.load("Images/Tree2.png")
tree_image2 =  pygame.transform.scale(tree_img2, (100, 100))

tree_img3 = pygame.image.load("Images/Tree3.png")
tree_image3 =  pygame.transform.scale(tree_img3, (100, 100))

tree_img4 = pygame.image.load("Images/Tree4.png")
tree_image4 =  pygame.transform.scale(tree_img1, (100, 100))



# ---------- Створюємо раунди для гри ---------- #
round1 = Round(
    [
        (1000, 200, 30, 30, tank_image1, 100, 1.5, 30, "red", "left")
    ],
    (
        (500, 300),
        (500, 340),
        (500, 380),
        (500, 420),
        (500, 460)
    ),
    (
        (300, 200, 35, tree_image2),
        (400, 150, 35, tree_image3),
        (330, 400, 35, tree_image4)
    ),
    player, fon3, wall_image1, player_image)



bufs = {
    "hp":     (10, 15, 20, 30, 70, 80, 110, 150, 200),
    "speed":  (1, 1.5, 2, 2.5, 3),
    "damage": (10, 20, 30, 40, 50, 70)
}



game1 = Game([round1], bufs, fon1, player, defoult_player)



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