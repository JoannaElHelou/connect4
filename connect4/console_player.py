from .game import Grid, Player, Cell


class ConsolePlayer(Player):
    """Allow a human to see the grid in its shell, and input a column from the
    keyboard."""

    def play(self, grid: Grid) -> int:
        print (grid)
        x = int(input ('enter the column number'))
        #line = grid.place (x,Cell.A)
        return x



