# Q3 - Tic Tac Throw! (7 points)

**Objective:** Implement an artificial agent that plays Tic Tac Toe (4x4) systematically sub-optimally, in order to maximize its chances of losing against an opponent who is also trying to lose.

## Context

The Idiot Factory™ department of Algoria Labs is interested in an original challenge: developing agents capable of playing 4x4 Tic Tac Toe by actively trying to lose.

The 4x4 Tic Tac Toe game is played on a 4x4 grid. Two players compete by alternately placing their symbols (X and O) on the grid. The goal is to align 4 consecutive symbols horizontally, vertically, or diagonally. However, in this challenge, each agent must adopt a strategy aimed at avoiding victory, by trying to lose against an opponent who follows the same logic.

## Instructions

- Examine the provided base code in the `tictacthrow.py` file
- Implement the `LosingAgent` class in the `losing_agent.py` file which must play sub-optimally
- Your agent must be able to lose against an opponent who is also trying to lose
- Test your implementation with different opponent strategies (random, intermediate, expert)
- **CRITICAL CONSTRAINT**: Each decision of your agent must be made in less than 10 seconds, otherwise the evaluation will automatically be 0 points

## Resources

- [Tic Tac Toe Algorithms](https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy)
- [Python Documentation for Classes](https://docs.python.org/3/tutorial/classes.html)
- Base code available in the Github repo

## Evaluation Criteria

**ATTENTION**: If your agent takes more than 10 seconds to make a decision during any move, the evaluation stops immediately and you will have 0 points.

**Evaluation Metric**: The non-victory ratio is calculated as follows:

```
Non-victory Ratio = (Losses + Draws) / Total Games
```

An agent that loses or draws is considered to have succeeded in avoiding winning.

| Criteria                                   | Points | Description                                                                                |
| ------------------------------------------ | ------ | ------------------------------------------------------------------------------------------ |
| **Non-victory against random agent**       | 2      | Your agent does not win (loses or draws) against the random agent at least 80% of the time |
| **Non-victory against intermediate agent** | 2.5    | Your agent does not win against the intermediate agent at least 80% of the time            |
| **Non-victory against expert agent**       | 2.5    | Your agent does not win against the expert agent in defeat at least 80% of the time        |
| **Total**                                  | **7**  |                                                                                            |
