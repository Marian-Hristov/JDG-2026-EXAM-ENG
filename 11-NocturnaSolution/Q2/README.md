# Q2 - Sloganology (7 points)

**Objective:** Develop an intelligent slogan-generation tool for Nocturna Solutions.

## Context

Alongside its new logo, Nocturna wants to have an intelligent slogan-generation tool. This tool must produce creative, relevant, and grammatically correct slogans that reflect the identity of the consulting company specializing in nocturnal solutions.

## Instructions

Develop a program that **takes as input a list of words** and **generates a grammatically correct slogan** using these words.

### Input format

Your program will receive a list of words from different grammatical categories in a random order:

- Proper nouns (e.g., Nocturna)
- Common nouns (e.g., consulting, solutions, night)
- Adjectives (e.g., intelligent, logical, innovative)
- Verbs (e.g., shine, enlighten, support)

An example of the input format can be found in the **`input.txt` file** located in the same folder as your executable/script. **Each line contains one word**.

**Example `input.txt` file:**

```
Nocturna
consultation
logic
intelligent
night
```

### Output format

Your program must produce a slogan that:

- Uses **all the words provided** in the input
- Respects **grammatical rules** (agreement, conjugation, syntax)
- Forms a **coherent and impactful sentence**
- Reflects the identity of Nocturna Solutions

**Example output:**

```
"Nocturna, logical and intelligent consulting, even at night"
```

## Technical constraints

- **All words** from the input list must be used in the slogan
- The slogan must be **grammatically correct** (agreement in gender/number, valid syntactic structure)
- Words may be **modified** according to grammatical rules (e.g., singular/plural, tense, etc.)
- The **order of words** can be changed to create a coherent sentence
- You may add **other words** (nouns, adjectives, verbs, etc.) to help form a natural and correct sentence
- The slogan must not exceed **100 characters**
- The methodology is up to you, as long as it does not use external LLM APIs. You may use open-source natural language processing (NLP) libraries.

## Additional examples

**Input:** `[Nocturna, solutions, shine, darkness]`  
**Possible output:** `"Nocturna: solutions that shine in the darkness"`

**Input:** `[consulting, night, success, day]`  
**Possible output:** `"consulting by night, success by day"`

**Input:** `[Nocturna, challenges, enlighten, expertise]`  
**Possible output:** `"Nocturna: our expertise enlightens your challenges"`

## Resources

- [NLP and text generation concepts](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Natural language processing](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)
- No starter code is provided; you are free to choose your approach

## Example of valid approaches

- **Template-based approach**: Create sentence templates and insert the words
- **Grammatical approach**: Analyze the grammatical category of the words and build valid sentences
- **Combinatorial approach**: Test different combinations and validate the grammar
- **Rule-based approach**: Define rules for constructing sentences

## Evaluation criteria

| Criterion                        | Points | Description                                                                                                                |
| -------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------- |
| **Complete use of words**        | 2      | All input words are present in the generated slogan; no word is omitted                                                    |
| **Grammatical correctness**      | 2      | Respect of grammatical rules (agreement in gender/number, correct conjugations, valid syntax), coherent sentence structure |
| **Slogan quality and coherence** | 2      | The slogan makes sense, is impactful, reflects the identity of Nocturna Solutions, and is memorable                        |
| **Creativity and arrangement**   | 1      | Ability to arrange words in an original way, creative use of linking words, quality of the formulation                     |
| **Total**                        | **7**  |                                                                                                                            |

\* _Note: Evaluation will be done with several word lists different from the one provided in `input.txt`. A hard-coded solution will not work._
