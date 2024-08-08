Sure, here’s the README without any links to resources:

---

# MySQL Advanced Project

## Overview

This project demonstrates advanced SQL concepts and techniques using MySQL. It covers a range of topics such as creating tables with constraints, optimizing queries with indexes, implementing stored procedures and functions, utilizing views, and working with triggers.

### Project Duration
- **Start Date:** June 11, 2024
- **End Date:** June 14, 2024

### Technologies Used
- **Database:** MySQL 5.7 (version 5.7.30)
- **Operating System:** Ubuntu 18.04 LTS

## Table of Contents

- [MySQL Advanced Project](#mysql-advanced-project)
	- [Overview](#overview)
		- [Project Duration](#project-duration)
		- [Technologies Used](#technologies-used)
	- [Table of Contents](#table-of-contents)
	- [Concepts Covered](#concepts-covered)
	- [Requirements](#requirements)
	- [Installation and Setup](#installation-and-setup)
	- [Tasks Overview](#tasks-overview)
		- [Task 0: We are all unique!](#task-0-we-are-all-unique)
		- [Task 1: In and not out](#task-1-in-and-not-out)
		- [Task 2: Best band ever!](#task-2-best-band-ever)
		- [Task 3: Old school band](#task-3-old-school-band)
		- [Task 4: Buy buy buy](#task-4-buy-buy-buy)
		- [Task 5: Email validation to sent](#task-5-email-validation-to-sent)
		- [Task 6: Add bonus](#task-6-add-bonus)
		- [Task 7: Average score](#task-7-average-score)
	- [Usage](#usage)
	- [Credits](#credits)

## Concepts Covered

- **Advanced SQL**
  - Creating tables with constraints
  - Optimizing queries using indexes
  - Implementing stored procedures and functions
  - Working with views and triggers
  - Managing data with SQL scripts

## Requirements

- All scripts are written in SQL and are executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- Each SQL script must:
  - End with a new line
  - Start with a comment describing the task
  - Use uppercase for all SQL keywords (e.g., `SELECT`, `WHERE`)
- A `README.md` file is required at the root of the project directory.

## Installation and Setup

To run this project:

1. Start a MySQL service on Ubuntu 18.04:
    ```bash
    $ service mysql start
    ```
2. Connect to MySQL using the provided credentials:
    ```bash
    $ mysql -uroot -p
    ```
3. Import the provided SQL dump files (where applicable) into your MySQL database.

## Tasks Overview

### Task 0: We are all unique!
- **File:** `0-uniq_users.sql`
- **Description:** Creates a `users` table with a unique `email` attribute to enforce business rules and avoid application bugs.

### Task 1: In and not out
- **File:** `1-country_users.sql`
- **Description:** Creates a `users` table with an additional `country` attribute using an enumeration type. The default value is set to `US`.

### Task 2: Best band ever!
- **File:** `2-fans.sql`
- **Description:** Ranks the country origins of bands, ordered by the number of non-unique fans.

### Task 3: Old school band
- **File:** `3-glam_rock.sql`
- **Description:** Lists all bands with `Glam rock` as their main style, ranked by their longevity.

### Task 4: Buy buy buy
- **File:** `4-store.sql`
- **Description:** Creates a trigger that decreases the quantity of an item after adding a new order.

### Task 5: Email validation to sent
- **File:** `5-valid_email.sql`
- **Description:** Creates a trigger that resets the `valid_email` attribute only when the email has been changed.

### Task 6: Add bonus
- **File:** `6-bonus.sql`
- **Description:** Creates a stored procedure `AddBonus` to add a new correction for a student. This procedure handles both existing and new projects.

### Task 7: Average score
- **File:** `7-average_score.sql`
- **Description:** Creates a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.

## Usage

To execute a specific SQL script, use the following command:

```bash
$ cat <script_name>.sql | mysql -uroot -p <database_name>
```

Replace `<script_name>` with the name of the SQL script file and `<database_name>` with the name of your database.

## Credits

This project is part of the curriculum for ALX's backend storage module. It was developed with guidance from the provided resources and course materials.
