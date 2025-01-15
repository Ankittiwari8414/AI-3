#-------------------- for small  letter ------------------------------

# import re

# xyz=r'[a-z]'
# text="wikipedia is a free online encyclopedia, created and edited by volunteers around the world and hosted by the Wikimedia Foundation"

# match=re.findall(xyz,text)

# print(match)


# ----------------------for upper letter-----------------------------

# import re

# abc=r'[A-Z]'

# text="THE SUN IS FAR FROM EARTH ALMOST 1.5BILLION KM IS DISTANCE BETWEEN SUN AND EARTH"

# match=re.findall(abc,text)

# print(match)

#---------------------------------for Numberic letter------------------------------------

# import re
 
# abd=r'[0-9]'

# text="total hotel in this area is 24 "

# match=re.findall(abd,text)

# print(match)

# ------------------------for print space btw words----------------------------------------

# import re

# xyz=r'[^abcde]'

# text= "total trade in nsti ramnathapur is 6"

# match=re.findall(xyz,text)

# print(match)


#---------------------------for print without space btw words-------------------------------

# import re
# abd=r'[^LISPL ]'

# text="LIFE IS SIMPLE BUT YOU HAVE FACE SOME HARD TIME AS WELL AS"

# match=re.findall(abd,text)

# print(match)


#----------------------------for print only space in text ----------------------------------

# import re

# abc=r'\s'

# text="hello b hai kaie ho"

# up=re.findall(abc,text)

# print(up)


#--------------------------for print only letter without space-----------------------------


# import re

# list=r'\S'

# text="there is a lot of students in ai trade"

# later=re.findall(list,text)

# print(later)


#---------------------------for print all word and number get find--------------------------

# import re

# op=r'\w'

# text="There is 124 students in this nsti"

# up=re.findall(op,text)

# print(up)

#-------------------------for find the character of word-------------------------------------


# import re

# op=r'\w(2)'

# text="There is 124 students in this nsti"

# up=re.findall(op,text)

# print(up)


#---------------------------- for find how many name in text  and print ----------------------

# import re

# xyz=r'name'

# text="my name is Ankit "

# match=re.findall(xyz,text)

# print(match)



#----------------------------


# import re

# op=r'xyz?'

# text="xyz xyyz xyzz"

# up=re.findall(op,text)

# print(up)

# --------match is used for the first word or beginning of the string.-------

# import re

# xyz=r'My'

# x='My name is Ankit'

# match=re.match(xyz,x)

# if match:
#     print("Match found :",match.group())

# else:
#     print("NO match found")

#    search is used to check the entire string.


# import re

# xyz=r'Ankit'

# x='My name is Ankit'

# match=re.search(xyz,x)

# if match:
#     print("Match found :",match.group())

# else:
#     print("NO match found")



#    sub patter for the replacement

# xyz=r'srija'

# rep='Shailesh'

# x='srija  sir is the trainer in Nsti'

# z=re.sub(xyz,rep,x)

# print(z)

#      spiltting the string of the pattern

# import re
# xyz=r'\d+'

# x='difhlg8387648rgjn895yhhty5'
# z=re.split(xyz,x)
# num=re.findall(xyz,x)
# print('numbers : ',num)
# print('sring :',z)




# Validations using RegEx

# import re 

# mob="+91-6202889283"
# xyz=r'^\+?\d{1,2}[-\s]?\d{10}?$'

# if re.match(xyz,mob):
#    print("valid no. :",mob)

# else:
#    print("Invalid no. :",mob)





# import re

# x="Ankittiwari8414@gmail.com"

# xyz=r'^[A-Za-z0-9]+@[a-z]+.[a-z]{1,3}$'


# if re.match(xyz,x):
#    print("valid Email  :",x)

# else:
#    print("Invalid Email :",x)




# import re

# x="Ankittiwari8414!@gmail.com"

# xyz=r'^[A-Za-z0-9*!#$%&]+@[a-z]+.[a-z]{1,3}$'


# if re.match(xyz,x):
#    print("valid Email  :",x)

# else:
#    print("Invalid Email :",x)



#----------------------------- Password Validation------------------------------------------
# import re

# password="Ankit76@"

# xyz=r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$&*])(A-Za-z\d@$#!*&){10,}'

# if re.match(xyz,password):
#     print("Strong Password",password)

# else:
#     print("Week Password :",password)

#########################################################################################################################################################################################################################

#                                                                              TASK DATE - 08 JAN 2025

# Task - 1: 
# Validate Multiple Email Formats: Write a regex pattern to validate email addresses that:

# Start with an uppercase letter.

# Contain numbers, special characters, and lowercase letters.

# Have a domain that includes a hyphen 

# Modify the email validation regex to allow complex domain names (e.g., example@sub.domain.co.uk).

# import re

# email="Ankit62_02@"
# Task - 2:
# Write a regex pattern to validate Indian mobile numbers that start with 7, 8, or 9 and are followed by exactly 9 digits.

# Write a regex pattern to match a phone number that may or may not have a country code prefix (e.g., "+91-1234567890" or "1234567890"

# import re

# x=r'^[789]\d{9}$'  # for without country code.

# y=r'^(\+91[-\s]?)?[789]\d{9}$'

# if re.match()break


##########################################################################################################################################################################################################################
                                                                                   
   #                                                                                TASK DATE - 07 jan 2025


# Task - 1:
#  Write a regex pattern to find all occurrences of 2 to 4 digit numbers in the string "123 4567 89 01234". 
# Use re.findall to extract the matches.

# import re

# xyz=r'\b\d{2,4}\b'

# digit_numbers="123 4567 89 01234"

# match=re.findall(xyz,digit_numbers)

# print(match)

# Task - 2: 
# Write a regex pattern to find all words with exactly 4 characters in the string "This is a test of the regex function.
# " Use re.findall to get the matches.

# import re

# xyz=r'\b\w{4}\b'

# string="This is a test of the regex function."


# match=re.findall(xyz,string)
# print(match)

# Task - 3:
#  Write a regex pattern to find all occurrences of the word "pen" in the string "I have an pen, and you have an pen too.
# " Use re.findall to get the matches

# import re

# xyz=r'pen'

# string="I have an pen, and you have an pen too."

# match=re.findall(xyz,string)

# print(match)




# \w: Matches word characters (letters, digits, and underscore).
# \W: Matches non-word characters.
# \A: Matches the start of the string.
# \Z: Matches the end of the string.
# \z: Matches the end of the string, including trailing newline characters.




# \D: Matches non-digits.

# import re

# pattern = r'\D'
# text = "There are 123 students in this class."

# matches = re.findall(pattern, text)
# print(matches)

# \d: Matches digits (0-9).

# import re

# pattern = r'\d'
# text = "There are 123354678 students in this class."

# matches = re.findall(pattern, text)
# print(matches)

# \b: Matches word boundarie.

# import re

# pattern = r'\bword\b'
# text = "This is a word in a sentence. Anotherword is here."

# matches = re.findall(pattern, text)
# print(matches)

# \B: Matches non-word boundaries.

# import re

# pattern = r'\Bword\B'
# text = "This is awordb test of the aadityawordwn regex function."

# matches = re.findall(pattern, text)
# print(matches)

# \s: Matches whitespace characters.

# import re

# pattern=r'\s'

# text="This is your phone"

# match=re.findall(pattern,text)

# print(match)

#  \S: Matches non-whitespace characters.

# import re

# pattern=r'\S'

# text="This is your phone"

# match=re.findall(pattern,text)

# print(match)