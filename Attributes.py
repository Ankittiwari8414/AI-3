# Task 1: Define a class Student with attributes name and roll_number. Create an object of this class and print its attributes.

# class Student:
#     def __init__ (self,name,roll_number):
#         self.name=name
#         self.roll_number=roll_number
    
# student1 =Student("ankit",26)
# student2 = Student("sahil",28)
    
# print(f"Name:{student1.name},{student1.roll_number}")
# print(f"Name:{student2.name},{student2.roll_number}")

# Task 2: Define a class Rectangle with attributes length and width. Add a method area to calculate the area of the rectangle. Create an object and call the method.

# class Rectangle:
#     def __init__ (self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width

# rect = Rectangle(12, 3)
# print(f"The area of the rectangle is: {rect.area()}")  

# Task 3: Define a class Circle with a method circumference to calculate the circumference and another method area to calculate the area. Use π = 3.14.

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def circumference(self):
#         return 2 * 3.14 * self.radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    
# circle = Circle(121)
# print(f"The circumference of the circle is: {circle.circumference()}")
# print(f"The area of the circle is: {circle.area()}") 
    
# Task 4: Define a class Employee with a class attribute company_name and instance attributes name and salary. Print both class and instance attributes.

class Employee:
    company_name = "AirIndia"  

    def __init__(self, name, salary):
        self.name = name  
        self.salary = salary  
emp = Employee("Ankit", 250000)
print(f"Company: {Employee.company_name}") 
print(f"Employee Name: {emp.name}")        
print(f"Salary: {emp.salary}")

# Task 5: Create a base class Animal with a method sound. Create a derived class Dog that overrides the sound method. Call the method from an object of Dog.

# class Animal:



# Task 6: Create a class Book with attributes title and author. Add a method is_same_author that compares the authors of two book objects.