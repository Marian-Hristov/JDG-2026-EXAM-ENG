"""
Losing agent for Tic Tac Throw!

THIS CLASS IS TO BE IMPLEMENTED BY THE STUDENT!

The agent must avoid winning while losing convincingly,
even against an opponent who is also trying to lose.
"""

from typing import List
from tictacthrow import Agent, TicTacToeBoard, Player


class LosingAgent(Agent):
    """
    Agent that aims to lose optimally.
    
    THIS CLASS IS TO BE IMPLEMENTED!
    
    The agent must avoid winning while losing convincingly,
    even against an opponent who is also trying to lose.
    """
    
    def __init__(self, player: Player):
        """
        Initializes the losing agent.
        
        Args:
            player: Player symbol (X or O)
        """
        super().__init__(player)
        # TODO: Add necessary attributes
        pass
    
    def make_move(self, board: TicTacToeBoard) -> int:
        """
        Chooses a suboptimal move.
        
        Args:
            board: Current board state
            
        Returns:
            Position of the chosen move (0-15)
        """
        # TODO: Implement the logic for a suboptimal choice
        # This method must return a move that maximizes the chances of losing
        valid_moves = board.get_valid_moves()
        if not valid_moves:
            raise ValueError("No valid move available")
        
        return valid_moves[0]
    
    