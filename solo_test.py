import pygame
import random
pygame.init()

LIFE = 3
CAT_DEST_X = random.randint(50, 650)
CAT_DEST_Y = random.randint(50, 650)

BLACK = (0,0,0)
PURPLE = (130, 25, 50)
PURPLE_DARK = (55,10,20)
WHITE = (220, 210, 210)

WIDTH, HEIGHT = 900, 700
FPS = 60
K = 0.05
PIECE_WIDTH, PIECE_HEIGHT = 30, 20
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 20, 90

mouse_img = pygame.image.load("mouse.png")
mouse_img = pygame.transform.scale(mouse_img, (90,90))
cat_img = pygame.image.load("cat.png")
cat_img = pygame.transform.scale(cat_img, (190,190))
bg_img = pygame.image.load("bg.png")
heart_img = pygame.image.load("heart.png")
heart_dead_img = pygame.image.load(heart_dead.png)
# bg_img = pygame.transform.scale(bg_img, (900,700))

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solo test")

class Obstacle:
    COLOR = WHITE
    VEL = 4
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

class Piece:
    COLOR = PURPLE_DARK
    VEL = 8
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.Surface.blit(win, mouse_img, (self.x-30, self.y-28, self.width, self.height))
        #pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True, left=True):
        if up == True:
            self.y -= self.VEL
        if up == False:
            self.y += self.VEL
        if left == True:
            self.x -= self.VEL
        if left == False:
            self.x += self.VEL

class Cat:
    temp_x = CAT_DEST_X
    temp_y = CAT_DEST_Y
    COLOR = WHITE
    VEL = 4
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.Surface.blit(win, cat_img, (self.x-80, self.y-85, self.width, self.height))
        #pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self):

        if self.x < self.temp_x:
            self.x += 3
        if self.x > self.temp_x:
            self.x -= 3

        if self.y > self.temp_x:
            self.y -= 3
        if self.y < self.temp_y:
            self.y += 3

        # self.x = self.temp_x
        # self.y = self.temp_y

def draw(win, pieces, obstacles, cats, lives):
    win.blit(bg_img,(0,0))

    for piece in pieces:
        piece.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)

    for cat in cats:
        cat.draw(win)

    for live in lives:
        live.draw(win)

    pygame.display.update()

def handle_piece_movement(keys, first_piece):
    if keys[pygame.K_w]:
        first_piece.move(up=True, left=None)
    if keys[pygame.K_s]:
        first_piece.move(up=False, left=None)
    if keys[pygame.K_a]:
        first_piece.move(left=True, up=None)
    if keys[pygame.K_d]:
        first_piece.move(left=False, up=None)

def handle_cat_movement(first_cat):
    temp_x = CAT_DEST_X
    temp_y = CAT_DEST_Y
    first_cat.move()

def collision_check(body1=(), body2=()):
    pass

class Lives:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    if LIFE == 3:
        def draw(self, win):
            pygame.Surface.blit(win, heart_img, (self.x, self.y-330, self.width, self.height))
            pygame.Surface.blit(win, heart_img, (self.x+35, self.y - 330, self.width, self.height))
            pygame.Surface.blit(win, heart_img, (self.x+70, self.y - 330, self.width, self.height))
    if LIFE == 2:
        def draw(self, win):
            pygame.Surface.blit(win, heart_img, (self.x, self.y-330, self.width, self.height))
            pygame.Surface.blit(win, heart_img, (self.x+35, self.y - 330, self.width, self.height))
    if LIFE == 1:
        def draw(self, win):
            pygame.Surface.blit(win, heart_img, (self.x, self.y-330, self.width, self.height))


def main():
    clock = pygame.time.Clock()
    run = True

    first_piece = Piece(10, HEIGHT//2 - PIECE_HEIGHT//2, PIECE_WIDTH, PIECE_HEIGHT)
    #second_piece = Piece(WIDTH - 10 - PIECE_WIDTH, HEIGHT // 2 - PIECE_HEIGHT // 2, PIECE_WIDTH, PIECE_HEIGHT)
    first_cat = Cat(WIDTH - 10 - PIECE_WIDTH, HEIGHT // 2 - PIECE_HEIGHT // 2, PIECE_WIDTH, PIECE_HEIGHT)
    lives1 = Lives(10, HEIGHT//2 - PIECE_HEIGHT//2, PIECE_WIDTH, PIECE_HEIGHT)

    first_obstacle = Obstacle(500, HEIGHT//2 - OBSTACLE_HEIGHT//2, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN, [first_piece], [first_obstacle], [first_cat], [lives1])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()

        handle_piece_movement(keys, first_piece)
        handle_cat_movement(first_cat)

    pygame.quit()

if __name__ == "__main__":
    main()