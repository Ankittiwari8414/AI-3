# class A:

#     def abc(self):
#         print("This is A")

# class B(A):
#     def xyz(self):
#         print("This is B")

# class C(A):
#     def apple(self):
#         print("This is C")

# class D(A):
#     def tu(self):
#         print("This is D")


# class E(B,C,D):
#     pass
# x=E()
# x.tu()
# x.abc()
# x.apple()



# class Company:

#     def __init__(self,name):
#         self.name=name

# class Model:
#     def __init__(self,model):
#         self.model=model

# class bike(Company,Model):

#     def __init__(self,name,model,launched):
#         Company.__init__(self,name)
#         Model.__init__(self,model)
#         self.launched=launched

#     def disp(self):
#         print(f'Name: {self.name} , Model: {self.model}, Launched in: {self.launched}')

# name=input("Enter the name of bike :")
# model=input("Enter the model of bike :")
# launched=input("Enter the launched year of a bike :")

# x=bike(name,model,launched)
# x.disp()

 ##########################################################################          DATE - 30 / 12/ 2024             ########################################################################################

"""
# Question 1: Create a Specialist class that inherits from two parent classes, Doctor and Surgeon.
#  The Doctor class should have a method diagnose that prints "Diagnosing the patient", and the Surgeon class should have a method operate that prints "Performing surgery". 
# The Specialist class should have a constructor that initializes the specialist's name and specialty, and a method display_info that prints the name and specialty.
"""

# class Doctor:

#     def __init__(self):
#         print("Diagnosing The Patient")

# class Surgeon:

#     def __init__(self):
#         print("performing surgery")


# class specialist(Doctor,Surgeon):

#     def __init__(self,name,specialty):
#         self.name=name
#         self.specialty=specialty

#     def display_info(self):
#         print(f'Name : {self.name}')
#         print(f'Specialty : {self.specialty}')

# name=input("ENTER THE DOCTOR NAME :")
# specialty=input("ENTER THE SPECIALTY OF DOCTOR :")

# x=specialist(name,specialty)
# x.display_info()



"""
# Question 2: Create an OnlineCourse class that inherits from two parent classes, CourseContent and InteractiveTools. 
# The CourseContent class should have a method provide_materials that prints "Providing course materials", 
# and the InteractiveTools class should have a method facilitate_interaction that prints "Facilitating student interaction with tools".
#  The OnlineCourse class should have a constructor that initializes the course name and a method display_info that prints the course name. 
# Additionally, write a method start_course that prints "Starting the course".
"""

# class CourseContent:
#     def provide_materials(self):

#         print("Providing Course Materials ")

# class InteractiveTools:
#     def facilitate_interaction(self):

#         print("Facilitating Student Interaction With Tools")

# class OnlineCourse(CourseContent,InteractiveTools):

#     def __init__(self,course_name):
#         self.course_name=course_name
    
#     def display_info(self):
#         print(f'CourseName : {self.course_name}')
    
#     def start_course(self):
#         print("Starting the course")

# x=OnlineCourse("investment in crypto")
# x.display_info()
# x.provide_materials()
# x.facilitate_interaction()

"""
Question 3: Create a Drone class that inherits from two parent classes, FlyingMechanism and Camera.
  The FlyingMechanism class should have a method fly that prints "Drone is flying", and the Camera class should have a method take_photo that prints "Taking a photo". 
 The Drone class should have a constructor that initializes the drone's model and a method display_info that prints the model.
  Additionally, write a method perform_actions that calls the methods from both parent classes.
"""


# class FlyingMechanism:
#     def fly(self):
#         print("Drone is flying")

# class Camera:
#     def take_photo(self):
#         print("Taking a Photo")

# class Drone(FlyingMechanism,Camera):
#     def __init__(self,drones_model):
#         self.drones_model=drones_model

#     def display_info(self):
#         print(f"Drone's Model :{self.drones_model}")

#     def perform_actions(self):
#         self.fly(),self.take_photo()

# x=Drone("DJI MINI 4 pro ")
# x.display_info()
# x.perform_actions()