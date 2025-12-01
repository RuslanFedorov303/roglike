import pygame
import random
import  time


bullets = []



# ---------- Пулі ---------- #
class Bullet:
    def __init__(self, x, y, direction, comand, damage, speed=8):
        self.rect = pygame.Rect(x, y, 10, 10)
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



# ---------- Базовий клас ---------- #
class Object:
    def __init__(self, x, y, width, height, img=""):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.img = img
        self.rect = pygame.Rect(x, y, width, height)


    def draw(self, screen):
        screen.blit(self.img, (self.rect.left, self.rect.top))



# ---------- Опоненти та игрок ---------- #
class Entiti(Object):
    def __init__(self, x, y, width, height, img, hp, damage, comand, defoult_directore="left"):
        super().__init__(x, y, width, height, img)
        self.hp = hp
        self.damage = damage
        self.directore = defoult_directore
        self.comand = comand
        self.start_time = time.time()
        self.end_time = 0


    def shot(self, direction):
        global bulletsdd

        self.end_time = time.time()
        duration = self.end_time - self.start_time

        if duration >= 0.7:
            if direction == 'up':      bullets.append(Bullet(self.rect.centerx, self.rect.centery, "up", self.comand, 30))
            elif direction == 'down':  bullets.append(Bullet(self.rect.centerx, self.rect.centery, "down", self.comand, 30))
            elif direction == 'left':  bullets.append(Bullet(self.rect.centerx, self.rect.centery, "left", self.comand, 30))
            elif direction == 'right': bullets.append(Bullet(self.rect.centerx, self.rect.centery, "right", self.comand, 30))
            self.start_time = time.time()


    def collide_bullets(self, bullets_c, tanks):
        global bullets
        for bullet in bullets_c:
            for tank in tanks:
                if bullet.rect.colliderect(tank.rect) and bullet.comand != tank.comand:
                    tank.hp -= bullet.damage
                    bullets.remove(bullet)



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
    #    def colide_wall():
        if self.directore == "up":      self.rect.y -= 3
        elif self.directore == "down":  self.rect.y += 3
        elif self.directore == "left":  self.rect.x -= 3
        elif self.directore == "right": self.rect.x += 3















# ---------- Текст для гри ---------- #
class Label:
    def __init__(self, x, y, size, color="black", default_text="text"):
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

        self.rect_image.fill(BLUE)
        self.rect_image_active = pygame.Surface((w, 50))
        self.rect_image_active.fill(GREEN)

        self.font = pygame.font.Font(None, 32)
        self.text_image = self.font.render(text, True, RED)
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