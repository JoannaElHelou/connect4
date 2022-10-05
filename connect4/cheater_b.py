from .game import Grid, Player


class CheaterB(Player):
    """this IA cheats and modify the grid to ensure player B wins."""
    
    def play(self, grid: Grid) -> int:
        ...
