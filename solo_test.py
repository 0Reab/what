import pygame
pygame.init()

BLACK = (0,0,0)
PURPLE = (130, 25, 50)
PURPLE_DARK = (55,10,20)
WHITE = (220, 210, 210)

WIDTH, HEIGHT = 700, 500
FPS = 60
K = 0.05
PIECE_WIDTH, PIECE_HEIGHT = 40, 40
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 20, 90

mouse_img = pygame.image.load("mouse.png")

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
        pygame.Surface.blit(win, mouse_img, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True, left=True):
        if up == True:
            self.y -= self.VEL
        if up == False:
            self.y += self.VEL
        if left == True:
            self.x -= self.VEL
        if left == False:
            self.x += self.VEL


def draw(win, pieces, obstacles):
    win.fill(PURPLE)

    for piece in pieces:
        piece.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.display.update()

def handle_piece_movement(keys, first_piece, second_piece):
    if keys[pygame.K_w]:
        first_piece.move(up=True, left=None)
    if keys[pygame.K_s]:
        first_piece.move(up=False, left=None)
    if keys[pygame.K_a]:
        first_piece.move(left=True, up=None)
    if keys[pygame.K_d]:
        first_piece.move(left=False, up=None)


def main():
    clock = pygame.time.Clock()
    run = True

    first_piece = Piece(10, HEIGHT//2 - PIECE_HEIGHT//2, PIECE_WIDTH, PIECE_HEIGHT)
    second_piece = Piece(WIDTH - 10 - PIECE_WIDTH, HEIGHT // 2 - PIECE_HEIGHT // 2, PIECE_WIDTH, PIECE_HEIGHT)

    first_obstacle = Obstacle(500, HEIGHT//2 - OBSTACLE_HEIGHT//2, OBSTACLE_WIDTH, OBSTACLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN, [first_piece, second_piece], [first_obstacle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        handle_piece_movement(keys, first_piece, second_piece)

    pygame.quit()

if __name__ == "__main__":
    main()