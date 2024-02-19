from classes.Maze import Maze
from classes.Window import Window

if __name__ == '__main__':
    win = Window(820, 700)
    # Create a few instances of the Cell class
    # cell1 = Cell(50, 100, 50, 100, "win1", True, False, True, False)
    # cell2 = Cell(100, 150, 100, 150, "win2", False, True, False, True)
    # cell3 = Cell(150, 200, 150, 200, "win3", True, True, False, False)
    #
    # win.draw_cell(cell1, 'black')
    # win.draw_cell(cell2, 'red')
    # win.draw_cell(cell3, 'green')
    #
    # win.draw_move(cell1, cell2)

    Maze(10, 10, 15, 15, 40, 40, win)

    win.wait_for_close()
