from .game import Grid, Cell, Player


class DumbIA (Player):
    def play(self, grid: Grid) -> int:
        for line in range (grid.lines):
            for column in range (grid.columns):
                if grid.grid[line][column] == Cell.EMPTY:
                    return column








