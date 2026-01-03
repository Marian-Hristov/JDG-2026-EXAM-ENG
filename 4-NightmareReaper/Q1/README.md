# Q1 - Capture the Flag (9 points)

**Objective:** Find up to **3 flags** of the form **"FLAGXYZ"** in the application (in a **docker-compose** environment) and provide, for each flag, a **reproducible method** to obtain it.

## Context

You are working on a Docker Compose environment designed as a mini-CTF. The evaluation is based both on your ability to find the flags and on the **quality of your approach** (where you look, which actions you take, and why).

## Instructions

- Start the Docker Compose environment.
- Find **3 flags**.
- For each flag, document a clear and reproducible method (steps, tool used, where the information is located).

## Startup / Execution

Using **docker compose**, go to the file’s root folder and run the following command to start the environment:

```pwsh
docker compose up -d
```

The ports in use are listed in **docker-compose.yml** to help you start your work.
(By default, simply open **localhost** in the browser.)

## ARM machines

The setup is built for **x86/x64 (Intel/AMD)**; you must use **Rosetta** to fully benefit from the containers on **Mac M1/M2** machines.

If you cannot use Rosetta, you must remove the `ctf-web-user` image, and some features may not work as expected / the challenge may be harder. But it is still doable without Rosetta.

## Resources

- Browser developer tools (F12): storage, network, console, etc.
- `docker-compose.yml` file (exposed ports and services).

## Tips

- Check your browser tools, stored data, messages (F12), etc. Developers may be exposing too much information about their environment and how it works ;)
- `ctf-web-user` uses the domain `ctf-web:3000` for its requests.
- `ctf-web-user` uses a “modern” browser with standard requirements such as CORS.

## Evaluation criteria

Each **flag** is worth up to **3 points** depending on the quality of the approach. A flag without justification is worth **0**.

| Criterion            | Points | Description                               |
| -------------------- | -----: | ----------------------------------------- |
| **Flag #1 + method** |      3 | Flag found + precise, reproducible method |
| **Flag #2 + method** |      3 | Flag found + precise, reproducible method |
| **Flag #3 + method** |      3 | Flag found + precise, reproducible method |
| **Total**            |  **9** |                                           |

_Examples of invalid justifications (0 points):_

- I decompiled the Docker images and read the app’s source files directly... (weakness due to the CTF Docker setup; this would not be acceptable on a production environment).
- I read directly from the **Postgres DB** in the **docker-compose** (since the settings are publicly available...).
