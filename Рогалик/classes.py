import pygame
import random
import time



pygame.init()
screen = pygame.display.set_mode((1300, 700))
clock = pygame.time.Clock()




# ---------- Текст для гри ---------- #
class Label:
    def __init__(self, x, y, size, default_text="text" ,color="black"):
        self.font = pygame.font.Font(None, size)
        self.coord = (x, y)
        self.color = color
        self.set_text(default_text)



    def set_text(self, text):
        self.image = self.font.render(text, True, self.color)



    def draw(self, screen):
        screen.blit(self.image, self.coord)




# ---------- Кнопки для гри ---------- #
class Button:
    def __init__(self, x, y, text, w, color=(0, 0, 0)):
        self.rect_image = pygame.transform.scale(
            pygame.image.load("Button_no_activate.png").convert_alpha(),
            (w, w/2)
        )

        self.rect_image_active = pygame.transform.scale(
            pygame.image.load("Button_activate.png").convert_alpha(),
            (w, w/2)
        )

        self.rect = pygame.Rect(x, y, w, 50)
        self.color = color


        self.font = pygame.font.Font(None, w//6)
        self.text_image = self.font.render(text, True, self.color)
        self.text_rect = self.text_image.get_rect()

        self.text_rect.x = self.rect.x + 20
        self.text_rect.y = y + 5
        self.active = False
        self.fn = None



    def update(self, event):
        # перевірка наведення миші
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.active = True
        else:
            self.active = False

        # обробка кліку
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.active:
                if self.fn:
                    self.fn()



    def draw(self, surface):
        if self.active:
            surface.blit(self.rect_image_active, (self.rect.x, self.rect.y))

        else:
            surface.blit(self.rect_image, (self.rect.x, self.rect.y))
        surface.blit(self.text_image, (self.text_rect.x*1.04, self.text_rect.y*1.1))



    def set_text(self, new_text):
        self.text_image = self.font.render(new_text, True, self.color)



    def onclick(self, fn):
        self.fn = fn




# ---------- Базовий клас ---------- #
class Object:
    def __init__(self, x, y, width, height, img=""):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.img = img
        self.rect = pygame.Rect(x, y, self.width, self.height)



    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))




# ---------- Ентіті ---------- #
class Entiti(Object):
    def __init__(self, x, y, width, height, img="", hp=100, speed=3, damage=30, comand="red", defoult_directore="left"):
        super().__init__(x, y, width, height, img)
        self.hp = hp
        self.speed = speed
        self.damage = damage
        self.directore = defoult_directore
        self.comand = comand
        self.start_time = time.time()
        self.end_time = 0



    def shot(self, directore, list):
        self.end_time = time.time()
        duration = self.end_time - self.start_time

        if duration >= 0.7:
            if directore == 'up':      list.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "up", self.comand, self.damage, self.speed*2.5))
            elif directore == 'down':  list.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "down", self.comand, self.damage, self.speed*2.5))
            elif directore == 'left':  list.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "left", self.comand, self.damage, self.speed*2.5))
            elif directore == 'right': list.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "right", self.comand, self.damage, self.speed*2.5))
            self.start_time = time.time()
            return list



    def collide_bullets(self, bullets, list):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect) and bullet.comand != self.comand:
                self.hp -= bullet.damage
                list.remove(bullet)
        return list



    def collide_walls(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.directore == 'up':      self.rect.y += self.speed
                elif self.directore == 'down':  self.rect.y -= self.speed
                elif self.directore == 'left':  self.rect.x += self.speed
                elif self.directore == 'right': self.rect.x -= self.speed




# ---------- Вороги ---------- #
class Bot(Entiti):
    def __init__(self, x, y, width, height, img="", hp=100, speed=3, damage=30, comand="red", defoult_directore="left"):
        super().__init__(x, y, width, height, img, hp, speed, damage, comand, defoult_directore)
        self.start_time_botMove = time.time()
        self.end_time_botMove = 0
        self.directore = defoult_directore
        self.tank_image = img
        self.directories = ["up", "down", "left", "right"]



    def bot_random_rotate(self):
        self.end_time_botMove = time.time()
        duration = self.end_time_botMove - self.start_time_botMove


        if self.directore == 'up':
            if not self.rect.y < 0:
                self.rect.y -= self.speed

            new_img = pygame.transform.rotate(self.tank_image, 90)
            self.img = new_img


        elif self.directore == 'down':
            if not self.rect.y > 600:
                self.rect.y += self.speed

            new_img = pygame.transform.rotate(self.tank_image, 270)
            self.img = new_img


        elif self.directore == 'left':
            if not self.rect.x < 0:
                self.rect.x -= self.speed

            new_img = pygame.transform.rotate(self.tank_image, 180)
            self.img = new_img


        elif self.directore == 'right':
            if not self.rect.x > 1200:
                self.rect.x += self.speed

            new_img = pygame.transform.rotate(self.tank_image, 0)
            self.img = new_img


        if duration > 1:
            self.directore = random.choice(self.directories)
            self.start_time_botMove = time.time()



    def bot_move(self):
        if self.directore == "up":      self.rect.y -= self.speed
        elif self.directore == "down":  self.rect.y += self.speed
        elif self.directore == "left":  self.rect.x -= self.speed
        elif self.directore == "right": self.rect.x += self.speed




# ---------- Пулі ---------- #
class Bullet(Object):
    def __init__(self, x, y, width, height, direction, comand, damage, speed=8):
        super().__init__(x, y, width, height)
        self.direction = direction
        self.speed = speed
        self.comand = comand
        self.damage = damage
        self.img = pygame.image.load("Bullet.png")

        if self.direction == "up":      self.img = pygame.transform.rotate(self.img, 90)
        elif self.direction == "down":  self.img = pygame.transform.rotate(self.img, 270)
        elif self.direction == "left":  self.img = pygame.transform.rotate(self.img, 180)
        elif self.direction == "right": self.img = pygame.transform.rotate(self.img, 0)



    def update(self):
        if self.direction == "up":      self.rect.y -= self.speed
        elif self.direction == "down":  self.rect.y += self.speed
        elif self.direction == "left":  self.rect.x -= self.speed
        elif self.direction == "right": self.rect.x += self.speed



    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))




