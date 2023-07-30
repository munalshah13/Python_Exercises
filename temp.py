# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
try:
    name = input('Ener list of  your name here:').title().split(",")
    assignments = input('Enter a number of assignments:').split(",")
    grades = input('Enter a list of grades:').split(",")
    
except ValueError:
    print('That\s not valid answr!')

message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignments, grades in zip(name, assignments, grades):
    print(message.format(name,assignments,grades, int(assignments) + int(grades) *2))