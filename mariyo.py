import pygame
import sys

pygame.init()

win = 1200
win_height = 600

fps = 20

Black = (0, 0, 0)
green = (0, 255, 0)

Add_new_Rate = 25
cactus_img = pygame.image.load('images.png')
cactus_img_rect = cactus_img.get_rect()
cactus_img_rect.left = 0

fir_img = pygame.image.load('nl.jpeg')
fir_img_rect = fir_img.get_rect()
fir_img_rect.left = 0

CLOCK = pygame.time.Clock()
font = pygame.font.SysFont('forte', 20)

canvas = pygame.display.set_mode((win, win_height))
pygame.display.set_caption('Mario Game')


class Topscore:
    def __init__(self):
        self.high_score = 0

    def top_score(self, score):
        if score > self.high_score:
            self.high_score = score
        return self.high_score


topscore = Topscore()


class Dragon:
    dragon_velcity = 10

    def __init__(self):
        self.dragon_img = pygame.image.load('dra.jpeg')
        self.dragon_img.rect = self.dragon_img.get_rect()
        self.dragon_img.rect.width -= 10
        self.dragon_img.rect.height -= 10
        self.dragon_img_rect.top = win_height / 2
        self.dragon_img_rect.right = win
        self.up = True
        self.down = False

    def update(self):
        canvas.blit(self.dragon_img, self.dragon_img_rect)
        if self.dragon_img_rect.top <= cactus_img_rect.bottom:
            self.up = False
            self.down = True
        elif self.dragon_img_rect.bottom >= fir_img_rect.top:
            self.up = True
            self.down = False

        if self.up:
            self.dragon_img_rect.top -= self.dragon_velcity
        elif self.down:
            self.dragon_img_rect.top += self.dragon_velcity


class Flames:
    flames_velocity = 20

    def __init__(self):
        self.flames = pygame.image.load('fair.jpeg')
        self.flames_img = pygame.transform.scale(self.flames, (20, 20))
        self.flames_img_rect = self.flames_img.get_rect()
        self.flames_img_rect.right = dragon.dragon_img_rect.left
        self.flames_img_rect.top = dragon.dragon_img_rect.top + 30

    def update(self):
        canvas.blit(self.flames_img, self.flames_img_rect)

        if self.flames_img_rect.left > 0:
            self.flames_img_rect.left -= self.flames_velocity


class Mario:
    velocity = 10

    def __init__(self):
        self.mario_img = pygame.image.load('mario.jpeg')
        self.mario_img_rect = self.mario_img.get_rect()
        self.mario_img_rect.left = 20
        self.mario_img_rect.top = win_height / 2 - 100
        self.down = True
        self.up = False

    def update(self):
        canvas.blit(self.mario_img, self.mario_img_rect)

        if self.mario_img_rect.top <= cactus_img_rect.bottom:
            gameover()
            if SCORE > self.mario_score:
                self.mario_score = SCORE

        if self.mario_img_rect.bottom >= fir_img_rect.top:
            gameover()
            if SCORE > self.mario_score:
                self.mario_score = SCORE
        if self.up:
            self.mario_img_rect.top -= 10
        if self.down:
            self.mario_img_rect.bottom += 10


def gameover():
    pygame.mixer.music.stop()
    music = pygame.mixer.sound('laser.wav')
    music.play()
    topscore.top_score(SCORE)
    game_over_img = pygame.image.load('m2.png')
    game_over_img_rect = game_over_img.get_rect()
    game_over_img_rect.center = (win / 2, win_height / 2)
    canvas.blit(game_over_img, game_over_img_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

                music.stop()
                game_loop()

        pygame.display.update()


def start_game():
    BLACK = pygame.Color("#000000")
    canvas.fill(BLACK)
    start_img = pygame.image.load('m1.png')
    start_img_rect = start_img.get_rect()
    start_img_rect.center = (win / 2, win_height / 2)
    canvas.blit(start_img, start_img_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
                game_loop()
        pygame.display.update()


def Check_level(SCORE):
    global LEVEL
    if score in range(0, 10):
        cactus_img_rect.bottom = 50
        fir_img_rect.top = win_height - 50
        LEVEL = 1
    elif SORE in range(10, 20):
        cactus_img_rect.bottom = 100
        fir_img_rect.top = win_height - 100
        LEVEL = 2
    elif SCORE in range(20, 30):
        cactus_img_rect.bottom = 150
        fir_img_rect.top = win_height - 150
        LEVEL = 3
    elif SCORE > 30:
        cactus_img_rect.bottom = 200
        fir_img_rect.top = win_height - 200
        LEVEL = 4


def game_loop():
    while True:
        global dragon
        dragon = Dragon
        dragon = Dragon()
        flames = False()
        mario = Mario()
        add_new_flame_counter = 0
        SCORE = 0
        global HIGH_SCORE
        flames_list = []
        pygame.mixer.music.load('')
        pygame.mixer.music.play(-1, 0, 0)
        while True:
            canvas.fill(BLACK)
            check_level(SCORE)
            dragon.update()
            if add_new_flame_counter == ADD_NEW_FLAMS_RATE:
                add_new_flame_counter == 0
                new_flame = Flames()
                flames_list.append(new_flame)
            for f in flames_list:
                if f.flames_img_rect.left <= 0:
                    flames_list.remove(f)
                    SCORE += 1

                f.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        mario.up = True
                        mario.down = False
                    elif event.key == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        mario.up = False
                        mario.down = True
                    elif event.type == pygame.K_DOWN:
                        mario.down = True
                        mario.up = False

            score_font = font.render('Score:' + str(SCORE),True,GREEN)
            score_font_rect = score_font.get_rect()
            score_font_rect.center =(200,cactus_img_rect.bottom + score_font_rect.height/2)
            canvas.blit(score_font,score_font_rect)

            level_font = font.render('Level:' + str(LEVEL), True, GREEN)
            level_font_rect = level_font.get_rect()
            level_font_rect.center = (500, cactus_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(level_font, level_font_rect)

            top_score_font = font.render('Top Score:' + str(topscore.high_score), True, GREEN)
            top_score_font_rect = top_score_font.get_rect()
            top_score_font_rect.center = (800, cactus_img_rect.bottom + score_font_rect.height / 2)
            canvas.blit(top_score_font, top_score_font_rect)

            canvas.blit(cactus_img,cactus_img_rect)
            canvas.blit(fir_img,fir_img_rect)
            mario.update()

            for f in flames_list:
                if f.flames_img_rect.colliderect(mario.mario_img_rect):
                    gameover()
                    if SCORE > mario.mario_score:
                        mario.mario_score = SCORE

            pygame.display.update()
            CLOCK.tick(FPS)


start_game()
