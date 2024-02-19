import random
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
            seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_walls_r(0, 0)

    def _create_cells(self):
        self._cells = []
        for col in range(0, self.num_cols):
            column = []
            for row in range(0, self.num_rows):
                offset_x = col * self.cell_size_x + self.x1
                offset_y = row * self.cell_size_y + self.y1
                cell = Cell(offset_x, offset_y, offset_x + self.cell_size_x, offset_y + self.cell_size_y, self._win)
                column.append(cell)
            self._cells.append(column)
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
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

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            to_visit = []
            neighbors: [(int, int)] = []
            if i < self.num_cols - 1:
                neighbors.append(
                    (i + 1, j),
                )
            if i - 1 > 0:
                neighbors.append(
                    (i - 1, j),
                )
            if j < self.num_rows - 1:
                neighbors.append(
                    (i, j + 1),
                )
            if j - 1 > 0:
                neighbors.append(
                    (i, j - 1),
                )
            for cell in neighbors:
                if not self._cells[cell[0]][cell[1]].visited:
                    to_visit.append(cell)

            if len(to_visit) == 0:
                current.draw()
                return
            choice_coords = random.choice(to_visit)
            choice = self._cells[choice_coords[0]][choice_coords[1]]
            if i > choice_coords[0]:
                current.has_left_wall = False
                choice.has_right_wall = False
            elif i < choice_coords[0]:
                choice.has_left_wall = False
                current.has_right_wall = False
            elif j > choice_coords[1]:
                choice.has_bottom_wall = False
                current.has_top_wall = False
            elif j < choice_coords[1]:
                current.has_bottom_wall = False
                choice.has_top_wall = False
            choice.draw()
            current.draw()
            self._animate()
            self._break_walls_r(choice_coords[0], choice_coords[1])

    def _animate(self):
        if self._win:
            time.sleep(0.005)
            self._win.redraw()
