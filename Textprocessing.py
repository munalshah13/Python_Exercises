# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 18:25:07 2022

@author: munal
"""



# Load eanglish tokenizer
#nlp = spacy.load("en_core_web_sm")

text_line = []
with open('Text-to-Process.txt','r') as f:
    for line in f:
        text_line.append(line.split and line.lower())

print(text_line)