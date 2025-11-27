# зробити ворога:
# створити для нього функцію bot_random_move
# додати кількох ворогів
# зробити колізію куль
# зробити отримання урону та вихід з гри для гравця
# а потім і для ворогів

# зробити стіни:
# створити клас для них під назвою Walls
# реалізувати колізію

# зробити меню:
# створити головне меню
# додати кнопку Start
# у грі, якщо натиснути клавішу Esc, має бути пауза
# у паузі можна повернутися в головне меню
# якщо у паузі знову натиснути Esc — гра продовжиться

# зробити класи для раундів:
# додати покращення характеристик гравця після кожного раунду
    # створити список покращень
    # випадково вибирати покращення зі списку
# зробити ануляцію покращень після програшу

# додати музику та звуки

# організувати код:
# зробити відступи у своєму стилі
# змінити назви змінних
# додати коментарі
# https://github.com/RuslanFedorov303/roglike.git


from classes import *



player_img = pygame.image.load("Green_tank.png")
player_image = small_image = pygame.transform.scale(player_img, (70, 70))
player = Entiti(0, 200, 30, 30, player_image, 100, 30, "right")


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

    for bullet in bullets:
        if len(bullets) > 99:
            del bullets[0]
        bullet.update()
        bullet.draw(screen)


    # оновлення дисплея
    pygame.display.flip()
    clock.tick(50)


pygame.quit()