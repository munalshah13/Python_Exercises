# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:18:58 2023

@author: munal
"""

"""
You are driving a little too fast, and a police officer stops you. 
Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases. 
"""

def spedding(speed,is_birthday):
    
    if speed <= 60 or (speed <=65 and is_birthday):
        print("No Tickets")
    if (speed >= 61 and speed >=80) and is_birthday:
        print("Small tickets")
    if speed >=81 and is_birthday:
        print("Big tickets")
        
spedding(45,True)
    
"""
Ask which direction the user wants to count (up or down). If they select up, then ask 
them for the top number and then count from 1 to that number. If they select down, ask 
them to enter a number below 20 and then count down from 20 to that number. If they 
entered something other than up or down, display the message “I don’t understand”.
"""
select = input("Which direction the user wats to count(u or d)?")
if select == 'u':
    num = int(input("what is above number?:"))
    for i in range(1, num + 1):
        print(i)
elif select == 'd':
    num = int(input("What is the below num?"))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I dont understand")





"""

"""