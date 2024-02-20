import random
import unittest

from classes.Maze import Maze


class Tests(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.m1 = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)

    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.m1._cells), self.num_cols
        )
        self.assertEqual(len(self.m1._cells[0]), self.num_rows)

    def test_maze_unvisit_cells(self):
        self.assertEqual(
            self.m1._cells[random.randint(0, self.num_cols)][random.randint(0, self.num_rows)].visited,
            False
        )

    def test_maze_solve_1x1(self):
        m1x1 = Maze(0, 0, 1, 1, 1, 1)
        self.assertEqual(
            m1x1.solve(), True
        )


if __name__ == "__main__":
    unittest.main()
