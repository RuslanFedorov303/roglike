from classes import *



player_img = pygame.image.load("Green_tank.png")
player_image = pygame.transform.scale(player_img, (70, 70))
player = Entiti(0, 200, 30, 30, player_image, 100, 30, "right")


tank_img = pygame.image.load("Red_tank.png")
tank_image = pygame.transform.scale(tank_img, (70, 70))
tank1 = Bot(1000, 200, 30, 30, tank_image, 100, 30, 'red')
tank2 = Bot(1000, 300, 30, 30, tank_image, 100, 30, 'red')
tank3 = Bot(1000, 400, 30, 30, tank_image, 100, 30, 'red')

all_tanks = [player, tank1, tank2, tank3]
tanks =[tank1, tank2, tank3]


wall_img = pygame.image.load("Wall.png")
wall_image = pygame.transform.scale(wall_img, (40, 40))
wall1 = Object(500, 300, 30, 30, wall_image)

walls = [wall1]


img_fon = pygame.image.load("BG.jpg")
fon = Object(0, 0, 1000, 1000, img_fon)


screen = pygame.display.set_mode((1300, 700))
clock = pygame.time.Clock()



running = True
while running:
    # обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shot(player.directore)


    # відображення
    if player.hp <= 0:
        running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        new_img = pygame.transform.rotate(player_image, 180)
        player.img = new_img
        player.rect.x -= 3
        player.directore = "left"

    if keys[pygame.K_d]:
        new_img = pygame.transform.rotate(player_image, 0)
        player.img = new_img
        player.rect.x += 3
        player.directore = "right"

    if keys[pygame.K_w]:
        new_img = pygame.transform.rotate(player_image, 90)
        player.img = new_img
        player.rect.y -= 3
        player.directore = "up"

    if keys[pygame.K_s]:
        new_img = pygame.transform.rotate(player_image, 270)
        player.img = new_img
        player.rect.y += 3
        player.directore = "down"


    fon.draw(screen)
    player.draw(screen)


    for tank in tanks:
        if not tank.hp <= 0:
            tank.bot_random_rotate()
            tank.collide_bullets(bullets, all_tanks)
            tank.shot(tank.directore)
            tank.draw(screen)


    for bullet in bullets:
        if len(bullets) > 99:
            del bullets[0]
        bullet.update()
        bullet.draw(screen)


    for wall in walls:
        wall.draw(screen)

    # оновлення дисплея
    pygame.display.flip()
    clock.tick(50)


pygame.quit()
