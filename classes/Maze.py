import time
from tkinter import Canvas

from classes.Cell import Cell
from classes.Window import Window


class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win: Window = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for col in range(0, self.num_cols):
            column = []
            for row in range(0, self.num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        offset_x = i * self.cell_size_x + self.x1
        offset_y = j * self.cell_size_y + self.y1
        self._cells[i][j].draw(offset_x, offset_y, offset_x + self.cell_size_x, offset_y + self.cell_size_y)
        self._animate()

    def _break_entrance_and_exit(self):
        tl = (self._cells[0][0])
        br = self._cells[self.num_cols - 1][self.num_rows - 1]
        tl.has_top_wall = False
        tl.has_bottom_wall = False
        tl.has_left_wall = False
        tl.has_right_wall = False
        self._draw_cell(0, 0)

        br.has_top_wall = False
        br.has_bottom_wall = False
        br.has_left_wall = False
        br.has_right_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)


    def _animate(self):
        if self._win:
            time.sleep(0.01)
            self._win.redraw()
