# collision.py
# Example solution for Lab 6, problem 1
#
# Aseem Kishore
#
# 6.189 - Intro to Python
# IAP 2008 - Class 4


# Imports should usually go at the top of a program instead of in the main code.

from math import *


# These helper functions let me "abstract away" the syntax of getting a ball's
# x- and y- coordinates, or its radius. This makes my code more readable and
# also helps prevent bugs where I use x instead of y, etc.

def get_x(ball):
    return ball[0]

def get_y(ball):
    return ball[1]

def get_r(ball):
    return ball[2]


# I got this function from the second day of class. We've been trying to tell
# you guys the importance of functions; here's one -- reuse. There are many
# applications for finding the distance between two points; detecting collision
# is one, so we can reuse the function. This is also why we don't ask for input
# or print our result inside the function.

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


# Here is my detect collision function. Note that I'm NOT taking six variables
# like x1, y1, r1, x2, y2, r2 -- that's the purpose of combining x, y, r into a
# tuple, as every ball has an x, y and r.

def collision(ball1, ball2):
    d = distance(get_x(ball1), get_y(ball1), get_x(ball2), get_y(ball2))
    sum_of_radii = get_r(ball1) + get_r(ball2)
    return d < sum_of_radii


# My test cases

print ("First test case:",)

a = (0, 0, 1)
b = (3, 3, 1)

if collision(a, b):
    print ("Oops, we detected a collision!")
else:
    print ("Passed!")

print ("Second test case:",)

a = (5, 5, 2)
b = (2, 8, 3)

if collision(a, b):
    print ("Passed!")
else:
    print ("Oops, we didn't detect a collision!")





'''
6.189 - Intro to Python
IAP 2008 - Class 4
Lead: Aseem Kishore
Lab 6: Tuples and Strings
Problem 1 – Collision detection of balls
Many games have complex physics engines, and one major function of these engines is to
figure out if two objects are colliding. Weirdly-shaped objects are often approximated as balls. In
this problem, we will figure out if two balls are colliding.

We will think in 2D to simplify things, though 3D isn’t different conceptually. For calculating
collision, we only care about a ball’s position in space and its size. We can store position with its
center x-y coordinates, and we can use its radius for size. So a ball is a tuple of (x, y, r).
To figure out if two balls are colliding, we need to compute the distance between their centers,
then see if this distance is less than the sum of their radii. If so, they are colliding.
Write a function that takes two balls and computes if they are colliding. Then call the function
with two sets of balls. The first set is (0, 0, 1) and (3, 3, 1); these should not be colliding. The
second set is (5, 5, 2) and (2, 8, 3); these should be colliding.

Problem 2 – Pig-Latin Converter
Write a program that lets the user enter in some English text, then converts the text to Pig-Latin.
To review, Pig-Latin takes the first letter of a word, puts it at the end, and appends “ay”. The
only exception is if the first letter is a vowel, in which case we keep it as it is and append “hay”
to the end.

E.g. “hello” Æ “ellohay”, and “image” Æ “imagehay”
It will be useful to define a list or tuple at the top called VOWELS. This way, you can check if a
letter x is a vowel with the expression x in VOWELS.
It’s tricky for us to deal with punctuation and numbers with what we know so far, so instead, ask
the user to enter only words and spaces. You can convert their input from a string to a list of
strings by calling split on the string:

“My name is John Smith”.split(“ ”) Æ [“My”, “name”, “is”, “John”, “Smith”]
sing this list, you can go through each word and convert it to Pig-Latin. Also, to get a word
ints: It will make your life much easier – and your code much better – if you separate tasks into
U
except for the first letter, you can use word[1:].
H
functions, e.g. have a function that converts one word to Pig-Latin rather than putting it into your
main program code.
'''
