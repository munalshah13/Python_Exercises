# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 21:24:25 2023

@author: munal
"""
import Employee1
import pickle

# Global constant for menu choice

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT  = 5

# Global Constant for the file name
Filename = 'Employee.dar'


# main funcation()
def main():
    
    
    myinfo = load_information()  # Load the existing contact dictionary and assighn it to mycontacts
    
    choice = 0
    while choice != QUIT:
        choice = get_menu_choice()
        
        #Process the choice
        if choice == LOOK_UP:
            look_up(myinfo)
        elif choice == ADD:
            add_employee_name_number(myinfo)
        elif choice == CHANGE:
            change(myinfo)
        elif choice == DELETE:
            delete(myinfo)
        else:
            print("QUIT program: there is no option")
            
            
            
    save_contacts(myinfo)
            
            
            
def get_menu_choice():
    
    print()
    print("Menu")
    print("___________________")
    print("1. Look up a information")
    print("2. Add a new information")
    print("3. Change an exiting information.")
    print("4. Delet information")
    print("5. Exit the program.")
    print()
    
    # get the user input
    choice = int(input("Enter your choice:"))
    
    # validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice:'))
        
    return choice
    
    
def load_information():
    try:
        
        #open the file 
        input_file = open(Filename, mode= 'rb')
                          
        
        # unpickle the dictionary
        
        Employee_dar = pickle.load(input_file)
        
        # close the file
        input_file.close()
    except IOError:
        #Could not open file, so create an empty dictionary
        Employee_dar = {}
        
    return Employee_dar

def look_up(myinfo):
    
    name = input('Enter a name:')

    #number = int(input("Enter a number:"))
    print(myinfo.get(name, 'This name not found in file'))
    

def add_employee_name_number(myinfo):
    name = input("Employee name:")
    email  = input('Email:')
    number = input('Employee numbe:')
                   
    
    
    # create a employee object in memory and assign it to the entry varaible.
    entry = Employee1.Employee(name,email,number)
    
    if name not in myinfo:
        myinfo[name] = entry
        print("The entry has been  added.")
    else:
        print('That name already exits')
        
def change(myinfo):
    # Get a name to llok up
    
    name = input("Enter a name:")
    
    if name in myinfo:
        # Get a new email
        email = input("Email:")
        number = int(input("Enter a number:"))
        
        # Create employee email and number 
        entry = Employee1.Employee(name, email, number)
        
        #update entry
        myinfo[name] = entry
        print("information Update")
    else:
        print("That name is not found")
        
def delete(myinfo):
    #get name to look up
    
    name = input("Enter name:")
    
    if name in myinfo:
        del myinfo[name]
        print("Entry deleted")
    else:
        print("That name is not found")

def save_contacts(myinfo):
    
    # Open the file for writing
    output_file = open(Filename, 'wb')
    
    # Pickle the dictionary and save it.
    pickle.dump(myinfo, output_file)
    
    #close the file
    output_file.close()


if __name__ == '__main__':
    main()