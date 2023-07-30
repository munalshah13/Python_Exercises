# Persoanl information Classes

class Information:

    #construction also called initialize method

    def __init__(self,first_name,last_name, gender,
                 age,address, phone_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__age = age
        self.__address = address
        self.__phone_number = phone_number

    # Accessor and mutatore methods

    def set_fname(self,first_name):
        self.__first_name = first_name
    def set_lname(self,last_name):
        self.last_name = last_name
    def set_gender(self,gender):
        self.__gender = gender
    def set_age(self,age):
        self.__age = age
    def set_address(self,address):
        self.__address = address
    def set_phone_number(self,pnum):
        self.__phone_number = phone_number

    # mutator methos

    def get_fname(self):
        return self.__first_name 
    def get_lname(self):
        return self.__last_name 
    def get_gender(self):
        return self.__gender 
    def get_age(self):
        return self.__age
    def get_address(self):
        return self.__address 
    def get_phone_number(self):
        return self.__phone_number 

    def __str__(self):
        return 'FirstName:' + self.__first_name + ' ' + self.__last_name + \
               '\nGender:' + self.__gender + \
               '\nAge:' + self.__age + \
               '\nAddress:' + self.__address + \
               '\nPhoneNumber:' + self.__phone_number 

class Employee(Information):
    def __init__(self,first_name, last_name, gender,age, address, phone_number, id_number, email, department, job_title):
        # Call the superclass's __init__ method and pass required arguments
        # we also have to pass self as an argument
        Information.__init__(self, first_name, last_name, gender, age, address, phone_number)

        # initialize enumber and email
        self.__id_number = idnum
        self.__email = email
        self.__department = dept
        self.__job_title = job_title
        
    def set_id_number(self,id_number):
        self.__id_number = idnum
    def set_email(self, email):
        self.__email = email
    def set_department(self, department):
        self.__department = dept
    def set__job_title(self,job_title):
        self.__job_title = job_title
        
    def get_id_number(self):
        return self.__idnum
    def get_email(self):
        return self.__email
    def get_department(self):
        return self.__dept
    def get_job_title(self):
        return self.__job_title
        
    

   

        
