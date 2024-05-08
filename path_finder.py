import curses
import curses as cs
from curses import wrapper as wr
import queue as qq
# import time as t

my_maze = [
    ['#', '#', '#', '#', '#', '#', '#', 'O', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', 'X', '#', '#']
]


def print_maze(maze, std_scr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) in path:
                std_scr.addstr(i, j * 2, "+", RED)
            else:
                std_scr.addstr(i, j * 2, col, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == start:
                return i, j
    return None


def find_path(maze, std_scr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    queue = qq.Queue()
    queue.put(
        (start_pos, [start_pos])
    )

    visited = set()
    while not queue.empty():
        pos, path = queue.get()
        row, col = pos

        std_scr.clear()
        print_maze(maze, std_scr, path)
        # t.sleep(0.2) # Take a look, how it works
        std_scr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            queue.put((neighbor, new_path))

            visited.add(neighbor)


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:
        # Up
        neighbors.append((row - 1, col))
    elif row + 1 < len(maze):
        # Down
        neighbors.append((row + 1, col))
    elif col > 0:
        # Left
        neighbors.append((row, col - 1))
    elif col + 1 < len(maze[0]):
        # Right
        neighbors.append((row, col + 1))

    return neighbors


def main(std_scr):
    cs.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    cs.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(my_maze, std_scr)
    std_scr.getch()


wr(main)
