import pygame
pygame.init()

BLACK = (0,0,0)
WIDTH, HEIGHT = 700, 500
FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solo test")

def draw(win):
    win.fill(BLACK)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

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