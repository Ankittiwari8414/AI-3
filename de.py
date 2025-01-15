#Define a class Student with attributes name and roll_number. Create an object of this class and print its attributes.

class Student:
    def __init(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number

student1 = Student("Aarav", 10)
student2 = Student("Kumar Aditya", 11)

print(f"Name: {student1.name}, {student1.roll_number}")
print(f"Name: {student2.name}, {student2.roll_number}")