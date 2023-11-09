import pygame
pygame.init()

BLACK = (0,0,0)
PURPLE = (130, 25, 50)
PURPLE_DARK = (55,10,20)

WIDTH, HEIGHT = 700, 500
FPS = 60
PIECE_WIDTH, PIECE_HEIGHT = 20, 20
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solo test")

class Piece:
    COLOR = PURPLE_DARK
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(win, pieces):
    win.fill(PURPLE)

    for piece in pieces:
        piece.draw(win)

    pygame.display.update()


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

    pygame.quit()

if __name__ == "__main__":
    main()