# ---------- Раунди ---------- #
class Round:
    def __init__(self, tanks, coords_walls, player, fon, wall_image, player_image):
        self.player = player
        self.player.hp_max = self.player.hp
        self.player_hp = Label(0, 600, 60, str(self.player.hp), "#ff4d4d")
        self.player_image = player_image
        self.fon = fon
        self.font = Label(550, 300, 80, "Pause")
        self.tanks = []
        self.walls = []
        self.bullets = []


        for x, y, width, height, image, hp, speed, damage, comand, defoult_directore in tanks:
            self.tanks.append(Bot(x, y, width, height, image, hp, speed, damage, comand, defoult_directore))


        for x, y in coords_walls:
            self.walls.append(Object(x, y, 30, 30, wall_image))



    def pause(self):
        while True:
            # обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        return


            self.fon.draw(screen)
            self.player.draw(screen)


            for tank in self.tanks:
                if not tank.hp <= 0:
                    tank.draw(screen)


            for bullet in self.bullets:
                bullet.draw(screen)


            for wall in self.walls:
                wall.draw(screen)


            pygame.display.flip()
            clock.tick(50)



    def game(self):
        self.player.rect.x = self.player.x
        self.player.rect.y = self.player.y


        while True:
            # обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.shot(self.player.directore, self.bullets)


            # відображення
            if len(self.tanks) == 0:
                self.player.hp = self.player.hp_max
                return True

            if self.player.hp <= 0:
                return False


            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                new_img = pygame.transform.rotate(self.player_image, 180)
                self.player.img = new_img
                self.player.rect.x -= self.player.speed
                self.player.directore = "left"

            elif keys[pygame.K_d]:
                new_img = pygame.transform.rotate(self.player_image, 0)
                self.player.img = new_img
                self.player.rect.x += self.player.speed
                self.player.directore = "right"

            elif keys[pygame.K_w]:
                new_img = pygame.transform.rotate(self.player_image, 90)
                self.player.img = new_img
                self.player.rect.y -= self.player.speed
                self.player.directore = "up"

            elif keys[pygame.K_s]:
                new_img = pygame.transform.rotate(self.player_image, 270)
                self.player.img = new_img
                self.player.rect.y += self.player.speed
                self.player.directore = "down"


            self.fon.draw(screen)
            self.player.collide_bullets(self.bullets, self.bullets)
            self.player.collide_walls(self.walls)
            self.player.draw(screen)


            for tank in self.tanks:
                if tank.hp <= 0:
                    self.tanks.remove(tank)
                tank.bot_random_rotate()
                tank.collide_bullets(self.bullets, self.bullets)
                tank.shot(tank.directore, self.bullets)
                tank.collide_walls(self.walls)
                tank.draw(screen)


            for bullet in self.bullets:
                for wall in self.walls:
                    if wall.rect.colliderect(bullet.rect):
                        self.bullets.remove(bullet)

                if len(self.bullets) > 99:
                    del self.bullets[0]

                bullet.update()
                bullet.draw(screen)


            for wall in self.walls:
                wall.draw(screen)


            self.player_hp.set_text(str(self.player.hp))
            self.player_hp.draw(screen)


            # оновлення дисплея
            pygame.display.flip()
            clock.tick(50)




