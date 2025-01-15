"""    Abstraction in python   """         #Date - 24/12/2024
# first we'll have to import module from the Abstract Base class Libaray.

# from abc import ABC, abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Bike(vehicle):
#     def start(self):
#         print("Hello KTM kaushik ")
    
#     def stop(self):
#         print("Goodbye Vamshi ")

# x=Bike()

# x.start()
# x.stop()

"""  Example-1  """

# from abc import ABC, abstractmethod

# class Computer(ABC):
#     @abstractmethod
#     def start(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class Cpu(Computer):
#     def start(self):
#         print("your computer was on now")

#     def stop(self):
#         print("your computer is shut down")

# x=Cpu()

# x.start()
# x.stop()

"""    Example-2     """

# from abc import ABC, abstractmethod

# class facebook(ABC):
#     @abstractmethod
#     def login(self):
#         pass

#     @abstractmethod
#     def scroll(self):
#         pass

#     @abstractmethod
#     def logout(self):
#         pass

# class account(facebook):
#     def login(self):
#         print("Your are successfully login your account")

#     def scroll(self):
#         print("Scroll down to see more content on facebook")

#     def logout(self):
#         print("you successfully logout your account ")

# x=account()
# x.login()
# x.scroll()
# x.logout()


# from abc import ABC,abstractmethod

# class math(ABC):
#     @abstractmethod
#     def Area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class square(math):
#     def __init__(self,side):


"""  ......................BANKING SYSTEM.......................... """

# from abc import ABC, abstractmethod

# class Banking(ABC):
#     @abstractmethod
#     def deposit(self):
#         pass

#     @abstractmethod
#     def withdraw(self):
#         pass
    
#     @abstractmethod
#     def check(self):
#         pass

# class Saving_account(Banking):
#     def __init__(self,deposit,withdraw,check):
#         self.deposit=deposit
#         self.withdraw=withdraw
#         self.check=check

#     def deposit(self):
#         self.deposit=
#         if DEPOSIT >0:
#             print("YOUR MONEY DEPOSIT SUCCESSFULLY")
#         else:
#             print("DEPOSIT AMOUNT MUST BE IN POSITIVE")

#     def withdraw(self,withdraw):
