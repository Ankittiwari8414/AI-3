"""
import os
def menu():
    print("NSTI Book Store")
    print("1. Add a Book:")
    print("2. View books:")
    print("3. search for book:")
    print("4. Delete the book")
    print("5. Exit")

    #add a new book

def add_new_book(filename):
    try:
        with open (filename,"a") as file:
            title=input("Enter the book title:")
            author=input("Enter the author:")
            price=input("Enter the price: ")
            book=f'{title},{author},{price}\n'
            file.write(book)
            print("Book added successfully.")
    except Exception as e:
        print(f'An Error Occurred:{e}')

def view_inventory(filename):
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                books=file.readlines()
                if books:
                    print("Inventory:")
                    for book in books:
                        title,author,price = book.strip().split(',')
                        print(f'Title: {title},Auhtor is: {author}, Price: {price}')
                else:
                    print("The inventory is empty.")
        else:
            print("Inventory file does not exits.")
    except Exception as e:
        print(f"An error occurred : {e}")

def search_book(filename):
    try:
        if os.path.exists(filename):
            search=input("Enter the book name :")
            with open (filename,"r") as file:
                books=file.readlines()
                found=False
                for book in books:
                    title,author,price=book.strip().split(',')
                    if title==search:
                        print("Book found below:")
                        print(f"Title-{title}")
                        print(f"Author-{author}")
                        print(f"price-{price}")
                        found=True
                        break
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_book(filename):
    try:
        if os.path.exists(filename):
            title1=input("Enter the book name :").lower()
            with open(filename,"r") as file:
                books=file.readlines()
                found=False
                with open(filename,"w") as file:
                    for book in books:
                        title, author, price = book.strip().split(',')
                        if title==title1:
                            print(f"Deleted -{title},{author},{price}")
                            found = True
                        else:
                            file.write(book)
                if not found:
                    print("Book not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main ():
    filename="Ankit.txt"
    while True:
        menu()
        choice=input("Enter you choice :")
        if choice =="1":
            add_new_book(filename)
        elif choice=="2":
            view_inventory(filename)
        elif choice=="3":
            search_book(filename)
        elif choice=="4":
            delete_book(filename)
            print("Exiting the code:")
            break
        else:
            print("Invalid choice.")

if __name__=="__main__":
    main()
"""