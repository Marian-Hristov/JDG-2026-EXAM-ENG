"""
Base code for the navigation algorithm in dream mazes
AlgoriaLabs - Q1

This file contains the basic structure and utility functions.
Complete the sections marked TODO to implement your pathfinding algorithm.
"""

import time
import os
import re
from typing import List, Tuple, Optional

class DreamMaze:
    """Class for handling the dream maze and its special properties."""
    
    # Terrain costs
    TERRAIN_COSTS = {
        '.': 1.0,    # Normal terrain
        'S': 1.0,    # Start point
        'E': 1.0,    # End point
        '>': 0.3,    # Acceleration zone
        '<': 3.0,    # Slowdown field
        'P': 0.1,    # Teleportation portal
        '#': float('inf')  # Temporal wall (impassable)
    }
    
    # Movement directions (8-directional)
    DIRECTIONS = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    def __init__(self, maze_file: str):
        """Initializes the maze from a file."""
        self.grid = []
        self.start = None
        self.end = None
        self.portals = {}  # Dict: position -> destination
        self.width = 0
        self.height = 0
        
        self.load_maze(maze_file)
    
    def load_maze(self, maze_file: str):
        """Loads the maze from a file."""
        try:
            with open(maze_file, 'r') as f:
                lines = f.readlines()
            
            # First line contains the information about portals
            portal_info = lines[0].strip()
            if portal_info.startswith("PORTALS:"):
                portal_data = portal_info[8:].strip()
                if portal_data:
                    # Format: (x1,y1)->(x2,y2) or multiple: (x1,y1)->(x2,y2),(x3,y3)->(x4,y4)
                    portal_pattern = r'\((\d+),(\d+)\)->\((\d+),(\d+)\)'
                    matches = re.findall(portal_pattern, portal_data)
                    for match in matches:
                        src_x, src_y, dst_x, dst_y = map(int, match)
                        self.portals[(src_x, src_y)] = (dst_x, dst_y)
            
            # The remaining lines contain the grid
            grid_lines = lines[1:]
            self.grid = []
            
            for y, line in enumerate(grid_lines):
                row = list(line.strip())
                self.grid.append(row)
                
                for x, cell in enumerate(row):
                    if cell == 'S':
                        self.start = (x, y)
                    elif cell == 'E':
                        self.end = (x, y)
            
            self.height = len(self.grid)
            self.width = len(self.grid[0]) if self.grid else 0
            
        except FileNotFoundError:
            print(f"Error: File {maze_file} not found.")
            raise
    
    def is_valid_position(self, x: int, y: int) -> bool:
        """Checks whether a position is valid in the grid."""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def get_terrain_cost(self, x: int, y: int) -> float:
        """Returns the movement cost for a given position."""
        if not self.is_valid_position(x, y):
            return float('inf')
        
        cell = self.grid[y][x]
        return self.TERRAIN_COSTS.get(cell, 1.0)
    
    def get_neighbors(self, pos: Tuple[int, int]) -> List[Tuple[Tuple[int, int], float]]:
        """
        Returns accessible neighbors and their movement cost.
        
        Args:
            pos: Current position (x, y)
            
        Returns:
            List of tuples (neighbor_position, movement_cost)
        """
        x, y = pos
        neighbors = []
        
        # TODO: Implement the logic to handle portals and terrain costs
        # If you don't think you need this function, you may ignore it.
        
        return neighbors
    
    def print_path_on_grid(self, path: List[Tuple[int, int]]):
        """Displays the grid with the path found."""
        if not path:
            print("No path to display.")
            return
        
        # Create a copy of the grid
        display_grid = [row[:] for row in self.grid]
        
        # Mark the path (except start and end)
        for i, (x, y) in enumerate(path):
            if (x, y) != self.start and (x, y) != self.end:
                display_grid[y][x] = '*'
        
        # Display the grid with spaces around each character
        print("\nGrid with the path found (* = path):")
        for row in display_grid:
            print(' '.join(row))


class PathfindingAlgorithm:
    """Main class for the pathfinding algorithm."""
    
    def __init__(self, maze: DreamMaze):
        self.maze = maze
    
    def find_path(self) -> Tuple[Optional[List[Tuple[int, int]]], float]:
        """
        Finds the optimal path from the start point to the end.
        
        Returns:
            Tuple (path, total_cost) where:
            - path: List of coordinates (x, y) of the optimal path, or None if no path
            - total_cost: Total cost of the path found
        """
        
        if not self.maze.start or not self.maze.end:
            print("Error: Start or end point not defined.")
            return None, float('inf')
        
        # TODO: Implémentez votre algorithme ici
        
        # Aucun chemin trouvé
        return None, float('inf')


def main():
    """Main function to test the algorithm."""
    try:
        # Load the maze
        # TODO: You can change the file name to test other mazes
        script_dir = os.path.dirname(os.path.abspath(__file__))
        maze_file = os.path.join(script_dir, './dream_maze/dream_maze_20x20.txt')
        maze = DreamMaze(maze_file)
        
        print(f"Maze loaded: {maze.width}x{maze.height}")
        print(f"Start: {maze.start}, End: {maze.end}")
        print(f"Portals: {maze.portals}")
        
        # Créer l'algorithme de recherche
        pathfinder = PathfindingAlgorithm(maze)
        
        # Measure execution time
        start_time = time.time()
        path, total_cost = pathfinder.find_path()
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        # Display results
        if path:
            print(f"\n=== SOLUTION FOUND ===")
            print(f"Path: {path}")
            print(f"Total cost: {total_cost:.2f}")
            print(f"Number of steps: {len(path) - 1}")
            print(f"Execution time: {execution_time:.3f} seconds")
            
            # Display the grid with the path
            maze.print_path_on_grid(path)
            
            # Time limit validation
            if execution_time > 10.0:
                print("⚠️ WARNING: Time limit exceeded (10 seconds)")
        else:
            print("❌ FAILURE: No path found")
    
    except Exception as e:
        print(f"Error during execution: {e}")


if __name__ == "__main__":
    main()