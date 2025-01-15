# try:
#     result=10/0
# except ZeroDivisionError:
#     print("Number can't be divisible by zero")

# result=10/2
# print(result)

# try:
#     res=10/2
# except ZeroDivisionError:
#     print("you can't divide a number by zero")
# else:
#     print("The result is :",res)
# finally:
#     print("it will print regardless of whether the issue is raised or not")


# def check_age(age):
#     if age <18:
#         raise ValueError("age must be 18")
#     return "you are allowed to vote "
# try:
#     result=check_age(11)
#     print(result)
# except ValueError as ve:
#     print(ve)
        

# try:
#     num=int(input("Enter a number:"))
#     result=10/num
# except  ValueError:
#     print("Invalid Input")
# except ZeroDivisionError:
#     print("you can't  divide by zero")
# else:
#     print(result)
# finally:
#     print(" you are done.")

