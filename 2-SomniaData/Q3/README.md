# Q3 - SQL Queries (5 points)

**Objective:** For the schema you proposed in question 2, write the SQL queries in the corresponding `REQUEST_X.sql` files.

## Instructions

- Complete the files `REQUEST_1.sql` to `REQUEST_5.sql` in this directory
- Use the MySQL language if possible
- Base yourself on your schema from question 2.2
- Optimize queries for performance
- Comment complex queries

## Queries to implement

### 1. REQUEST_1.sql

Retrieve the list of users with more than 3 active intervention plans.

### 2. REQUEST_2.sql

Retrieve a list of all the profiles of a given user (user id = 42) with its number of pending
intervention plans.

### 3. REQUEST_3.sql

Retrieve all non-active recommendations for a given plan (plan id = 30).

### 4. REQUEST_4.sql

Retrieve the history of actions in the logs for a given user (user id = 42) on his plans and
recommendations, sorted in descending order according to their creation date

### 5. REQUEST_5.sql

Retrieve all intervention plans with their associated profile and user created between
December 1st and January 1st, sorted chronologically by creation date.

## Resources

- [MySQL Queries Documentation](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [MySQL JOIN Types](https://dev.mysql.com/doc/refman/8.0/en/join.html)

## Evaluation Criteria

| Criteria          | Points | Description                                   |
| ----------------- | ------ | --------------------------------------------- |
| **REQUEST_1.sql** | 1      | The query correctly returns what is requested |
| **REQUEST_2.sql** | 1      | The query correctly returns what is requested |
| **REQUEST_3.sql** | 1      | The query correctly returns what is requested |
| **REQUEST_4.sql** | 1      | The query correctly returns what is requested |
| **REQUEST_5.sql** | 1      | The query correctly returns what is requested |
| **Total**         | **5**  |                                               |
