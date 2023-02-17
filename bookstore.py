#import sqlite
import sqlite3

#import tabulate
import tabulate


#define the add_book function
def add_book(identity, title, author, quantity, db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Insert a new row into the books table
    c.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)",
              (identity, title, author, quantity))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

#define the update_book function
def update_book(identity, table_header, new_value, db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Update the specified row in the books table
    c.execute(f"UPDATE books SET {table_header} = ? WHERE id = ?", (new_value, identity))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

#define the delete_book function
def delete_book(identity, db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Delete the specified row from the books table
    c.execute("DELETE FROM books WHERE id = ?", (identity,))

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()


#define the search_book function
def search_book(identity, db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Search for the specified row in the books table
    c.execute("SELECT * FROM books WHERE id = ?", (identity,))
    book = c.fetchone()

    return book

    # Close the connection
    conn.close()


#define the show_all function
def show_all(db_file):
    # Connect to the database
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # Fetch all rows from the books table
    c.execute("SELECT * FROM books")
    rows = c.fetchall()

    # Print the results using tabulate
    headers = ['ID', 'Title', 'Author', 'Quantity']
    print(tabulate.tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    # Close the connection
    conn.close()

def main():
    # connect to the database
    conn = sqlite3.connect('ebookstore.db')

    # create a cursor object
    cursor = conn.cursor()

    #use a try-except block to prevent a table from being created more than once
    try:
        # create the books table
        cursor.execute('''CREATE TABLE books
                    (id INTEGER PRIMARY KEY, 
                        title TEXT,
                        author TEXT,
                        quantity INTEGER)''')

        # insert some data into the table
        cursor.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)", (3002, 'A Tale of Two Cities', 'Charles Dickens', 30))
        cursor.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)", (3003, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40))
        cursor.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)", (3004, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25))
        cursor.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)", (3005, 'The Lord of the Rings', 'J.R.R. Tolkien', 37))
        cursor.execute("INSERT INTO books (id, title, author, quantity) VALUES (?, ?, ?, ?)", (3006, 'Alice in Wonderland', 'Lewis Carroll', 12))

        # commit the changes
        conn.commit()

    #if the table already exists, move on
    except Exception:
        pass


    # close the connection
    conn.close()


    #menu
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Welcome to the Bookstore Database""")
    while True:
        print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

\tPlease make a choice.

    Menu:
    1 - Enter a new book into the database
    2 - Update a book in the database
    3 - Delete a book
    4 - Search for a book
    5 - See all books
    quit - exit
    
    """)
        option = input(": ").lower()

        #when the user chooses 1, as the user for the book details
        if option == "1":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("Adding a new book\n")
            print("First we need a few details.\n")
                
            while True:
                #make sure the user puts an integer for the ID
                try:
                    identity = int(input("Enter the id for the book: "))
                
                #if not an integer, throw an error
                except Exception as e:
                    print(f"\nError: {e}.")
                    print("Try again.\n")
                    continue

                #check if the key already exists
                book = search_book(identity, "ebookstore.db")

                #if ID unique, continue
                if book == None:
                    break

                #if the ID is already used, prompt again
                else:
                    print(f"\nError: ID {identity} already used by:\n")
                    print(f"Title:  \t{book[1]}")
                    print(f"Author: \t{book[2]}")
                    print(f"Quantity: \t{book[3]}\n")

            #ask the user for the title and author
            title = input("\nEnter the title of the book: " )
            author = input("Enter the author of the book: ")
            
            while True:
                #make sure the user inputs an integer for quantity
                try:
                    quantity = int(input("Enter the quantity: "))
                    break

                #if not an integer, throw an error
                except Exception as e:
                    print(f"\nError: {e}.")
                    print("Try again.\n")
            

            #call the add_book function
            print(f"\nAdding {title} to database.\n")
            add_book(identity, title, author, quantity, "ebookstore.db")

            #let the user know it worked
            print(f"{title} added successfully!")


        #if the user chooses 2, update a book
        elif option == "2":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("Update a book.\n")
            
            #use a loop to make sure the user can retry putting in an ID number
            while True:
                try:
                    #ask the user to input the ID of the book they are updating
                    identity = int(input("Enter the ID of the book you want to update: "))
                    break

                #if not an integer, throw an error
                except Exception as e:
                    print(f"\nError: {e}.")
                    print("Try again.\n")


            #check to see if book exists
            book = search_book(identity, "ebookstore.db")
            
            #if the book does not exist, ask if they would like to add it
            if book == None:
                print(f"\nThe book with ID {identity} does not appear in the database, would you like to add it? Y/N")
                while True:
                    add_choice = input(": ").lower()
                    if add_choice == "y": 

                        #get the rest of the data
                        title = input("\nEnter the title of the book: " )
                        author = input("Enter the author of the book: ")
                        while True:
                            
                            #check if the user inputs an integer
                            try:
                                quantity = int(input("Enter the quantity: "))
                                break

                            #if the user doesn't input it correctly, throw an error 
                            except Exception as e:
                                print(f"\nError: {e}.")
                                print("Try again.\n")
                                continue
                            
                        #call the add_book function
                        add_book(identity, title, author, quantity, "ebookstore.db")
                        
                            #let the user know that it has worked
                        print(f"\n{title} has been added to the database.")
                        break
                    
                    #if user chooses no, return to the menu
                    elif add_choice == "n":
                        print("\nGoing back to the menu.")
                        break

                    else:
                        print("\nYou have input an invalid choice, try again.\n")
                        print(f"Would you like to add a book with ID {identity} to the database?")
            else:

                #print the details of the book to be updated
                print(f"\nID: \t\t{book[0]}")
                print(f"Title:  \t{book[1]}")
                print(f"Author: \t{book[2]}")
                print(f"Quantity: \t{book[3]}\n")

                while True:
                    #allow the user to choose what they are updating
                    update_choice = input("\nChoose which option you want to update - \ntitle\nauthor\nquantity\n\n: ").lower()
                    
                    #ask the user for the new title or author
                    if update_choice == "title" or update_choice == "author":
                        new_value = input(f"\nEnter the new {update_choice}: ")
                    
                    #ask the user for a new quanity
                    if update_choice == "quantity":
                        while True:
                            try:
                                new_value = int(input(f"\nEnter the new {update_choice}: "))
                                break
                            
                            #if it isnt an integer, throw an error
                            except Exception as e:
                                print(f"\nError: {e}.")
                                print("Try again.")


                    #update the new data
                    if update_choice == "title" or update_choice == "author" or update_choice == "quantity":
                        
                        #update the database
                        update_book(identity, update_choice, new_value, "ebookstore.db")

                        #let the user know that it has been done
                        print("\nThe book has been updated. It is now: \n")
                        book = search_book(identity, "ebookstore.db")
                        print(f"\nID: \t\t{identity}")
                        print(f"Title:  \t{book[1]}")
                        print(f"Author: \t{book[2]}")
                        print(f"Quantity: \t{book[3]}")
                        break
                    else:
                        print("\nYou have not chosen a valid choice. Please try again.\n")
                    
                

        
        #if the user chooses 3, delete a book
        elif option == "3":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("Delete a book.")

            #initialise the try_again variable
            try_again = "y"

            while True:
                while True:
                    #ask the user to input the ID for the book
                    try:
                        identity = int(input("\nEnter the ID of the book you wish to delete: "))
                        break

                    #if they don't put in a number, throw an error
                    except Exception as e:
                        print(f"\nError: {e}")
                        print("Try again.")
        
                #check if the book exists
                book = search_book(identity, "ebookstore.db")

                #if the book doesnt exist, ask the user if they would like to try again
                if book == None:
                    print("\nBook does not exist.\n")
                    while True:
                        print("Would you like to try a different ID? Y/N")
                        try_again = input(": ").lower()
                        if try_again == "y":
                            break
                        elif try_again == "n":
                            break
                        else:
                            print("\nInvalid response.\n")
                            continue
                    
                    #if the user does not want to try again, return to the menu
                    if try_again == "n":
                        print("\nReturning to the menu.\n")
                        break
                
                #if the book exists, show it to the user
                else:
                    print("Here is the book you wish to delete: \n")
                    print(f"\nID: \t\t{identity}")
                    print(f"Title:  \t{book[1]}")
                    print(f"Author: \t{book[2]}")
                    print(f"Quantity: \t{book[3]}")
                    
                    #ask the user to confirm deletion
                    while True:    
                        print(f"\n\nDo you want to delete {book[1]}? Y/N")
                        delete_choice = input(":  ").lower()

                        #if yes, delete it
                        if delete_choice == "y":
                            delete_book(identity, "ebookstore.db")
                            print(f"\n{book[1]} by {book[2]} has been deleted.")
                            break

                        #if no, return to the menu
                        elif delete_choice == "n":
                            print("\nReturning to menu.")
                            break

                        #show an error if the user inputs invalid response
                        else:
                            print("\nYou have not entered a valid choice, try again.")
                            continue
                    break

        #if the user chooses 4, search for a book
        elif option == "4":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            while True:

                #ask the user to input the ID of the book
                try: 
                    identity = int(input("Enter the book ID: "))
                    break

                #if the ID is not an integer, throw an exception
                except Exception as e:
                    print(f"\nError: {e}")
                    print("Try again.\n")

            #check if the book exists
            book = search_book(identity, "ebookstore.db")
            
            #if the book exists, print the details
            if book:
                print(f"\nID: \t\t{identity}")
                print(f"Title:  \t{book[1]}")
                print(f"Author: \t{book[2]}")
                print(f"Quantity: \t{book[3]}")
            
            #if the book does not exist, ask the user if they want to add it
            else:
                while True:
                    print(f"\n{identity} is not in the database, would you like to add it? Y/N")
                    add_choice = input(": ").lower()

                    #if yes, add book
                    if add_choice == "y":

                        #get the rest of the data
                        title = input("\nEnter the title of the book: " )
                        author = input("Enter the author of the book: ")
                        while True: 
                            try:
                                quantity = int(input("Enter the quantity: "))
                                break

                            #if the user doesn't input it correctly, throw an error 
                            except Exception as e:
                                print(f"\nError: {e}.")
                                print("Try again.\n")
                            
                        #call the add_book function
                        add_book(identity, title, author, quantity, "ebookstore.db")
                        5
                        #let the user know that it has worked
                        print(f"\n{title} has been added to the database.")
                        break
                
                    #if the user says no, return to the menu
                    elif add_choice == "n":
                        break

                    #if the input is invalid, throw an error
                    else: 
                        print("\nYou have not input a correct choice, try again.\n")
        
        #if the user chooses 5, show all books in a table
        elif option == "5":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("Showing all books:\n")
            show_all("ebookstore.db")
        
        #if the user chooses quit, quit
        elif option == "quit":
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print("\nLogging off\n")
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            quit()

        #if the user inputs an incorrect choice, alert them
        else:
            print("\nYou have input an incorrect choice.")
            print("Try again.\n")

if __name__ == "__main__":
    main()