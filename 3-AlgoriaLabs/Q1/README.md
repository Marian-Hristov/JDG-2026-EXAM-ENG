# Q1 - Navigation in Dream Mazes (6 points)

**Objective:** Develop a pathfinding algorithm to navigate complex dream mazes with teleportation portals, acceleration zones, and temporal obstacles.

## Context

The *Dream Navigation*™ department of Algoria Labs studies optimal navigation in dream environments where physical laws do not always apply. These mazes contain special zones that modify travel time.

In these worlds, travelers encounter:

- **Teleportation Portals**: Instant transport to another position
- **Acceleration Zones**: Reduced temporal movement cost
- **Slowdown Fields**: Increased temporal movement cost
- **Temporal Walls**: Impassable obstacles
- **Normal Terrain**: Standard movement

The goal is to find the fastest path by exploiting these anomalies while avoiding obstacles.

## Instructions

- Complete the provided Python code (`pathfinding_base.py`) to implement your pathfinding algorithm. The base code already includes some utility functions to help you.
- Take into account the different terrain types and their effects on travel time
- Test your code on the provided grids (`dream_maze_X.txt`)
- **Time Limit:** 10 seconds maximum to find the optimal path
- **Output Format:** Path as coordinates (x,y) and total travel time

## Technical Constraints

- **8-directional Navigation:** Movement possible in 8 directions (horizontal, vertical, diagonal)
- **Variable Costs by Terrain:**
  - Normal Terrain: 1.0 time unit
  - Acceleration Zone: 0.3 time unit
  - Slowdown Field: 3.0 time units
  - Teleportation Portal: 0.1 time unit + teleportation

\* _Note: the time unit is spent **after** the movement, based on the destination cell (for example, a move from `(0,0)` to `(0,1)` on normal terrain costs `1.0` time unit)._

- **Diagonal Movement:** Cost × √2 (≈ 1.414) (Euclidean distance)
- **Portal Management:** Each portal has a fixed destination defined in the grid
- Implementation in Python with the provided base code

## Terrain Types (symbols in the grid)

| Symbol | Type                 | Effect                       |
| ------ | -------------------- | ---------------------------- |
| `.`    | Normal Terrain       | Standard cost                |
| `S`    | Start Point          | Start of the path            |
| `E`    | End Point            | Goal to reach                |
| `#`    | Temporal Wall        | Impassable                   |
| `>`    | Acceleration Zone    | Reduced cost (0.3x)          |
| `<`    | Slowdown Field       | Increased cost (3.0x)        |
| `P`    | Teleportation Portal | Teleportation + minimal cost |

## Resources

- [Pathfinding Algorithms](https://en.wikipedia.org/wiki/Pathfinding)
- [Heuristics for Pathfinding](<https://en.wikipedia.org/wiki/Heuristic_(computer_science)>)
- Python Base Code: `pathfinding_base.py`
- Test Grids: `dream_maze_X.txt`

## Evaluation Criteria

**Automatic Failure Conditions (0 points):**

- Exceeding the 10-second time limit
- Invalid path (passing through walls, incorrect coordinates)
- No output or incorrect format
- Algorithm that does not terminate or crashes

**Points Attribution based on successful paths:**

| Successful Paths                             | Points |
| -------------------------------------------- | ------ |
| **Invalid solution or failure**              | 0      |
| **dream_maze_20x20 optimal solution**        | 1      |
| **dream_maze_50x50 optimal solution**        | 1      |
| **dream_maze_60x25 optimal solution**        | 1      |
| **dream_maze_portal_stuff optimal solution** | 1      |
| **dream_maze_200x200 optimal solution**      | 2      |
| **Total**                                    | **6**  |
