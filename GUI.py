import pygame
import sys

BOX_LENGTH = 70
LINE_THIN = 5
LINE_THICK = 8
WINDOW_WIDTH = BOX_LENGTH * 9 + 100
WINDOW_HEIGHT = WINDOW_WIDTH + 140
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoko Game")

    # Create canvas
    bg = pygame.Surface(screen.get_size()).convert()
    bg.fill(WHITE)

    # # Draw Boundary
    # pygame.draw.line(bg, BLACK, (0, 70), (WINDOW_WIDTH, 70), LINE_THICK)
    # pygame.draw.line(bg, BLACK, (0, WINDOW_HEIGHT - 70), (WINDOW_WIDTH, WINDOW_HEIGHT - 70), LINE_THICK)

    # Draw Grid
    w = 0
    while w < 10:
        if w % 3 == 0:
            pygame.draw.line(bg, BLACK, (w * BOX_LENGTH + 50, 70), (w * BOX_LENGTH + 50, WINDOW_HEIGHT - 170), LINE_THICK)
        else:
            pygame.draw.line(bg, BLACK, (w * BOX_LENGTH + 50, 70), (w * BOX_LENGTH + 50, WINDOW_HEIGHT - 170), LINE_THIN)
        w += 1

    h = 0
    while h < 10:
        if h % 3 == 0:
            pygame.draw.line(bg, BLACK, (47.5, h * BOX_LENGTH + 70), (WINDOW_WIDTH - 46, h * BOX_LENGTH + 70), LINE_THICK)
        else:
            pygame.draw.line(bg, BLACK, (47.5, h * BOX_LENGTH + 70), (WINDOW_WIDTH - 46, h * BOX_LENGTH + 70), LINE_THIN)
        h += 1


    screen.blit(bg, (0, 0))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == "__main__":
    main()
