import pygame
pygame.init()

BLACK = (0,0,0)
WIDTH, HEIGHT = 500,600
FPS = 60
win = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("Solo test")

def draw(win):
    win.fill(BLACK)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event == pygame.QUIT:
                run = False
                break
    pygame.quit()

if __name__ == "__main__":
    main()