from classes.Maze import Maze
from classes.Window import Window

if __name__ == '__main__':
    win = Window(1220, 820)
    maze = Maze(10, 10, 20, 30, 40, 40, win)
    maze.solve()

    win.wait_for_close()
