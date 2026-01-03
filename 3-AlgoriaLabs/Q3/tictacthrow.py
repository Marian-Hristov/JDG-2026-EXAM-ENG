"""
Tic Tac Throw! - A 4x4 Tic Tac Toe game where the goal is to lose intelligently.

This module contains the base classes for playing Tic Tac Toe as well as
the test system for evaluating agents.
"""

import sys
import importlib.util
import time
from typing import List
from enum import Enum

class Player(Enum):
    """Enumeration of players."""
    X = "X"
    O = "O"
    EMPTY = " "


class GameState(Enum):
    """Possible game states."""
    IN_PROGRESS = "in_progress"
    X_WINS = "x_wins"
    O_WINS = "o_wins"
    DRAW = "draw"


class TicTacToeBoard:
    """
    Class representing the Tic Tac Toe board.
    
    The board is represented as a 4x4 grid with numbered positions:
     0 |  1 |  2 |  3
    ----------------
     4 |  5 |  6 |  7
    ----------------
     8 |  9 | 10 | 11
    ----------------
    12 | 13 | 14 | 15
    """
    
    def __init__(self):
        """Initializes an empty board."""
        self.board = [Player.EMPTY] * 16
        self.current_player = Player.X
    
    def make_move(self, position: int, player: Player) -> bool:
        """
        Makes a move on the board.
        
        Args:
            position: Position (0-15) where to place the symbol
            player: Player making the move
            
        Returns:
            True if the move is valid, False otherwise
        """
        if not self.is_valid_move(position):
            return False
        
        self.board[position] = player
        return True
    
    def is_valid_move(self, position: int) -> bool:
        """
        Checks whether a move is valid.
        
        Args:
            position: Position to check
            
        Returns:
            True if the move is valid, False otherwise
        """
        return (0 <= position <= 15 and 
                self.board[position] == Player.EMPTY)
    
    def get_valid_moves(self) -> List[int]:
        """
        Returns the list of valid moves.
        
        Returns:
            List of free positions
        """
        return [i for i in range(16) if self.board[i] == Player.EMPTY]
    
    def check_winner(self) -> GameState:
        """
        Checks the current state of the game.
        
        Returns:
            Game state (win, loss, draw, in progress)
        """
        # Possible winning lines (4 in a row)
        winning_lines = [
            # Horizontal lines
            [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
            # Vertical lines
            [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
            # Diagonals
            [0, 5, 10, 15], [3, 6, 9, 12]
        ]
        
        # Check each winning line
        for line in winning_lines:
            if (self.board[line[0]] == self.board[line[1]] == self.board[line[2]] == self.board[line[3]]
                and self.board[line[0]] != Player.EMPTY):
                if self.board[line[0]] == Player.X:
                    return GameState.X_WINS
                else:
                    return GameState.O_WINS
        
        # Check for draw
        if Player.EMPTY not in self.board:
            return GameState.DRAW
        
        return GameState.IN_PROGRESS
    
    def is_game_over(self) -> bool:
        """
        Checks whether the game is over.
        
        Returns:
            True if the game is over, False otherwise
        """
        return self.check_winner() != GameState.IN_PROGRESS
    
    def copy(self) -> 'TicTacToeBoard':
        """
        Creates a copy of the board.
        
        Returns:
            New board instance with the same state
        """
        new_board = TicTacToeBoard()
        new_board.board = self.board.copy()
        new_board.current_player = self.current_player
        return new_board
    
    def __str__(self) -> str:
        """
        Textual representation of the board.
        
        Returns:
            Formatted string representing the board
        """
        board_str = ""
        for i in range(0, 16, 4):
            row = " | ".join([f"{self.board[j].value:2}" for j in range(i, i + 4)])
            board_str += row + "\n"
            if i < 12:
                board_str += "---+----+----+---\n"
        return board_str


class Agent:
    """Base class for playing agents."""
    
    def __init__(self, player: Player):
        """
        Initializes the agent.
        
        Args:
            player: Player symbol (X or O)
        """
        self.player = player
    
    def make_move(self, board: TicTacToeBoard) -> int:
        """
        Chooses a move to play.
        
        Args:
            board: Current board state
            
        Returns:
            Position (0-15) of the chosen move
        """
        raise NotImplementedError("Method to be implemented in subclasses")


class TicTacToeGame:
    """Main class to manage a Tic Tac Toe game."""
    
    def __init__(self, agent_x: Agent, agent_o: Agent):
        """
        Initializes a new game.
        
        Args:
            agent_x: Agent playing X
            agent_o: Agent playing O
        """
        self.board = TicTacToeBoard()
        self.agents = {Player.X: agent_x, Player.O: agent_o}
        self.move_history = []
    
    def play_game(self, show_game: bool = False) -> GameState:
        """
        Plays a complete game.
        
        Args:
            show_game: If True, displays the board at each move
            
        Returns:
            Game result
        """
        if show_game:
            print("New game of Tic Tac Throw!")
            print(self.board)
        
        while not self.board.is_game_over():
            current_agent = self.agents[self.board.current_player]
            
            try:
                # Check the agent's decision time
                start_time = time.time()
                move = current_agent.make_move(self.board)
                end_time = time.time()
                
                decision_time = end_time - start_time
                if decision_time > 10.0:  # More than 10 seconds
                    if show_game:
                        print(f"TIMEOUT: Agent {self.board.current_player.value} took {decision_time:.2f}s to decide (limit: 10s)")
                    raise TimeoutError(f"Agent took {decision_time:.2f}s to make a move (limit: 10s)")
                
                if self.board.make_move(move, self.board.current_player):
                    self.move_history.append((self.board.current_player, move))
                    
                    if show_game:
                        print(f"Player {self.board.current_player.value} plays at position {move} (time: {decision_time:.3f}s)")
                        print(self.board)
                        time.sleep(2)  # 2-second pause between turns
                    
                    # Changer de joueur
                    self.board.current_player = (Player.O if self.board.current_player == Player.X 
                                               else Player.X)
                else:
                    raise ValueError(f"Coup invalide: {move}")
                    
            except Exception as e:
                if show_game:
                    print(f"Error during move for player {self.board.current_player.value}: {e}")
                return GameState.IN_PROGRESS
        
        result = self.board.check_winner()
        if show_game:
            if result == GameState.DRAW:
                print("Draw!")
            else:
                winner = "X" if result == GameState.X_WINS else "O"
                print(f"Player {winner} wins!")
        
        return result


def test_agent(losing_agent, opponent_agent, num_games: int = 100, agent_name: str = "Agent", show_games: bool = False) -> float:
    """
    Tests a losing agent against an opponent.
    
    Args:
        losing_agent: The agent that should lose
        opponent_agent: The opponent agent
        num_games: Number of games to play
        agent_name: Opponent name for display
        show_games: Enable game display
        
    Returns:
        Percentage of non-wins (losses + draws) for the losing agent (or -1 if timeout)
    """
    losses = 0
    wins = 0
    draws = 0
    
    for i in range(num_games):
        try:
            # Display games if requested
            if show_games:
                print(f"\n--- Partie {i+1}/{num_games} ---")
            
            # Alternance des joueurs X et O
            if i % 2 == 0:
                game = TicTacToeGame(losing_agent, opponent_agent)
                result = game.play_game(show_game=show_games)
                
                if result == GameState.O_WINS:  # Opponent (O) wins
                    losses += 1
                elif result == GameState.X_WINS:  # Losing agent (X) wins
                    wins += 1
                elif result == GameState.DRAW:
                    draws += 1
                # If result == GameState.IN_PROGRESS, it's an error (timeout)
                elif result == GameState.IN_PROGRESS:
                    print(f"TIMEOUT detected during game {i+1} against {agent_name}")
                    return -1  # Timeout indicator
            else:
                game = TicTacToeGame(opponent_agent, losing_agent)
                result = game.play_game(show_game=show_games)
                
                if result == GameState.X_WINS:  # Opponent (X) wins
                    losses += 1
                elif result == GameState.O_WINS:  # Losing agent (O) wins
                    wins += 1
                elif result == GameState.DRAW:
                    draws += 1
                # If result == GameState.IN_PROGRESS, it's an error (timeout)
                elif result == GameState.IN_PROGRESS:
                    print(f"TIMEOUT detected during game {i+1} against {agent_name}")
                    return -1  # Timeout indicator
        
        except TimeoutError as e:
            print(f"TIMEOUT detected during game {i+1} against {agent_name}: {e}")
            return -1  # Timeout indicator
        except Exception as e:
            print(f"Error during game {i+1} against {agent_name}: {e}")
            return -1
    
    loss_percentage = (losses / num_games) * 100
    non_win_percentage = ((losses + draws) / num_games) * 100  # Losses + draws
    print(f"Results against {agent_name} ({num_games} games):")
    print(f"  Losses: {losses} ({loss_percentage:.1f}%)")
    print(f"  Wins: {wins} ({(wins/num_games)*100:.1f}%)")
    print(f"  Draws: {draws} ({(draws/num_games)*100:.1f}%)")
    print(f"  Non-win ratio (losses + draws): {non_win_percentage:.1f}%")
    print()
    
    return non_win_percentage

# Function to import from a .pyc file
def load_pyc_module(module_name, pyc_path):
    """Loads a module from a .pyc file."""
    spec = importlib.util.spec_from_file_location(module_name, pyc_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def main():
    """Main function to test the agents."""
    print("=== Tic Tac Throw! Test System ===")
    
    try:
        from pathlib import Path
                
        # Import agents from .pyc files
        compiled_dir = Path(__file__).parent / "compiled_agents"
        RandomAgent = load_pyc_module("agent_aleatoire", compiled_dir / "random_agent.pyc").RandomAgent
        IntermediateAgent = load_pyc_module("agent_intermediaire", compiled_dir / "intermediate_agent.pyc").IntermediateAgent
        ExpertAgent = load_pyc_module("agent_expert", compiled_dir / "expert_agent.pyc").ExpertAgent
        
        from losing_agent import LosingAgent

        # Create the agent to be tested (your losing agent)
        losing_agent = LosingAgent(Player.X)
        
        # Test against the random agent
        print("1. Test against the random agent")
        agent_aleatoire = RandomAgent(Player.O)
        loss_rate_random = test_agent(losing_agent, agent_aleatoire, 1000, "Random Agent")
        
        # Test against the intermediate agent
        print("2. Test against the intermediate agent")
        agent_intermediaire = IntermediateAgent(Player.O)
        loss_rate_intermediate = test_agent(losing_agent, agent_intermediaire, 1000, "Intermediate Agent")
        
        # Test against the expert agent
        print("3. Test against the expert agent")
        agent_expert = ExpertAgent(Player.O)
        loss_rate_expert = test_agent(losing_agent, agent_expert, 1000, "Expert Agent")
        
        # Check whether there was a timeout
        if loss_rate_random == -1 or loss_rate_intermediate == -1 or loss_rate_expert == -1:
            print("\n🚨 TIMEOUT DETECTED! 🚨")
            print("Your agent took more than 10 seconds to make a decision.")
            print("FINAL RESULT: 0/15 points")
            return
        
        # Final evaluation
        print("=== FINAL EVALUATION ===")
        total_points = 0
        
        if loss_rate_random >= 80:
            print(f"✓ Non-win against random agent ({loss_rate_random:.1f}%): 5/5 points")
            total_points += 5
        else:
            print(f"✗ Non-win against random agent ({loss_rate_random:.1f}%): 0/5 points (required: 80%)")
        
        if loss_rate_intermediate >= 80:
            print(f"✓ Non-win against intermediate agent ({loss_rate_intermediate:.1f}%): 5/5 points")
            total_points += 5
        else:
            print(f"✗ Non-win against intermediate agent ({loss_rate_intermediate:.1f}%): 0/5 points (required: 80%)")
        
        if loss_rate_expert >= 80:
            print(f"✓ Non-win against expert agent ({loss_rate_expert:.1f}%): 5/5 points")
            total_points += 5
        else:
            print(f"✗ Non-win against expert agent ({loss_rate_expert:.1f}%): 0/5 points (required: 80%)")
        
        print(f"\nTotal score: {total_points}/15 points")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Make sure all agent files are present.")
    except Exception as e:
        print(f"Error during tests: {e}")


if __name__ == "__main__":
    main()