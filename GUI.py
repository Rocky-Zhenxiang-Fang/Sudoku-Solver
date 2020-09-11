import pygame
from Sudoku_GUI import SudokuGUI
import sys

BOX_LENGTH: int = 70
LINE_THIN = 5
LINE_THICK = 8
WINDOW_WIDTH = BOX_LENGTH * 9 + 100
WINDOW_HEIGHT = WINDOW_WIDTH + 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)


def draw_sudoku(sc, sudo: SudokuGUI):
    font = pygame.font.Font(None, 60)
    # Draw numbers
    for r in range(9):
        for c in range(9):
            if sudo.boxes[r][c].val == 0 and sudo.boxes[r][c].temp == 0:
                continue
            elif sudo.boxes[r][c].temp == sudo.boxes[r][c].val:
                num = font.render(str(sudo.boxes[r][c].val), True, BLACK, WHITE)
                num_rect = num.get_rect()
                num_rect.center = (50 + BOX_LENGTH * (c + 0.5), BOX_LENGTH * (r + 0.5) + 70)
                sc.blit(num, num_rect)
            else:
                num = font.render(str(sudo.boxes[r][c].temp), True, GRAY, WHITE)
                num_rect = num.get_rect()
                num_rect.center = (50 + BOX_LENGTH * (c + 0.5), BOX_LENGTH * (r + 0.5) + 70)
                sc.blit(num, num_rect)


def draw_status(sc, sudo: SudokuGUI, c, r):
    font = pygame.font.Font(None, 40)
    unchecked = font.render("     Unchecked = " + str(sudo.boxes[r][c].unchecked) + "     ", False, BLUE, WHITE)
    un_rect = unchecked.get_rect()
    un_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 90)
    sc.blit(unchecked, un_rect)


def record_number(sc, sudoku, c, r, event):
    num = event.key - 256
    # font = pygame.font.Font(None, 60)
    # num = font.render(str(num), True, GRAY)
    # num_rect = num.get_rect()
    # num_rect.center = (50 + BOX_LENGTH * (c + 0.5), BOX_LENGTH * (r + 0.5) + 70)
    sudoku.boxes[r][c].temp = event.key - 256
    draw_sudoku(sc, sudoku)


def update_number(sc, sudo: SudokuGUI, c, r):
    box = sudo.boxes[r][c]
    if box.temp != 0:
        if box.temp in box.unchecked:
            box.unchecked.remove(box.temp)
            if box.temp == box.ans:
                box.val = box.temp
    draw_status(sc, sudo, c, r)
    draw_sudoku(sc, sudo)


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
            pygame.draw.line(bg, BLACK, (w * BOX_LENGTH + 50, 70), (w * BOX_LENGTH + 50, WINDOW_HEIGHT - 130),
                             LINE_THICK)
        else:
            pygame.draw.line(bg, BLACK, (w * BOX_LENGTH + 50, 70), (w * BOX_LENGTH + 50, WINDOW_HEIGHT - 130),
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
    r, c = None, None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if r is not None and c is not None:
                    pygame.draw.rect(bg, BLACK, (50 + c * BOX_LENGTH, 70 + r * BOX_LENGTH, BOX_LENGTH, BOX_LENGTH),
                                     LINE_THIN)
                pos = pygame.mouse.get_pos()
                if 0 <= (pos[0] - 50) // BOX_LENGTH <= 8 and 0 <= (pos[1] - 70) // BOX_LENGTH <= 8:
                    c = (pos[0] - 50) // BOX_LENGTH
                    r = (pos[1] - 70) // BOX_LENGTH
                    pygame.draw.rect(bg, GREEN, (50 + c * BOX_LENGTH, 70 + r * BOX_LENGTH, BOX_LENGTH, BOX_LENGTH),
                                     LINE_THIN)
                    screen.blit(bg, (0, 0))
                    draw_status(screen, sudoku, c, r)
                    draw_sudoku(screen, sudoku)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1 or \
                        event.key == pygame.K_2 or event.key == pygame.K_KP2 or \
                        event.key == pygame.K_3 or event.key == pygame.K_KP3 or \
                        event.key == pygame.K_4 or event.key == pygame.K_KP4 or \
                        event.key == pygame.K_5 or event.key == pygame.K_KP5 or \
                        event.key == pygame.K_6 or event.key == pygame.K_KP6 or \
                        event.key == pygame.K_7 or event.key == pygame.K_KP7 or \
                        event.key == pygame.K_8 or event.key == pygame.K_KP8 or \
                        event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    record_number(screen, sudoku, c, r, event)
                    pygame.display.update()
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    update_number(screen, sudoku, c, r)
                    pygame.display.update()

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
