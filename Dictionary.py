# Word Count on different methods
from collections import Counter
text = ('this is sample text with several words 5 this is more sample text with some different words')

counter = Counter(text.split())

"""
word_counts = {} #create empty dictionary to store word in file

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(f'{"WORD":<10}COUNT') # create space between two words
"""
for words,count in sorted(counter.items()):
    print(f'{words:<12}{count}')

print('\nnumber of unique words:', len(counter.keys()))



"""
5           1
different   1
is          2
more        1
sample      2
several     1
some        1
text        2
this        2
with        2
words       2

number of unique words: 11
"""


"""


# Continue advance  Dictionary , Compound Data Strucutures
elements = {"hydrogen": {"number":1, "weight": 1.00794, "symbol": "H"},
             "helium": {"number": 2, "weight": 4.002602, "symbol": "He"}
            }

# Access elements in this nested disctionary

helium = elements["helium"] # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"] # get hydrogen's weight

# you can also add a new key to the element

oxygen = {"number": 2, "weight": 2.0065, "symbol": "o"}
elements["oxygen"] = oxygen # assign oxygen as a key to the element dictionary
print('elements = ', elements)

"""
