#!/usr/bin/env python3

"""
Quiz: Generate Messages

Imagine you're a teacher who needs to send a message to each of your students reminding them of their missing assignments and grade in the class. You have each of their names, number of missing assignments, and grades on a spreadsheet and just have to insert them into placeholders in this message you came up with:

    Hi [insert student name],

    This is a reminder that you have [insert number of missing assignments] assignments left to submit before you can graduate. Your current grade is [insert current grade] and can increase to [insert potential grade] if you submit all assignments before the due date.

You can just copy and paste this message to each student and manually insert the appropriate values each time, but instead you're going to write a program that does this for you.

Write a script that does the following:

    Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
    Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.

Template code for your script:

names =  # get and process input for a list of names
assignments =  # get and process input for a list of the number of assignments
grades =  # get and process input for a list of grades

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message

Below is an example of a successful run of this script in the terminal.

name = input('Enter a name:')
assignments = input('Enter a list of assignment:')
grades = input('Enter a grade')


"""

name = input("Enter a list of name:").title().split(",")
assignments = input("Enter a list of the number assignment:").split(",")
grades = input("Enter a list of grades:").split(",")

Report = "This is your grade report. \n Name: {} \n Assignment: {} \n Grades:{}\n"
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"


for name, assignments, grades in zip(name,assignments,grades):
    print(Report.format(name, assignments, grades))
    print(message.format(name,assignments,grades,  int(grades) + int(assignments)*2))
