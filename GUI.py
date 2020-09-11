import pygame
from Sudoku_GUI import SudokuGUI
import sys

BOX_LENGTH = 70
LINE_THIN = 5
LINE_THICK = 8
WINDOW_WIDTH = BOX_LENGTH * 9 + 100
WINDOW_HEIGHT = WINDOW_WIDTH + 140
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw_sudoku(sc, sudo: SudokuGUI):
    font = pygame.font.Font(None, 60)
    for r in range(9):
        for c in range(9):
            if sudo.origin[r][c] == 0:
                continue
            num = font.render(str(sudo.origin[r][c]), True, BLACK)
            num_rect = num.get_rect()
            num_rect.center = (50 + BOX_LENGTH * (c + 0.5), BOX_LENGTH * (r + 0.5) + 70)
            sc.blit(num, num_rect)

def main(board):
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Sudoko Game")

    # Create canvas
    bg = pygame.Surface(screen.get_size()).convert()
    bg.fill(WHITE)

    # Draw Grid
    w = 0
    while w < 10:
        if w % 3 == 0:
            pygame.draw.line(bg, BLACK, (w * BOX_LENGTH + 50, 70), (w * BOX_LENGTH + 50, WINDOW_HEIGHT - 170),
                             LINE_THICK)
        else:
            pygame.draw.line(bg, BLACK, (w * BOX_LENGTH + 50, 70), (w * BOX_LENGTH + 50, WINDOW_HEIGHT - 170),
                             LINE_THIN)
        w += 1

    h = 0
    while h < 10:
        if h % 3 == 0:
            pygame.draw.line(bg, BLACK, (47.5, h * BOX_LENGTH + 70), (WINDOW_WIDTH - 46, h * BOX_LENGTH + 70),
                             LINE_THICK)
        else:
            pygame.draw.line(bg, BLACK, (47.5, h * BOX_LENGTH + 70), (WINDOW_WIDTH - 46, h * BOX_LENGTH + 70),
                             LINE_THIN)
        h += 1
    screen.blit(bg, (0, 0))

    sudoku = SudokuGUI(board)

    draw_sudoku(screen, sudoku)



    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == "__main__":
    b = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    main(b)
