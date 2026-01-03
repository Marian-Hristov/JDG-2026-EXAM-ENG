# Q1 - Deadlocks (5 points)

**Objective:** Fix/improve a C program that blocks (deadlocks) and clearly explain the changes you made.

## Context

You are given the file `to_debug`, a problem written in C (without the ++).  
Your colleague started part of the work but cannot identify what is wrong with their program.  
The program appears to stop for no obvious reason...

## Instructions

To run the program:

- You can run it locally with a compiler of your choice.
- You can also use an online compiler to test it.

### Command to run the program (after compilation)

```bash
./a.out <numProducers> <numConsumers> <bufferSize>
```

## Technical constraints

- Keep the solution in C (no C++).
- Aim for reproducible execution and observable improvement (fewer deadlocks / better behaviour).

## Resources

- Online C compiler: [OnlineGDB](https://www.onlinegdb.com/online_c_compiler)
- Concepts: producer/consumer, locks (mutex), condition variables (condvar), deadlocks.

## Evaluation criteria

| Criterion                      | Points | Description                                                              |
| ------------------------------ | -----: | ------------------------------------------------------------------------ |
| **Explanations and reasoning** |    2.5 | Written explanation of the changes and diagnosis                         |
| **Execution improvement**      |    2.5 | Execution improved vs. initial (partial points if some deadlocks remain) |
| **Total**                      |  **5** |                                                                          |
