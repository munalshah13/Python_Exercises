# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:34:36 2023

@author: munal
"""

compnum = 50
count = 0
guess = int(input("Enter a number:"))

while guess != compnum:
    if guess < compnum:
        print("Too Low")
    else:
        print("Too High")
    count = count + 1
    guess = int(input("Do you want to another guess num? (y/n)"))
print("Well dine", count,"You done")
