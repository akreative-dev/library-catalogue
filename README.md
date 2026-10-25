# Library Catalogue System

A Python-based library catalogue project developed as part of my
MSc Computer Science studies and refined for my software development portfolio.

## Overview

The project demonstrates object-oriented programming through a
library management model covering:

- **Books and catalogue management** — add, search, and remove books,
  manage copy counts, and check availability.
- **User management** — register users, search by username, and
  manage user records.
- **Loan management** — borrow and return books, track loan dates,
  calculate due dates, and identify overdue loans.
- **Automated testing** — validate core catalogue, user, and loan
  behaviours using Python's built-in `unittest` framework.

## Technologies

- Python
- Object-oriented programming
- `unittest`
- `datetime` and `uuid`

## Project structure

```text
Library-Catalogue-Portfolio/
├── catalogue_app.py
├── test_library.py
├── README.md
└── .gitignore
```

## Requirements

Python 3.10 or a compatible Python 3 version.

No third-party packages are required for the current implementation.

## Run the tests

From the project directory, run:

```bash
python3 -m unittest -v test_library.py
```

The current test suite contains 19 tests covering book catalogue
operations, user management, and borrowing and returning books.

## Notes

This portfolio version is a cleaned and tested version of a coursework
project. Original coursework copies and backup files are kept separately
from the public portfolio source.

The project currently models its data in memory; it does not provide
persistent database storage or a web interface.
