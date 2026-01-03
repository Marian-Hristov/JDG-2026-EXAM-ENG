# Mandate 2 – Database - Somnia Data

## Context

Somnia Data is a company specializing in data management and analysis, with the slogan: "We keep
your dreams in mind". It aims to develop a web-based platform enabling users to store their sleep
profiles, receive personalized recommendations and follow intervention plans designed to improve the
quality of their sleep.

Each user must have an account on the platform before being able to access the services. A user is
characterized by a unique identifier, a first name, a last name, an address (street, city, postal code) and
an e-mail address. Users can save multiple sleep profiles, each including detailed preferences
(mattress type, firmness, temperature, sleeping position, night-time habits).

For each profile, the platform can generate several personalized intervention plans, identified by a
unique number and a creation date. Each intervention plan can contain several recommendations
(relaxation exercises, habit adjustments, sleep schedules), a description and a status indicating
whether it is active, completed or pending.

For administration and performance optimization, the platform keeps track of logs and statistics on
profiles, action plans and recommendations. Each log is identified by a unique identifier and contains
the action taken, a description and the date. Logs are rarely accessed and are used for debugging
purposes only.

Your task is to model a database designed to manage the Somnia Data platform. You'll need to identify
all entities, their attributes, associations between them, cardinalities and association types (binary 1:n,
n:m, etc.).
