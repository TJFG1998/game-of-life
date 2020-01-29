import pygame
import numpy


SIZE = 10  # Heigth and width of the game GAME_BOARD
GAME_BOARD = [
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WIDTH = 20
HEIGHT = 20
MARGIN = 5
WINDOW_SIZE = [255, 255]
SCREEN = pygame.display.set_mode(WINDOW_SIZE)

pygame.init()
pygame.display.set_caption("GAME OF LIFE")
clock = pygame.time.Clock()
SCREEN.fill(BLACK)


def draw(board):
    for row in range(10):
        for column in range(10):
            color = WHITE
            if board[row][column] == 1:
                color = GREEN
            if board[row][column] == 0:
                color = RED
            pygame.draw.rect(SCREEN, color, [
                (MARGIN + WIDTH) * column + MARGIN,
                (MARGIN + HEIGHT) * row + MARGIN,
                WIDTH,
                HEIGHT
                ]
            )
    clock.tick(600)
    pygame.display.flip()


def is_alive(GAME_BOARD, pos_x, pos_y) -> int:
    alive = 0
    for x in range(pos_x-1, pos_y+2):
        for y in range(pos_y-1, pos_y+2):
            if 0 <= x < SIZE and 0 <= y < SIZE:
                if GAME_BOARD[x][y] == 1:
                    alive += 1
    if GAME_BOARD[pos_x][pos_y] == 1:
        return alive - 1
    return alive


def check_cells():
    try:
        for x in range(0, 10):
            for y in range(0, 10):
                cell = is_alive(GAME_BOARD, x, y)
                print("Position (" + str(x) + "," + str(y) + ")")
                print("Value: " + str(cell))
                if GAME_BOARD[x][y] == 1:
                    if cell <= 1:
                        GAME_BOARD[x][y] = 0
                        print("CELL died by under population.")
                    if cell == 2 or cell == 3:
                        GAME_BOARD[x][y] = 1
                        print("CELL lives.")
                    else:
                        GAME_BOARD[x][y] = 0
                        print("CELL died by over population.")
                else:
                    if cell < 3:
                        GAME_BOARD[x][y] = 0
                        print("CELL stays death for under population.")
                    if cell == 3:
                        GAME_BOARD[x][y] = 1
                        print("CELL born.")
                    elif cell > 3:
                        GAME_BOARD[x][y] = 0
                        print("CELL stays dead for over population.")
                draw(GAME_BOARD)
    except Exception as e:
        raise e


def increase_matrix():
    new = []
    for i in range(0, SIZE):
        new.append(0)

    for row in GAME_BOARD:
        row.insert(0, 0)
        row.append(0)

    GAME_BOARD.insert(0, new)
    GAME_BOARD.append(new)


# for i in range(20):
#     check_cells()

pygame.quit()
