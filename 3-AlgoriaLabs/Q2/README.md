# Q2 - Block Stacking Optimization (15 points)

**Objective:** Develop an algorithm to maximize the height of a tower of blocks, respecting resistance, dimensions, and fragility constraints.

## Context

The *To Infinity And Beyond*™ department wishes to stack blocks of different dimensions to build stable and compact towers, ready to be shipped into space. The current system, based on naive sorting, does not allow reaching the desired heights.

Each block has:

- Width (w), depth (d), height (h)
- Weight (p)
- Maximum resistance (r): total weight supported above
- Type: fragile, standard, or robust

The goal is to design an efficient algorithm to optimize stacking while ensuring stability and accessibility.

## Instructions

- Implement an optimization algorithm respecting all constraints (programming language of choice).
- Test your code on the `blocks_X.txt` files
- **Time Limit:** 30 seconds to find the best configuration
- **Output Format:** Your program can display multiple successive solutions during the 30 seconds. The **last output in the console** will be considered your final solution, whether valid or not.
- **Valid Output:** Must contain the total height of the tower and the ordered list of block ids used (from bottom to top).

## File Format blocks.txt

The `blocks_X.txt` files list the data of available blocks to stack, with one block per line. Each line of the file contains the following information separated by spaces:

```
id weight resistance width depth height type
```

**Field Description:**

- `id`: Unique block identifier (integer)
- `weight`: Block weight in units (integer)
- `resistance`: Maximum resistance the block can support (integer)
- `width`: Block width in units (integer)
- `depth`: Block depth in units (integer)
- `height`: Block height in units (integer)
- `type`: Product type (`fragile`, `standard`, or `robuste`)

**Example:**

```
20 2002 3000000 120 123 123 fragile
21 1500 2500000 115 118 110 standard
22 3000 5000000 140 145 150 robuste
```

## Technical Constraints

- **Mechanical Resistance:** The cumulative weight of blocks placed above a block must not exceed its maximum resistance
- **Strictly Decreasing Dimensions:** A block can only be placed on a block strictly wider and deeper: $w_{top} < w_{bottom}$ and $d_{top} < d_{bottom}$
- **Fragility Constraint:** A fragile block must always be above standard or robust blocks
- Implementation in programming language of choice (Python, Java, C++, C#, etc.)

## Resources

- [Combinatorial Optimization Algorithms](https://en.wikipedia.org/wiki/Combinatorial_optimization)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Genetic Algorithms for Optimization](https://en.wikipedia.org/wiki/Genetic_algorithm)

## Evaluation Criteria

**Automatic Failure Conditions (0 points):**

- Invalid solution (non-compliance with constraints)
- Exceeding the allotted time (30 seconds) before a first output
- Absence of valid output in the console (total height + list of indices)
- Hardcoded valid output (we want an algorithm, not a pre-calculated solution)

Your algorithm will be tested on 5 datasets (500 to 1M blocks). Each execution is worth 1.2 points depending on the height reached:

| Height Reached               | Points |
| ---------------------------- | ------ |
| Invalid solution or failure  | 0      |
| ≥ 75% of max possible height | 0.4    |
| ≥ 90% of max possible height | 0.8    |
| 100% of max possible height  | 1.2    |

**Note:** Only the last displayed output will be taken into account. You can therefore display intermediate outputs during your solution search.

Example of valid output:

```
Height: 1234
Blocks: 10 2893 3593 3152 2853 234 5763 9003 657 5360 2165 4915 409 9022 303 6002
```
