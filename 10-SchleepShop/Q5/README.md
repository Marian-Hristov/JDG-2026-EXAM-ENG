# Q5 - Prompt engineering (3 points)

**Objective:** Design robust prompts (system + user) for a generative AI so that it produces personalized sleep plans.

## Context

SchleepShop wants to automate the generation of personalized sleep plans. The prompts must be designed to guide an AI so that it returns a structured, clear plan adapted to the user's data.

**Important constraint:** The AI is restricted in the context of the exam, so you are not allowed to test your prompts. Rely only on prompt engineering theory.

## Instructions

- Write the prompts in English.

## Description of the prompts to complete

- **System prompt**: A set of instructions intended for the AI to define its role, set boundaries for its responses, specify the tone to adopt, and structure the expected output format. In the context of this mandate, the AI's role is that of a sleep expert capable of providing recommendations based on the best clinical and scientific practices.

- **User prompt**: A template of questions or fields to be filled in by the user, allowing the collection of the information needed to personalize the sleep plan. In the context of this mandate, the user prompt must make it possible to collect data such as age, sleep habits, issues encountered, and the user's specific goals.

## Expected deliverables

- `prompt_system.txt`
- `prompt_user.txt`

## Resources

- [Prompt Engineering Techniques (Prompting Guide)](https://www.promptingguide.ai/techniques)
- [Best Practices for Prompt Engineering (OpenAI Help)](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [Prompt Design Guide (Anthropic)](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)

## Evaluation criteria

| Criterion                        | Points | Description                                                                    |
| -------------------------------- | ------ | ------------------------------------------------------------------------------ |
| **System prompt**                | 1      | Clear role, safety constraints, defined output format (JSON/Markdown schema)   |
| **User prompt**                  | 1      | Complete variables, clear template, instructions on format and level of detail |
| **Application of PE principles** | 0.75   | Specificity, use of explicit patterns                                          |
| **Edge-case handling**           | 0.25   | Identification of risky situations and fallback instructions                   |
| **Total**                        | **3**  |                                                                                |
