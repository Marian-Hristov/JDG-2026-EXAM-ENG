# Q3 - Officology (7 points)

**Objective:** Implement an algorithm to optimally place the elements in Nocturna Solutions' office to maximize the "Total Joy" score.

## Context

Nocturna Solutions is moving and wants to design the perfect workspace for its **7 consultants**. The space is a grid where some locations are blocked by walls. Your mission is to determine the coordinates $(x, y)$ of each element to create the most productive and happy environment possible.

## Instructions

- Read the room configuration (dimensions and obstacles) from the input file (or use the provided default parameters).
- Place all required elements in the grid.
- Respect all hard constraints.
- Maximize the scoring function defined below.
- Output a file `output.txt` containing the completed grid.

## Output format

Your program must generate a file named `output.txt`.
This file must contain the final grid, strictly matching the dimensions and wall positions of the `input_grid.txt` file.
Characters must correspond to the placed elements (`C`, `M`, `R`, `P`) or empty spaces (`.`).

## Technical specifications

### 1. The grid and distances

- The space is a 2D grid of size $L \times H$.
- The distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is the **Manhattan distance**:
  $$d = |x_1 - x_2| + |y_1 - y_2|$$
- For objects occupying multiple cells (chairs), the distance is the shortest distance to any cell of the object.

### 2. Elements to place

You have the following inventory.

| Symbol | Element        | Required quantity | Description                                             |
| :----: | -------------- | :---------------: | ------------------------------------------------------- |
|  `C`   | Consultant     |   **Exactly 7**   | The employees to satisfy (1x1).                         |
|  `M`   | Coffee machine |   **Exactly 1**   | The heart of the office (1x1).                          |
|  `R`   | Nap chair      |   **Exactly 2**   | **Size 2x1**. Can be placed horizontally or vertically. |
|  `P`   | Plant          |   **Unlimited**   | Decoration (1x1).                                       |
|  `#`   | Wall           |      (Fixed)      | Unusable cell (already present).                        |
|  `.`   | Empty          |         -         | Circulation space.                                      |

## Hard constraints

_If any of these rules is violated, the solution is invalid (Score = 0)._

1. **Uniqueness**: A cell can contain only one element (or one part of an element).
2. **Walls**: No element may be placed on a wall (`#`).
3. **Inventory**: You must place exactly 7 Consultants (`C`), 1 Coffee machine (`M`), and 2 Nap chairs (`R`).
4. **Chair integrity**: Each chair must occupy 2 adjacent cells (horizontally or vertically).
5. **Personal space**: Two consultants cannot be adjacent (neither orthogonally nor diagonally).
6. **Accessibility (flood fill)**: There must exist a path made of empty cells (`.`) allowing each Consultant to reach:
   - The Coffee machine.
   - Both Nap chairs.
   - All other Consultants.
     _Note: The path cannot cross objects or walls, only empty cells._

## Joy calculation formula

The total score is the sum of the individual joy scores of each consultant.
$$Score_{Total} = \sum_{i=1}^{7} Joy(Consultant_i)$$

For a given consultant, joy is calculated as follows:

### A. Caffeine factor (distance)

- If the distance ($d$) to the Coffee machine (`M`) is $\le 3$ cells: **0 points** (too close/noisy).
- If the distance ($d$) is $> 3$ cells: **$15 - (d \times 2)$ points** (minimum 0).

### B. Social factor (bonus/penalty)

For _each_ other consultant in the office:

- If distance $\le 2$: **-10 points** (too much noise/distraction).
- If distance between 3 and 6 (inclusive): **+5 points** (team synergy).
- If distance $> 6$: **0 points** (too far to collaborate).

### C. Environment factor (+1 pt per plant)

- **+1 point** for each Plant (`P`) located in the 8 neighboring cells (adjacent and diagonal) around the consultant.

### D. Well-being factor (+5 pts)

- If the distance to the nearest Nap chair (`R`) is $\le 3$ cells: **+5 points**.
  _(Distance measured to the closest cell of the chair)._

## Resources

- You may use any scripting language (Python, JS, etc.).
- An `input_grid.txt` file (empty grid with walls) is provided for testing.
- **Validation script**: A script `validator.py` is provided to check your solution. DO NOT MODIFY THIS FILE.

```
# Usage
python validator.py output.txt input_grid.txt
```

## Evaluation criteria

| Criterion             | Points | Description                                                                        |
| --------------------- | ------ | ---------------------------------------------------------------------------------- |
| **Solution validity** | 3      | Respect of hard constraints (Inventory, Walls, Personal space, **Accessibility**). |
| **Joy score**         | 3      | Performance of your solution compared to a reference threshold.                    |
| **Code quality**      | 1      | Clarity, functional decomposition, self-documenting code.                          |
| **Total**             | **7**  |                                                                                    |

\* _Note: The office layout used for the final evaluation will be different from the one provided in `input_grid.txt`. A hard-coded solution will not work._
