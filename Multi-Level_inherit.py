###################################### DATE_ 31/12/2024  ########################################################

# class NSTI:
#     def __init__(self,Institute_name,Branch):
#         self.Institute_name=Institute_name
#         self.Branch=Branch

# class Trade(NSTI):
#     def __init__(self, Institute_name, Branch,Trade):
#         super().__init__(Institute_name, Branch)
#         self.Trade=Trade

# class Student(Trade):
#     def __init__(self, Institute_name, Branch, Trade,Student):
#         super().__init__(Institute_name, Branch, Trade)
#         self.Student=Student

#     def disp(self):
#         print(f'Institute Name : {self.Institute_name}')
#         print(f'Branch Name : {self.Branch}')
#         print(f'Trade : {self.Trade}')
#         print(f'Student Name : {self.Student}')


# x=Student("NSTI","Ramanthapur","Artifical Intelligence","Ankit")

# x.disp()


# class LIBRARY:
#     def __init__(self,library_name,Branch):
#         self.library_name=library_name
#         self.Branch=Branch

# class AUTHOR(LIBRARY):
#     def __init__(self, library_name, Branch,Author_name):
#         super().__init__(library_name, Branch)
#         self.Author_name=Author_name

# class PUBLICATION(AUTHOR):
#     def __init__(self, library_name, Branch, Author_name,Publication_name):
#         super().__init__(library_name, Branch, Author_name)
#         self.Publication_name=Publication_name

# class PRICE(PUBLICATION):
#     def __init__(self, library_name, Branch, Author_name, Publication_name,Price_of_book):
#         super().__init__(library_name, Branch, Author_name, Publication_name)
#         self.Price_of_book=Price_of_book


#     def disp(self):
#         print(f'LIBRARY NAME : {self.library_name}')
#         print(f'BRANCH : {self.Branch}')
#         print(f"AUTHOR'S NAME : {self.Author_name}")
#         print(f'PUBLICATION NAME : {self.Publication_name}')
#         print(f'PRICE OF BOOK : {self.Price_of_book}')


# x=PRICE("AMAR PUSTAK BANDAR","RAMANTHAPUR","BEN JHONSON","IGI GLOBAL",2500)
# x.disp()


# Task - 1
# Build a program with the following structure:

# Class Animal has a method eat() and an attribute species.
# Class Mammal inherits from Animal and adds attributes like has_hair and methods like walk().
# Class Dog inherits from Mammal and adds specific attributes like breed and methods like bark().
# Write a program to create a Dog object and demonstrate all the inherited methods.    


# class Animal:
#     def __init__(self,species):
#         self.species=species

#     def eat(self):
#         print("This Animal eats food.")

# class Mammal(Animal):
#     def __init__(self, species,has_hair):
#         super().__init__(species)
#         self.has_hair=has_hair

#     def walk(self):
#         print("This Mammal walk.")

# class Dog(Mammal):
#     def __init__(self, species, has_hair,breed):
#         super().__init__(species, has_hair)
#         self.breed=breed

#     def bark(self):
#         print("The Dog barks : woof! woof !")

# dog= Dog(species="American Labrador",has_hair="Yes",breed="Labrador Retriever")

# print(f'species :{dog.species}')
# print(f'has _hair : {dog.has_hair}')
# print(f'Breed : {dog.breed}')


# Task-2 :
# Create a multilevel inheritance:

# Class Vehicle has attributes like brand and model.
# Class Car inherits from Vehicle and adds attributes like number_of_doors and fuel_type.
# Class ElectricCar inherits from Car and adds attributes like battery_capacity and range.
# Write methods to display the details of an ElectricCar.                           


# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# class Car(Vehicle):
#     def __init__(self, brand, model,numbers_of_door,fuel_type):
#         super().__init__(brand, model)
#         self.number_of_door=numbers_of_door
#         self.fuel_type=fuel_type

# class ElectriCar(Car):
#     def __init__(self, brand, model, numbers_of_door, fuel_type,battery_capacity,range):
#         super().__init__(brand, model, numbers_of_door, fuel_type)
#         self.battery_capacity=battery_capacity
#         self.range=range

#     def disp(self):
#         print(f'Brand of Car: {self.brand}')
#         print(f'Model of Car: {self.model}')
#         print(f'Number of Doors In Car: {self.number_of_door}')
#         print(f'Fuel Type: {self.fuel_type}')
#         print(f'Battery Capacity: {self.battery_capacity}')
#         print(f'Range: {self.range}')

# x=ElectriCar("TATA","NANO","FIVE","PETROL","9volt","20km/pr litre")
# x.disp()


# Task -3 :Design a library management system using multilevel inheritance:

# Class Library has attributes library_name and location.
# Class Book inherits from Library and includes attributes like book_name, author, and ISBN.
# Class Borrower inherits from Book and adds attributes like borrower_name and borrow_date.
# Write a program to manage borrowers and display their borrowed book details, including library information.     


# class LIBRARY:
#     def __init__(self,library_name,location):
#         self.library_name=library_name
#         self.location=location

# class Book(LIBRARY):
#     def __init__(self, library_name, location,book_name,author,publication_year):
#         super().__init__(library_name, location)
#         self.book_name=book_name
#         self.author=author
#         self.publication_year=publication_year

# class Borrower(Book):
#     def __init__(self, library_name, location, book_name, author, publication_year,borrower_name,borrow_date):
#         super().__init__(library_name, location, book_name, author, publication_year)
#         self.borrower_name=borrower_name
#         self.borrow_date=borrow_date
    
#     def display_borrower_details(self):
#         print(f'LIBRARY NAME : {self.library_name}')
#         print(f'LOCATION : {self.location}')
#         print(f'BOOK NAME : {self.book_name}')
#         print(f'AUTHOR : {self.author}')
#         print(f'PUblication year : {self.publication_year}')
#         print(f'BORROWER NAME : {self.borrower_name}')
#         print(f'BORROW DATE : {self.borrow_date}')

# borrower=Borrower(library_name="DEEPAK PUSTAK BHANDAR",location="BIHAR",book_name=" DO YOU LOVE ME",author="JOHNSON GALB",publication_year="2013",borrower_name="KUMAR ADITYA",borrow_date="31/12/2024")

# borrower.display_borrower_details()