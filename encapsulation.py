"""  a
# class AI:
#     def __init__(self):
#         self.name="Ankit"

#         def disp(self):
#             print(self.name)

# x=AI()
# # x.disp()
# print(x.name)            


# class NSTI:
#     def __init__(self):
#         self._trade="AI"

# class CTS(NSTI):
#     def disp(self):
#         print(self._trade)

# x=CTS()
# x.disp()
                         """

#  private 


# class Trainer:
#     def __init__ (self):
#         self.__salary="200"

#     def disp(self):
#         print(self.__salary)

#         return self.__salary

# x=Trainer()

# print(x.disp())



# Write a Python class with a public attribute name and a public method greet() that prints "Hello, [name]". Access both the attribute and method from outside the class.

# class meeting:
#     def __init__(self):
#         self.__name="HEllo, 'Anuj'"

#     def disp(self):
#         print(self.__name)

#         return self.__name
    
# x=meeting()

# print(x.disp())

#  Create a class with a protected attribute _age and a method _show_age() that prints the value of _age. Access these members directly from an object and observe the output.

# class protected:
#     def __init__(self):
#         self._age="21"

#     def _show_age(self):
#         print(self._age)

# x=protected()
# x._show_age()



# Create a class with a private method __secret(). Add a public method to call the private method, and demonstrate that the private method cannot be called directly from outside
#  the class.

# class private:
#     def __init__(self):
#         self.__name="Anuj"
    
#     def secret(self):
#         print(self.__name) 

# x=private()
# x.secret()
# x.__name()    you can't recall directly because its hidden in secret.



"""     real- world example      """
 
# class hospital:
#     def __init__(self):
#         self.__patients=[]

#     def add (self,patient):
#         self.__patients.append(patient)
#         print(f'patient {patient} added')

#     def remove(self,patient):
#         if patient in self.__patients:
#             self.__patients.remove(patient)
#             print(f' patient {patient} removed from list.')
#         else:
#             print(f'{patient} not found.')

#     def disp(self):
#         for patient in self.__patients:
#             print(patient)

# x=hospital()
# x.add("vamshi")
# x.add("aadil")
# x.add("anuj")
# x.remove("anuj")
# x.disp()

"""    real world example     """

# class Nsti:
#     def __init__(self):
#         self.__students=[]

#     def add(self,student):
#         self.__students.append(student)
#         print(f' student {student} added ')

#     def remove(self,student):
#         if student in self.__students:
#             self.__students.remove(student)
#             print(f' student {student} removed from list.')
        
#         else:
#             print(f'{student} was not found')


#     def dis(self):
#         for student in self.__students:
#             print(student)
# x=Nsti()
# x.add("Ankit")
# x.add("Aditya")
# x.add("Sakshi")
# x.remove("popt")
# x.dis()


"""           Lab- 52               """


# class BankAccount:
#     def __init__(self,account_number,holder_name,initial_balance):
#         self.__account_number=account_number
#         self.__holder_name=holder_name
#         self.__balance=initial_balance

#     def deposit(self,amount):
#         if amount>0:
#             self.__balance+=amount
#             print(f'deposited {amount} total balance is {self.__balance}.')
#         else:
#             print("deposit amount must be in positive.")

#     def withdraw(self,amount):
#         if 0<amount<=self.__balance:
#             self.__balance-=amount
#             print(f"withdraw {amount} . remaining balance is {self.__balance}")
#         else:
#             print("insufficient balance .")


#     def get_balance(self):
#         return self.__balance
    

#     def __str__ (self):
#         return (f"Account Number: {self.__account_number}\n"
#         f'Holder Name : {self.__holder_name}\n'
#         f"balance : {self.__balance}")

# account=BankAccount("20289029485341234","Ankit",49800)
# print(account)

# account.deposit(500)
# account.withdraw(4000)

# print(f"final balance : {account.get_balance()}")



"""  Date  - 24/12/2024   """


# class Movie:
#     def __init__(self,id,title,price):
#         self.id=id
#         self.__title=title
#         self.__price=price

#     def s_title(self,title):
#         self.__title=title


#     def t_price(self,price):
#         if price >0:
#             self__price=price
#         else:
#             print("Enter price more than 0.")
        
#     def g_title(self):
#         return self.__title

#     def g_ticket(self):
#         return  self.__price

#     def disp(self):
#         print(f'ID :{self.id}')
#         print(f'Name : {self.__title}')
#         print(f'Price : {self.__price}')

# def movie():
#         id=input("Enter id :")
#         title=input("Enter Movie name :")
#         while True:
#             price=float(input("Enter the price :"))
#             if 0<price<=999:
#                 break
#             else:
#                 print("Price must be 3 digits. ")
#         return Movie(id,title,price)

# x=movie()

# x.disp()


"""     TASK DATE - 24/12/2024     """

# Task 1 : Create a Book class to manage book information in a library. The class should have private attributes for the book title, author, and price. Implement getter and setter methods for each attribute and a function to create a Book instance with user input.

# class Book:

#     def __init__(self,title,author,price):
#        self.__title=title
#        self.__author=author
#        self.__price=price

#     def b_title(self,title):
#         self__title=title

#     def b_author(self,author):
#         self__author=author

#     def t_price(self,price):
#         if price >150:
#             self__price=price
#         else:
#             print("Enter price more than Rs.-150 .")
#     def dis(self):
#         print(f'Title: {self.__title}')
#         print(f' Author: {self.__author}')
#         print(f' price : {self.__price}')

# def libaray():
#         title=input("Enter the title of book :")
#         author=input("Enter the the author of book :")
#         while True:
#             price =float(input("Enter the price of book :"))
#             if 150<price:
#                 break
#             else:
#                 print("price must be rs.-150.")
#         return Book(title,author,price)

# x=libaray()
# x.dis()


# Task 2 : Create an Employee class to manage employee information. The class should have private attributes for the employee name, position, and salary. Implement getter and setter methods for each attribute and a function to create an Employee instance with user input.

class Employee:

    def __init__(self,name,position ,salary):
        self.__name=name
        self.__position=position
        self.__salary=salary

    def e_name(self,name):
        self.__name=name 

    def e_position(self,position):
        self.__position=position

    def e_salary(self,salary):
        if salary >15000:
            self__salary=salary
        else:
            print("salary must be 15000.")

    def dis(self):
        print(f'Empolyee Name :{self.__name}')
        print(f'Position of Employee :{self.__position}')
        print(f'salary :{self.__salary}')

def Company():
    name=input("Enter the name of employee :")
    position=input("Enter the position of employee :")
    while True:
        salary=float(input("Enter the salary of employee :"))
        if salary<15000 :
            break
        else:
            print("salary must be Rs. 15000.")
        return Employee(name,position,salary)
    
x=Company()
x.dis()
