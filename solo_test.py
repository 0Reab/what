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
        pygame.draw.rect(win, self.COLOR)

class Piece:
    COLOR = PURPLE_DARK
    VEL = 8
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


def draw(win, pieces):
    win.fill(PURPLE)

    for piece in pieces:
        piece.draw(win)

    pygame.display.update()

def handle_piece_movement(keys, first_piece, second_piece):
    if keys[pygame.K_w]:
        first_piece.move(up=True)
    if keys[pygame.K_s]:
        first_piece.move(up=False)


def main():
    clock = pygame.time.Clock()
    run = True

    first_piece = Piece(10, HEIGHT//2 - PIECE_HEIGHT//2, PIECE_WIDTH, PIECE_HEIGHT)
    second_piece = Piece(WIDTH - 10 - PIECE_WIDTH, HEIGHT // 2 - PIECE_HEIGHT // 2, PIECE_WIDTH, PIECE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN, [first_piece, second_piece])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        handle_piece_movement(keys, first_piece, second_piece)

    pygame.quit()

if __name__ == "__main__":
    main()