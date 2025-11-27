# Digital Library (Library_Project.py)

A Python console application for managing a personal library.  
Users can add books, search, borrow/return, and save/load library data in JSON format.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Example Output](#example-output)
6. [Project Structure](#project-structure)
7. [Important Notes](#important-notes)
8. [License](#license)
9. [Future Improvements](#future-improvements)
10. [Portfolio Value](#portfolio-value)

---

## Overview

Digital Library is a **Python console application** demonstrating object-oriented programming, file I/O, and interactive menu design. It allows users to manage a personal book collection efficiently.

---

## Features

- **Add new books** with title, author, publication year, and category
- **Display all books** or sort them by publication year
- **Search books** by author, category, or year
- **Borrow & return books** with status tracking
- **Library report** showing total books, available books, borrowed books, and total successful borrows
- **Save & load data** in JSON format (`library_data.json`) for persistent storage
- Editable JSON file for external modifications or pre-populated libraries

---

## Installation

1. Make sure you have **Python 3.9+** installed.
2. Clone this repository:
```bash
git clone https://github.com/teogame3d-alt/Library_Project.py.git
cd Library_Project.py
Usage
Run the application using Python:

bash
Copiază codul
python digital_library.py
Follow the interactive menu:

Display all books

Display books sorted by year

Add a book

Search by author

Search by publication year

Borrow a book

Return a book

Library report

Save library to JSON

Load library from JSON

Exit

Example Output
yaml
Copiază codul
Books in Central Library:
 - The Little Prince – Antoine de Saint-Exupéry – available
 - Ion – Liviu Rebreanu – borrowed
 - Baltagul – Mihail Sadoveanu – available

==== LIBRARY REPORT ====
Total books: 3
Available books: 2
Borrowed books: 1
Total successful borrows: 1
Project Structure
bash
Copiază codul
Library_Project.py/
├── digital_library.py      # Main Python script
├── library_data.json       # JSON file storing book data
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── .gitignore              # Git ignore rules
Important Notes
Add books and save them first before loading library data from JSON.

If you try to load without saved books, the library will start empty.

library_data.json is editable, allowing you to pre-populate the library or modify books manually.

License
This project is licensed under the MIT License – see LICENSE for details.

Future Improvements
GUI version for easier interaction

Categorization and filtering options

Multiple user profiles

Integration with online book databases

Portfolio Value
This project demonstrates:

Python OOP skills – classes, methods, and object management

File I/O & JSON handling – saving and loading persistent data

Interactive console applications – menus, input validation, and user experience

Project organization & documentation – ready for professional portfolio