# ---------- Гра ---------- #
class Game:
    def __init__(self, rounds, bufs, fon, player):
        self.rounds = rounds
        self.bufs = bufs
        self.fon = fon
        self.def_player = player
        self.player = player


        self.button1 = Button(320, 300, "", 200)
        self.button2 = Button(550, 300, "", 200)
        self.button3 = Button(780, 300, "", 200)



    def random_buf(self):
        key = random.choice(list(self.bufs.keys()))
        value = random.choice(self.bufs[key])
        return key, value



    def new_bufs(self, buf1, buf2, buf3):
        def button_return(buf):
            if buf[0] == "hp":     self.player.hp += buf[1]
            if buf[0] == "speed":  self.player.speed += buf[1]
            if buf[0] == "damage": self.player.damage += buf[1]
            nonlocal running
            running = False


        self.button1.onclick(lambda: button_return(buf1))
        self.button2.onclick(lambda: button_return(buf2))
        self.button3.onclick(lambda: button_return(buf3))

        self.button1.set_text(f"{buf1[0]} + {buf1[1]}")
        self.button2.set_text(f"{buf2[0]} + {buf2[1]}")
        self.button3.set_text(f"{buf3[0]} + {buf3[1]}")


        running = True
        while running:
            # обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


                self.button1.update(event)
                self.button2.update(event)
                self.button3.update(event)


            self.fon.draw(screen)
            self.button1.draw(screen)
            self.button2.draw(screen)
            self.button3.draw(screen)


            # оновлення дисплея та обмеження частоти
            pygame.display.flip()
            clock.tick(50)



    def cycle(self):
        running = True
        while running:
            # обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            self.fon.draw(screen)
            self.player = self.def_player
            win1, win2, win3, win4, win5, win6, win7, win8, win9, win10 = False, False, False, False, False, False, False, False, False, False
            win1 = self.rounds[0].game()


            # Перший раунд 🧨
            if win1:
                self.new_bufs(
                    self.random_buf(),
                    self.random_buf(),
                    self.random_buf()
                )

                win2 = self.rounds[1].game()


                # Другий раунд 🎃
                if win2 and len(self.rounds) == 2:
                    self.new_bufs(
                        self.random_buf(),
                        self.random_buf(),
                        self.random_buf()
                    )

                    win3 = self.rounds[2].game()


                    # Третій раунд 🎇
                    if win3 and len(self.rounds) == 3:
                        self.new_bufs(
                            self.random_buf(),
                            self.random_buf(),
                            self.random_buf()
                        )

                        win4 = self.rounds[3].game()


                        # Четвертий раунд 🎄
                        if win4 and len(self.rounds) == 4:
                            self.new_bufs(
                                self.random_buf(),
                                self.random_buf(),
                                self.random_buf()
                            )

                            win5 = self.rounds[4].game()


                            # Пятий раунд 🎫
                            if win5 and len(self.rounds) == 5:
                                self.new_bufs(
                                    self.random_buf(),
                                    self.random_buf(),
                                    self.random_buf()
                                )

                                win6 = self.rounds[5].game()


                                # Шостий раунд 🧢
                                if win6 and len(self.rounds) == 6:
                                    self.new_bufs(
                                        self.random_buf(),
                                        self.random_buf(),
                                        self.random_buf()
                                    )

                                    win7 = self.rounds[6].game()


                                    # Сьомий раунд 🔮
                                    if win7 and len(self.rounds) == 7:
                                        self.new_bufs(
                                            self.random_buf(),
                                            self.random_buf(),
                                            self.random_buf()
                                        )

                                        win8 = self.rounds[7].game()


                                        # Восьмий раунд 🪀
                                        if win8 and len(self.rounds) == 8:
                                            self.new_bufs(
                                                self.random_buf(),
                                                self.random_buf(),
                                                self.random_buf()
                                            )

                                            win9 = self.rounds[8].game()


                                            # Девятий раунд 🥼
                                            if win9 and len(self.rounds) == 9:
                                                self.new_bufs(
                                                    self.random_buf(),
                                                    self.random_buf(),
                                                    self.random_buf()
                                                )

                                                win10 = self.rounds[9].game()


                                                # Десятий раунд 🎩
                                                if win10 and len(self.rounds) == 10:
                                                    self.new_bufs(
                                                        self.random_buf(),
                                                        self.random_buf(),
                                                        self.random_buf()
                                                    )

                                                    self.rounds[10].game()


            # оновлення дисплея та обмеження частоти
            pygame.display.flip()
            clock.tick(50)
