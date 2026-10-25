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

## Refinement Notes

This project was reviewed and refined before publication to improve code organisation, reliability, maintainability, and readiness for a public portfolio.

### Changes made

- **Code organisation:** Created `catalogue_app.py` as the main application module, separating the application code from the test suite.
- **Input validation:** Added or retained validation for book titles, authors, copy counts, and user objects to prevent invalid data from being accepted in common scenarios.
- **Catalogue management:** Implemented case-insensitive duplicate detection for books based on title and author, alongside copy-management and search functionality.
- **User management:** Refined user registration and lookup behaviour, including case-insensitive username matching and duplicate-user prevention.
- **Loan management:** Added and tested borrowing and returning workflows, including availability updates, due dates, and overdue-loan checks.
- **Automated testing:** Created a dedicated `unittest` test suite covering the core catalogue, user, and loan-management behaviours.
- **Privacy and repository hygiene:** Excluded original coursework files, local backups, generated Python cache files, and environment-specific files from the published repository.
- **Project documentation:** Added setup instructions, a description of the project structure, and the command required to run the tests.

### Verification

The automated test suite passed all 19 tests using:

```bash
python3 -m unittest -v test_library.py
```

### Current limitations

- The application stores data in memory; records are not persisted between program runs.
- The project does not currently include a web interface or database integration.
- The test suite covers the implemented core behaviours, but does not represent exhaustive testing of every possible input or edge case.

### Purpose of the refinement

The aim was to turn a coursework codebase into a clearer, testable, and documented portfolio project while preserving its core object-oriented design.

