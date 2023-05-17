# Bookstore Database

This is a Python program that manages a bookstore database using SQLite. The program allows users to perform various operations such as adding a book, updating a book, deleting a book, searching for a book, and viewing all books in the database.

## Prerequisites

Before running the program, make sure you have the following installed:

- Python 3.x
- SQLite

## Getting Started

1. Clone the repository or download the code files.
2. Open a terminal or command prompt and navigate to the directory where the files are located.

## Setup

1. Open the `ebookstore.db` file with an SQLite database browser or run the following commands in the terminal or command prompt to create the database and populate it with sample data:

```bash
sqlite3 ebookstore.db
```

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    quantity INTEGER
);

INSERT INTO books (id, title, author, quantity) VALUES (3002, 'A Tale of Two Cities', 'Charles Dickens', 30);
INSERT INTO books (id, title, author, quantity) VALUES (3003, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40);
INSERT INTO books (id, title, author, quantity) VALUES (3004, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25);
INSERT INTO books (id, title, author, quantity) VALUES (3005, 'The Lord of the Rings', 'J.R.R. Tolkien', 37);
INSERT INTO books (id, title, author, quantity) VALUES (3006, 'Alice in Wonderland', 'Lewis Carroll', 12);
```

2. Save and exit the SQLite database browser or run the following command in the terminal or command prompt:

```bash
.quit
```

## Usage

Run the program by executing the following command in the terminal or command prompt:

```bash
python bookstore.py
```

The program will display a menu with the following options:

```
1 - Enter a new book into the database
2 - Update a book in the database
3 - Delete a book
4 - Search for a book
5 - See all books
quit - exit
```

Select an option by entering the corresponding number or type "quit" to exit the program.

### Adding a Book

To add a book to the database, choose option 1 from the menu. Enter the book's ID (must be unique), title, author, and quantity when prompted.

### Updating a Book

To update a book in the database, choose option 2 from the menu. Enter the ID of the book you want to update. Then, choose whether you want to update the title, author, or quantity. Enter the new value for the selected field.

### Deleting a Book

To delete a book from the database, choose option 3 from the menu. Enter the ID of the book you want to delete. Confirm the deletion when prompted.

### Searching for a Book

To search for a book in the database, choose option 4 from the menu. Enter the ID of the book you want to search for. The program will display the details of the book if it exists in the database.

### Viewing All Books

To see all books in the database, choose option 5 from the menu. The program will retrieve all the books and display them in a tabular format.

## Note

- The database file `ebookstore.db` is created automatically by the program if it doesn't exist.
- The `sqlite3` and `tabulate` modules are required to run the program. Make sure they are installed by running the following
