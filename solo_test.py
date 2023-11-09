import pygame
pygame.init()

BLACK = (0,0,0)
PURPLE = (130, 25, 50)
PURPLE_DARK = (55,10,20)

WIDTH, HEIGHT = 700, 500
FPS = 60
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solo test")

class piece:
    COLOR = PURPLE_DARK
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(win):
    win.fill(PURPLE)

    piece.draw(win)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    first_piece = piece(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    while run:
        clock.tick(FPS)
        draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

if __name__ == "__main__":
    main()