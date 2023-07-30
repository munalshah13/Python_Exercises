# -*- coding: utf-8 -*-
"""
Created on Tue May 23 21:26:26 2023

@author: munal
"""
"""
Display the following menu to the user:
1. create new file
2. Dispaly the file
3.Add a new item to the file.

Make a selection  1, 2 or 3

Ask the user to enter 1, 2 or 3. If they select 
anything other than 1, 2 or 3 it should display a 
suitable error message. 
If they select 1, ask the user to enter a school 
subject and save it to a new file called 
“Subject.txt”. It should overwrite any existing file 
with a new file. 
If they select 2, display the contents of the 
“Subject.txt” file. 
If they select 3, ask the user to enter a new 
subject and save it to the file and then display 
the entire contents of the file. 
Run the program several times to test the 
options
"""
print('Select menu choice:')

print("1) Create a new file")
print("2) Dispaly the file")
print("3) Add a new item to the file")

select = int(input("Enter 1,2,3?:"))

if select == 1:
    subject = input("Enter a name of subject")
    file = open("Subject.txt", "w")
    file.write(subject)
    file.close()
    
elif select == 2:
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
    
elif select == 3:
    file = open("Subject.txt", 'a')
    subject = input("Enter a name of subject:")
    file.write(subject + " \n ")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
    
else:
    print("Error: Invalid option")
    
#