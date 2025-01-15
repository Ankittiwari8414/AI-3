# file =open("Ankit.py","r")  (r use for read the content of file you mention)
# content=file.read()
# print(content)

# file = open ("new.py","r") (In this code file is open and shows the content of file
# content=file.read()           and close the file last code.)
# print(content)
# file.close()

# with open ("file.py","r") as file:
#     content=file.read()
#     print(content)

# with open("python.py","r") as file:
#     for line in file:                       (open python.py as file and show content by lines from file 
#         print(line.strip())                   we mention )


# with open("python.py","r") as file:          (In This code file open and read content by mention word where you 
#     content=file.read(13)                          want to read from)
# print(content)

# with open("python5dec.py","r") as file:
#     file.readline(13)
#     content=file.read(9)
#     print(content)

# with open ("python.py","w") as file:         (This is use for write something in file but all the       
#     file.write("hello, My name is Anki2t")   content of file will remove and print what you are want to write)

# with open ("python.py","a") as file:                (\n use for write a new line in the file where you 
#     file.write("\n tHIS IS ANOTHER NEW LINE.")        want to write after the previous line)

# with open ("python.py","r") as file:
#     file.read(32)
#     file.read(8)
#     file.seek(5)
#     print(file.read())
#     print(file.tell())
# try:
#     with open ("python.py","r") as file:\
#     print(file.read())
# except FileNotFoundError:                   ( try use because if file name was not matched than it shows error but
#     print("file is not available")            if you use try than it show file is not available.)
        
# with open ("python.pye","r") as file:     
#     print(file.read())

# try:
#     with open("python5dec.py","r") as file:
#         print(file.read())                    (In this code file was open if the file name was matched
# except FileNotFoundError:                     if not it shows file is not available and finally use for to show code run)
#     print("file is not available")
# finally:
#     print("code was excutive")


# import os
# if os.path.exists("python.py"):     (In this code we find file by name and remove from system by using remove.)
#     os.remove("python.py")
#     print("File is deleted")
# else:
#     print("File not found")
# file=open("python5dec.py","r")



# age=17
# if age>=18:
#     print("you are adult")
# else:
#     print("you ar minor")

# marks= int(input("ENter your marks: "))
# if marks>=90:
#     print("grade:a")
# elif marks>=75:
#     print("grade:b")
# elif marks>=60:
#     print("grade:c")
# else:
#     print("grade:d")
