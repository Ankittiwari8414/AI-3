# import os

# dir=("abc")
# try:
#     os.makedirs(dir)
#     print(f' Folder created :{dir}')
# except FileExistsError:
#     print(f"folder already exits.")
# finally:
#     print("Code is excuted ")

 
# cur_name="ADIT"
# new_name="AI"
# try:
#     os.rename(cur_name,new_name)
# except FileNotFoundError:
#     print(f"folder was not found ")
# finally:
#     print("code is excuted")

# import shutil

# dir_del="AI"
# try:
#     shutil.rmtree(dir_del)
#     print("Directory deleted")
# except FileNotFoundError:
#     print("Folder was not found")
# except PermissionError:
#     print("permission denied")
# except Exception as e:
#     print(f'An error Occurred: {e}')


# import os
# dir="AI"
# try:
#     os.makedirs(dir,exist_ok=True)
#     file_name="Ankit.txt"
#     file_path=os.path.join(dir,file_name)
#     with open(file_path,"w") as file:
#         file.write("hi ankit thiis is your file.")
#         print(f"file: '{file_name}'craeted successfully in {dir}'")
# except Exception as e:
#     print(f'An error Occurred: {e}')

# scan directory
# import os

# dir="."   # path of current directory

# with os.scandir(dir) as entries:  #scandir- scan the directory.
#     print(f"Content of the folder are :'{dir}'")
#     for entry in entries:
#         print(entry.name)


# list of directory.
# import os
# try:
#     dir=os.listdir()
#     print("Content in folder: ",dir)
# except Exception as e:
#     print(f"An error Occurred ")

# import os
# dir=os.getcwd()
# print("Working folder is :",dir)

# import shutil
# dir_del="AI"

# try:
#     shutil.rmtree(dir_del) # for del the directory.
#     print("directory deleted.")
# except FileNotFoundError:
#     print("file was not found.")
# except PermissionError:
#     print("permission denied.")
# except Exception as e:
#     print("An Error Occurred.")

# import shutil
# dir_move="AI"
# try:
#     shutil.move(dir_move,"Ap")    # for move the directory to other directory.
#     print("directory moved successfully.")
# except Exception as e:
#     print("An Error Occurred.")

# import shutil
# dir_copy="Ap"
# try:
#     shutil.copytree(dir_copy,"net")   #for copy the directory in new directory.
#     print("directory copy successfully.")
# except Exception as e:
#     print(f"An Error Occurred: {e}")

#  # csv file create 
# import csv

# with open("Book12.csv",mode="w",newline='')as csvfile:
#     add_csv=csv.writer(csvfile)
#     add_csv.writerow(['Name','Address','Trade'])
#     add_csv.writerow(['vamshi','beside_vamshi','AIPA'])
#     add_csv.writerow(['Diwakar','Behind_vamshi','AIPA'])
# print("CSV created successfully.")

# # open csv file.
# import csv
# with open("Book12.csv",newline='') as csvfile:
#     csv1=csv.reader(csvfile)
#     for row in csv1:
#         print(row)