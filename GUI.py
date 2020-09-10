import pygame
import sys

BOX_LENGTH = 70
LINE_THIN = 5
LINE_THICK = 10
WINDOW_WIDTH = BOX_LENGTH * 9 + LINE_THIN * 6 + LINE_THICK * 4
WINDOW_HEIGHT = WINDOW_WIDTH + 100

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoko Game")


    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()




if __name__ == "__main__":
    main()