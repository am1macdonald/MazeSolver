from tkinter import Canvas

from classes.Line import Line
from classes.Point import Point
from classes.Window import Window


class Cell:
    def __init__(self,
                 _x1=None,
                 _y1=None,
                 _x2=None,
                 _y2=None,
                 _win: Window = None,
                 has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self._y2 = _y2
        self._y1 = _y1
        self._x2 = _x2
        self._x1 = _x1
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._win = _win
        self.visited = False

    def draw(self, ):
        if not self._win:
            return
        points = [Point(self._x1, self._y1), Point(self._x2, self._y1), Point(self._x2, self._y2),
                  Point(self._x1, self._y2)]

        if self.has_top_wall:
            Line(points[0], points[1]).draw(self._win.canvas, 'black')
        else:
            Line(points[0], points[1]).draw(self._win.canvas, '#d9d9d9')
        if self.has_right_wall:
            Line(points[1], points[2]).draw(self._win.canvas, 'black')
        else:
            Line(points[1], points[2]).draw(self._win.canvas, '#d9d9d9')
        if self.has_bottom_wall:
            Line(points[2], points[3]).draw(self._win.canvas, 'black')
        else:
            Line(points[2], points[3]).draw(self._win.canvas, '#d9d9d9')
        if self.has_left_wall:
            Line(points[0], points[3]).draw(self._win.canvas, 'black')
        else:
            Line(points[0], points[3]).draw(self._win.canvas, '#d9d9d9')

    def get_center(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

    def draw_move(self, to_cell, undo=False):
        if not self._win:
            return
        if undo:
            colour = 'red'
        else:
            colour = 'gray'
        Line(self.get_center(), to_cell.get_center()).draw(self._win.canvas, colour)
