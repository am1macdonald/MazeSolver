from classes.Line import Line
from classes.Point import Point
from classes.Window import Window


if __name__ == '__main__':
    win = Window(800, 600)
    win.draw_line(Line(Point(0, 0), Point(50, 50)), 'black')
    win.wait_for_close()

