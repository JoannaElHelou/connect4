from .game import Grid, Player,Cell


class CheaterB(Player):
    """This IA cheats and modify the grid to ensure player B wins."""

    def play(self, grid: Grid) -> int:
        print (grid)
        grid.place(1,Cell.B)
        grid.place(1,Cell.B)
        grid.place(1,Cell.B)
        
        return 1
