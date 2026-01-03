# Q1 - Backend Server (8 points)

**Objective:** Expose **GET** endpoints (to populate dropdowns) and a **POST** endpoint (to randomize items) based on external APIs, with proper error handling.

## Context

Your team is tasked with designing and deploying a backend server capable of supporting an application that helps users plan their party nights (heavy-drinking evenings).

The backend must aggregate several public APIs (cocktails, meals, games, music) in order to provide dynamic lists for a future frontend.

The goal is to allow the user to generate a high-level plan for an evening (choices of cocktails, meals, games, music playlists) in an interactive and personalized way.

## Instructions

- Implement the necessary **GET** endpoints to obtain the options for each category (ingredients, categories, genres, etc.).
- Implement a **POST** endpoint that receives the lists/choices and returns randomized items.
- Error tolerance: if an external API is unreachable, return **500** without crashing.

## Expected deliverable

You work with **4 categories of items**:

- **Cocktails**
- **Meals**
- **Video games**
- **Music**

For **each category**, you must expose routes that allow:

- **1 GET** that returns _all sub-elements_ used to populate dropdowns (e.g. ingredients, categories, genres, etc.).
- **1 GET** that returns a _list of filtered items_ based on one or more sub-elements/types provided as parameters (e.g. selected ingredients, selected game category, selected music genre).

Globally, you must also expose:

- **1 POST** that receives the user’s choices/criteria (lists of selected sub-elements) and returns a **randomized plan**:
  - **1 cocktail**
  - **1 meal**
  - **1 video game**
  - **5 songs**

```
# Example
- A cocktail with [Gin] (ingredient).
- A meal with [Chicken] (ingredient).
- A game of type [Shooter] (category).
- A list of 5 songs of type [Rock] (genre).
```

## Expected HTTP status codes

Each route must return the **appropriate HTTP status code** together with the data:

- **20X** if the request succeeds and returns data (e.g. `200 OK`).
- **40X** if the request is valid but **no item is available** for the given criteria (e.g. `404 Not Found`).
- **50X** in case of server error, especially if an **external API is unreachable / failing** (e.g. `500 Internal Server Error`) — the server must not crash.

> Tip: you can also use `400 Bad Request` if required parameters are missing or malformed.

## Bonus (2 points)

The bonus can only bring your grade up to a maximum of **100%** of the exercise value:

- Implement basic authentication:
  - A **POST** `/login` with `www-form-encoded` that returns a `SET_COOKIE` containing the username as a string.
  - The request must include `username` and `password` as strings, validated from an array read from a JSON file.
  - Return **401 Unauthorized** for **GET/POST** requests if the user is not authenticated (via `SET_COOKIE`).

## APIs to use

- [The Cocktail DB](https://www.thecocktaildb.com/api.php)
- [The Meal DB](https://www.themealdb.com/api.php)
- [MMOBomb API](https://www.mmobomb.com/api)
- [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API#Application_rate_limiting_and_identification)
  - Please read the instructions to respect the constraints (for example user-agent string).

**If you have connectivity issues with external APIs:**

Describe how minimal support for this API could be implemented.  
Hard-code a few fallback options as a backup solution.

## Technical constraints

- You must use the APIs listed above to obtain the data.
- Respect the API limitations (e.g. MusicBrainz: user-agent / rate limiting).
- The stack must be available to the graders so they can run the application. Allowed languages:

  - **JavaScript/TypeScript/Node**
  - **Java** (Specify the setup with the installed Java version, ideally via SDKMAN).
  - **Rust**
  - **C#**
  - **Python**

- You do not need to reuse `./backend-example.py`; it is only there to highlight the routes to implement with an example of code.
- Bonus: if authentication is implemented, protect your routes via cookie and return **401** when the user is not authenticated.

## Client.py

Contains an example of the calls that could be made to test your API.  
If you implement the bonus, you must modify `Client.py` to support authentication.

## Evaluation criteria

| Criterion                     | Points | Description                                                                                            |
| ----------------------------- | -----: | ------------------------------------------------------------------------------------------------------ |
| **GET - Options (dropdowns)** |      1 | 1 GET per category to dynamically return sub-elements (ingredients, categories, genres, etc.).         |
| **GET - Filtered items**      |      1 | 1 GET per category to return a list of items based on parameters (filters).                            |
| **POST - Randomization**      |      2 | 1 POST that composes the final result (1 cocktail, 1 meal, 1 game, 5 songs) from the received choices. |
| **HTTP status + robustness**  |      2 | 20X if OK, 40X if no result, 50X if error (external API down => 500) without crashing.                 |
| **Code quality**              |      2 | Reusable/modular code (methods/classes), clarity, separation of concerns, error handling.              |
| **Bonus: Auth**               |   +2.0 | `/login` (form-encoded) + cookie + `401` protection.                                                   |
| **Total**                     |  **8** | Capped at 8 points.                                                                                    |
