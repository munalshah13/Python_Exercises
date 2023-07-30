# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:38:18 2023

@author: munal
"""
class Employee:
    def __init__(self, name, email, number):
        self.__name = name
        self.__email = email
        self.__number = number                # instance attribute
        
    # Accessor method return the name attribute 
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_number(self):
        return self.__number
    
    # The set_name method sets the atrribute 
    def set_name(self, name):
        self.__name = name
        
    def set_email(self,email):
        self.__email = email
        
    def set_number(self, number):
        self.__number = number
    
    
    # The __str__ method returns the objects state as a string
    def __str__(self):
        return "Name:" + self.__name + \
               "Email:" + self.__email + \
               "Number:" + self.__number 