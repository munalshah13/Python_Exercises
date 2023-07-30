# -*- coding: utf-8 -*-
"""
Created on Mon May 22 19:54:58 2023

@author: munal
"""

'''
import unicordcsv

enrollments_filename = '/Users/munal/Downloads/enrollments.csv'

daily_enrollments = []
f = open(enrollments_filename, 'rb')
reader = unicodecsv.DictReader(f)
for row in reader:
    daily_enrollments.append(row)
    print(daily_enrollments)
'''
import random

num = random.randint(0,10)
name = input("Enter your name:")

file = open("Numbers.txt", "a") # write a new file called Number.txt
file.write(str(num))
file.write("\n")
file.write("Tom\n")
file.write("Alex\n")
file.write("Mike\n")
file.write(name)
file.close()

file = open("Numbers.txt", "r")
print(file.readlines())

with open("Intro.txt", "r") as myinputfile:
    for line in myinputfile.readlines():
        print(line)
    