import employee
# implement program for employee managment system

FileName = 'employee.dat'  # constant for the filename

# Global constant for menu choice
LOOK_UP = 1
ADD  = 2
EDIT = 3
DELETE = 4
QUIT = 5


# main function

def main():

    #Load the exiting contact disctionary and  assign it to mycontacts

    mycontacts = load_contacts()

   # Initialize variable for the user's choice
    choice = 0

    while choice != QUIT:

        # get the user menu choice
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        
        elif choice == ADD:
            add(mycontacts)
            
            
        
            

def load_contacts():
    try:
        # Open the contacts.dat file

        input_file = open(FileName, 'rb')

        # Unpickle the dictionary
        contact_dct = pickle.load(input_file)

        # close the phone_inventory.dat file.
        input_file.close()

    except IOError:

        #couldn't open the file, so create an empty dictionary
        contact_dct = {}

    #return the dictionary
    return contact_dct
    

def get_menu_choice():

    print()
    print("Meni Choice")
    print('----------------')
    print('1. Look up contact information.')
    print('2. Add information.')
    print('3. Edit information.')
    print('4. Delete information.')
    print('5. Quite.')
    print()

    # get the user choice
    choice = int(input("Enter your choice:"))

    #validate user choice, prompts the user to reenter his or her choice.

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter a valid choice:"))
        
    return choice

def look_up(mycontacts):

    first_name = input('Entr a name:')
    id_number = int(input("ID number:"))

    #Look it up in the dictionary
    print(mycontacts.get(first_name, 'That name is not found.'))

    print(mycontacts.get(id_number, ''))

#add funcation add new entry of employee into empty dictionary

def add(mycontacts):

    fname = input("Enter first name:")
    lname = input("Enter Last name:")
    gender = input("What is your Gender:")
    age = input("What is your age?")
    address = input("What is your address?")
    pnum = input("Enter 10 digit phone number:")
    idnum = int(input("Enter ID number:"))
    email = input("Enter email address:")
    dept = input("What is your department?:")
    jtitle = input("What is your job title?")



    # Create a Contact object name entry

    entry = employee.Employee(fname, lname, gender, age, address, pnum,idnum, email, dept, jtitle)

    name = fname + lname
    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')
    
    
    
    
    
    


# call the main funcation
if __name__ == '__main__':
    main()

        
