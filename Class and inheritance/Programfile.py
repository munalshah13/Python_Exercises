# This program manage contact

import PersonalInformation
# a program taht creates three instance of the class
# One instance should hold your infromation,and other two hold your freind's or family members information



def main():
    f_name = input("Enter your name:")
    l_name =  input("Enter last name:")
    gen =  input("Enter gender:")
    age =  int(input("Enter age:"))
    addr =  input("Enter address:")
    p_num =  int(input("Enter phone number:"))


    my_info = PersonalInformation.Information(f_name,l_name,gen,age,addr,p_num)
    f_info = PersonalInformation.Information(f_name,l_name,gen,age,addr,p_num)
    fa_info = PersonalInformation.Information(f_name,l_name,gen,age,addr,p_num)


  
    print("Data Dispaly for my info")
    print("-----------------")
    print(f'Name:{my_info.get_fname() + my_info.get_lname()}')
    print(f'Gender: {my_info.get_gender()}')
    print(f' Age: {my_info.get_age()}')
    print(f'Address: {my_info.get_address()}')
    print(f'PhoneNumber: {my_info.get_phone_number()}')

    
  
     
# call the main function

if __name__ == '__main__':
    main()
    
