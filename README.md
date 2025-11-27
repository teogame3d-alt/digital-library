# Digital Library

A Python console application simulating a personal library. 
Users can add books, borrow/return them, search, and save/load library data in JSON format.

**Important:** The library data is stored in `library_data.json`. Before loading data, you should first add books and save them to JSON. Loading before saving will start with an empty library.

## Features

1. Display all books
2. Display books sorted by publication year
3. Add a new book (title, author, year, category)
4. Search books by author
5. Search books by publication year
6. Borrow a book
7. Return a book
8. Display library report (total books, available, borrowed, borrow history)
9. Save library data to `library_data.json`
10. Load library data from `library_data.json`
0. Exit

## Usage

Run the program using Python 3:

```bash
python digital_library.py
Follow the menu and use the options in order:

Add books – before you can borrow or save anything, you need to add some books.

Save library to JSON – saves the current state to library_data.json.

Load library from JSON – reloads the saved library state; if the file doesn't exist, an empty library is used.

Example workflow:

Add books → Save to JSON → Exit → Restart → Load from JSON → Continue borrowing/returning.

File
library_data.json – stores the library books in JSON format. You can modify this file externally, but it's recommended to use the program's interface to maintain consistency.

License
This project is licensed under the MIT License.

yaml
Copiază codul

---

 Avantaje:

- Explică clar fluxul corect de utilizare.  
- Structurat profesional pentru portofoliu.  
- Evidențiază fișierul JSON și modul de manipulare.  
- Include exemple și instrucțiuni de rulare.  

Dacă vrei, pot să fac și o **versiune cu secțiune „Demo”** care arată concret ce afișează programul la rulare, ca să fie și mai atractiv pentru recrutor/portofoliu. Vrei să fac asta?
