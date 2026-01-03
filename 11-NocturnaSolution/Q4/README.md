# Q4 - Emojiology (7 points)

**Objective:** Analyze the sleep trends of Nocturna Solutions employees using Emojicode.

## Context

Nocturna Solutions wants to analyze the sleep trends of its employees to optimize their well-being and productivity. The company has data on bedtime and the sleep state of employees at each subsequent hour. The objective is to analyze these data to draw conclusions.

**Special twist:** The input data are in emojis, the code must be written in **Emojicode**, and the output must also be provided in emojis!

## Instructions

- Review the code to complete in the `solution.emojic` file (methods 🅰️, 🅱️, and ©️).
- Implement the solution in **Emojicode**.
- The input data to process come from the `input.txt` file; parsing of the input data has already been done for you.
- Generate the output in the **console** using the specified format (example in `output_example.txt`).

## Data format

### Input data

- ⭐⭐⭐: Sleep satisfaction levels (1 star = very dissatisfied, 5 stars = very satisfied)
- 🕐XX: Bedtime
- 🛏️😴💭💤: Sleep states at each hour including bedtime (in bed 🛏️, light sleep 😴, REM 💭, deep sleep 💤)

### Statistical analysis to perform

You must produce **3 statistics** from the input lines. See the output format in the `output_example.txt` file.

#### 🏆 Ranking of average satisfaction by bedtime (Method 🅰️)

```
For each bedtime 🕐XX, compute the average satisfaction (in whole stars) and produce a ranking (round to the nearest integer).
```

#### 🕰️ Most frequent sleep state by absolute hour (Method 🅱️)

```
For each hour between 20:00 and 12:00, provide the most frequent sleep state at that hour with its corresponding emoji.

* In case of a tie, use the following priority:
💤 > 💭 > 😴 > 🛏️

** If no data exists for an hour, output no emoji (empty).
```

#### 📊 Average sleep efficiency (Method ©️)

```
For each employee, compute sleep efficiency as the ratio between hours spent asleep (😴, 💭, 💤) and the total recorded hours (including 🛏️).

hours_asleep = #(😴) + #(💭) + #(💤)
total_hours = #(🛏️) + #(😴) + #(💭) + #(💤)
efficiency = hours_asleep / total_hours

Expected emoji output, rounded up (74% = 8/10 green squares):
🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
```

## Example flow

```
Input
⭐⭐⭐ 🕐22 😴💤💤😴💤💤💤🛏️
⭐⭐ 🕐23 💤💤😴💤💭💤🛏️
⭐⭐⭐ 🕐21 😴😴💤💭💤😴🛏️
...

Output (example structure, fictitious values):

🏆
🥇 🕐22 ⭐⭐⭐⭐
🥈 🕐21 ⭐⭐⭐
🥉 🕐23 ⭐⭐

🕰️
🕐20 😴
🕐21 😴
🕐22 💤
🕐23 💭
🕐00 💭
...

📊
🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜
```

## Execution with Docker

To compile and run your Emojicode code, use the provided Docker container:

1. **Build the container (first time only):**

   ```powershell
   cd emojicode-container
   docker-compose build
   ```

2. **Compile and run your .emojic file:**

   **Option A - With the script (recommended on Windows):**

   ```powershell
   .\run-emojicode.ps1 .\solution.emojic
   ```

   **Option B - Manually with Docker:**

   ```powershell
   cd emojicode-container
   docker-compose run --rm emojicode bash -c "emojicodec solution.emojic && ./solution"
   ```

## Resources

- [Emojicode documentation](https://www.emojicode.org/docs/reference/)
- [Emojicode documentation - Standard package](https://www.emojicode.org/docs/packages/s/)

## Evaluation criteria

A solution that does not use Emojicode will not be evaluated. However, you can obtain partial points according to the following criteria:

| Criterion                                | Points | Description                                                                                                                          |
| ---------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Average satisfaction ranking**         | 2      | Correct calculation of average satisfaction by bedtime, appropriate ranking with medals, rounding to the nearest integer             |
| **Most frequent state by absolute hour** | 2      | Correct determination of the dominant state for each hour (20:00–12:00), tie-breaking according to priority, empty output if no data |
| **Average sleep efficiency**             | 2      | Accurate calculation of the hours_asleep/total_hours ratio, correct visual representation with green/white squares, rounding up      |
| **Compilation and execution**            | 1      | Code compiles without error in Emojicode, can be executed, and displays console output in the expected format                        |
| **Total**                                | **7**  |                                                                                                                                      |

\* _Note: Evaluation will be done with a dataset different from the one provided in `input.txt`. A hard-coded solution will not work._
