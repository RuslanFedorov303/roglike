import pygame
import random
import  time
pygame.init()


bullets = []
screen = pygame.display.set_mode((1300, 700))
clock = pygame.time.Clock()



# ---------- Базовий клас ---------- #
class Object:
    def __init__(self, x, y, width, height, img=""):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.img = img
        self.rect = pygame.Rect(x, y, width, height)


    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))



# ---------- Ентіті ---------- #
class Entiti(Object):
    def __init__(self, x, y, width, height, img, hp, damage, comand, defoult_directore="left"):
        super().__init__(x, y, width, height, img)
        self.hp = hp
        self.damage = damage
        self.directore = defoult_directore
        self.comand = comand
        self.start_time = time.time()
        self.end_time = 0


    def shot(self, directore):
        self.end_time = time.time()
        duration = self.end_time - self.start_time

        if duration >= 0.7:
            if directore == 'up':      bullets.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "up", self.comand, self.damage))
            elif directore == 'down':  bullets.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "down", self.comand, self.damage))
            elif directore == 'left':  bullets.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "left", self.comand, self.damage))
            elif directore == 'right': bullets.append(Bullet(self.rect.centerx, self.rect.centery, 10, 10, "right", self.comand, self.damage))
            self.start_time = time.time()


    def collide_bullets(self, bullets_c, tanks):
        global bullets
        for bullet in bullets_c:
            for tank in tanks:
                if bullet.rect.colliderect(tank.rect) and bullet.comand != tank.comand:
                    tank.hp -= bullet.damage
                    bullets.remove(bullet)


    def colide_walls(self, walls, tanks):
        for wall in walls:
            for tank in tanks:
                if tank.rect.colliderect(wall.rect):
                    if tank.directore == 'up':      tank.rect.y += 3
                    elif tank.directore == 'down':  tank.rect.y -= 3
                    elif tank.directore == 'left':  tank.rect.x += 3
                    elif tank.directore == 'right': tank.rect.x -= 3



# ---------- Вороги ---------- #
class Bot(Entiti):
    def __init__(self, x, y, width, height, img, hp, damage, comand, defoult_directore="left"):
        super().__init__(x, y, width, height, img, hp, damage, comand, defoult_directore="left")
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
                self.rect.y -= 3

            new_img = pygame.transform.rotate(self.tank_image, 90)
            self.img = new_img

        elif self.directore == 'down':
            if not self.rect.y > 600:
                self.rect.y += 3

            new_img = pygame.transform.rotate(self.tank_image, 270)
            self.img = new_img

        elif self.directore == 'left':
            if not self.rect.x < 0:
                self.rect.x -= 3

            new_img = pygame.transform.rotate(self.tank_image, 180)
            self.img = new_img

        elif self.directore == 'right':
            if not self.rect.x > 1200:
                self.rect.x += 3

            new_img = pygame.transform.rotate(self.tank_image, 0)
            self.img = new_img


        if duration > 1:
            self.directore = random.choice(self.directories)
            self.start_time_botMove = time.time()


    def bot_move(self):
        if self.directore == "up":      self.rect.y -= 3
        elif self.directore == "down":  self.rect.y += 3
        elif self.directore == "left":  self.rect.x -= 3
        elif self.directore == "right": self.rect.x += 3



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
    def __init__(self, tanks, player, fon, coords_walls, wall_image, player_image):
        self.player = player
        self.player_image = player_image
        self.fon = fon
        self.tanks = []
        self.all_tanks = [self.player]
        self.walls = []


        for x, y, width, height, image, hp, damage, comand in tanks:
            self.tanks.append(Bot(x, y, width, height, image, hp, damage, comand))
            self.all_tanks.append(Bot(x, y, width, height, image, hp, damage, comand))


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
            pygame.display.flip()
            clock.tick(50)


    def game(self):
        while True:
            # обробка подій
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        self.pause()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.player.shot(self.player.directore)


            # відображення
            if self.player.hp <= 0:
                return


            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                new_img = pygame.transform.rotate(self.player_image, 180)
                self.player.img = new_img
                self.player.rect.x -= 3
                self.player.directore = "left"

            if keys[pygame.K_d]:
                new_img = pygame.transform.rotate(self.player_image, 0)
                self.player.img = new_img
                self.player.rect.x += 3
                self.player.directore = "right"

            if keys[pygame.K_w]:
                new_img = pygame.transform.rotate(self.player_image, 90)
                self.player.img = new_img
                self.player.rect.y -= 3
                self.player.directore = "up"

            if keys[pygame.K_s]:
                new_img = pygame.transform.rotate(self.player_image, 270)
                self.player.img = new_img
                self.player.rect.y += 3
                self.player.directore = "down"


            self.fon.draw(screen)
            self.player.colide_walls(self.walls, self.all_tanks)
            self.player.draw(screen)


            for tank in self.tanks:
                if not tank.hp <= 0:
                    tank.bot_random_rotate()
                    tank.collide_bullets(bullets, self.all_tanks)
                    tank.shot(tank.directore)
                    tank.colide_walls(self.walls, self.all_tanks)
                    tank.draw(screen)


            for bullet in bullets:
                if len(bullets) > 99:
                    del bullets[0]
                bullet.update()
                bullet.draw(screen)


            for wall in self.walls:
                wall.draw(screen)


            # оновлення дисплея
            pygame.display.flip()
            clock.tick(50)



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
    def __init__(self, x, y, text, w):
        self.rect = pygame.Rect(x, y, w, 50)
        self.rect_image = pygame.Surface((w, 50))

        self.rect_image.fill((0, 0, 0))
        self.rect_image_active = pygame.Surface((w, 50))
        self.rect_image_active.fill((0, 0, 0))

        self.font = pygame.font.Font(None, 32)
        self.text_image = self.font.render(text, True, (100, 0, 0))
        self.text_rect = self.text_image.get_rect()

        self.text_rect.x = self.rect.x + 20
        self.text_rect.y = y+5
        self.active = False
        self.fn = None


    def update(self):
        x, y = pygame.mouse.get_pos()
        collision = self.rect.collidepoint(x, y)
        if collision:
            self.active = True
            click = pygame.mouse.get_pressed()[0]

            if click and self.fn:
                self.fn()

        else:
            self.active = False


    def draw(self, surface):
        if self.active:
            surface.blit(self.rect_image, (self.rect.x, self.rect.y))

        else:
            surface.blit(self.rect_image_active, (self.rect.x, self.rect.y))
        surface.blit(self.text_image, (self.text_rect.x, self.text_rect.y))


    def onclick(self, fn):
        self.fn = fn
