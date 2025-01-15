import os
def menu():
    print("1. Add new book")
    print("2. search book")
    print("3. view book")
    print("4. Delete Book")
    print("5. Borrow Book")
    print("6. Exit")


# This module is used for interacting with the operating system, specifically to check if files exist (os.path.exists).


def add_new_book(filename):
    try:
        with open(filename, 'a') as file:
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            pub_year=input("Enter the pub_year of the book: ")
            book=f'{title},{author},{pub_year}\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error occurred: {e}')        



# Adds a new book to the inventory:
# Opens the file in append mode ('a').
# Accepts the book details from the user: title, author, and publication year.
# Writes the details to the file in CSV format (comma-separated values).
# Prints a success message.



def search_book(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                search=input("Enter the book name: ") 
                with open(filename,"r") as file:
                    books=file.readlines()  
                    found=False
                    for book in books:
                        title,author,pub_year=book.strip().split(",")
                        if title==search:
                            print("found book below")
                            print(f"title-{title}")
                            print(f"Author-{author}")
                            print(f"Pub_year-{pub_year}")
                            found=True
                            break
                    if not found:
                        print("Book not found")    
        else:
            print("Inventory not found")    
    except Exception as e:
        print(f"An Error occurred: {e}")



# Searches for a book in the inventory:
# Checks if the file exists.
# Reads all lines from the file.
# Iterates through each line, splitting it into title, author, and year.
# Compares the entered title with the title from the file.
# Displays the book details if found; otherwise, indicates that the book is not in the inventory.



def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open (filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                        title,author,pub_year=book.strip().split(",")
                        print(f'Title: {title},Author: {author},Pub_year: {pub_year}')
                else:
                    print("Inventory is empty")
        else:
            print("Inventory not found")
    except Exception as e:
        print(f"An Error occurred: {e}")


# Displays all the books in the inventory:
# Checks if the file exists.
# Reads all lines and prints the details of each book.
# If the file is empty, informs the user.




def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the book name: ")
            with open(filename,"r") as file:
                books=file.readlines()
            with open(filename,"w") as file:
                found=False
                for book in books:
                        title,author,pub_year=book.strip().split(",")
                        if title==title1:
                            print(f"Delete-{title},{author},{pub_year}")
                            found==True
                        else:
                            file.write(book)
            if not found:
                print("Book not found")
            else:
                print("Inventory not found")
    except Exception as e:
        print(f"An Error occurred: {e}")


# # Deletes a book from the inventory:
# Reads all books from the file.
# Rewrites all books except the one to be deleted.
# Indicates success or failure to find the book.



def borrow_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the book name: ")
            with open(filename,"r") as file:
                books=file.readlines()
            with open(filename,"w") as file:
                found=False
                for book in books:
                        title,author,pub_year=book.strip().split(",")
                        if title==title1:
                            print(f"Borrow-{title},{author},{pub_year}")

                            found==True
                        else:
                            file.write(book)
            if not found:
                print("Book not borrow")
            else:
                print("Book found")
    except Exception as e:
        print(f"An Error occurred: {e}")
def main():
    filename="books.txt"
    while True:
        menu()
        choice=(input("Enter your choice: "))
        if choice=="1":
            add_new_book(filename)
        elif choice=="2":
            search_book(filename)
        elif choice=="3":
            view_inventory(filename)
        elif choice=="4":
            delete_book(filename)
        elif choice=="5":
            borrow_book(filename)
            break
        else:
            print("Invalid choice")


if __name__== "__main__":
 main()