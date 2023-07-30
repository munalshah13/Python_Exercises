
from datetime import datetime as dt
def hello(fname, lname, datestring = ' '):
    msg = 'Hello ' + " " + fname + " " + lname
    msg += 'you mentioned' + datestring
    print(msg)

fname = input("Enter you first name: ")
lname = input("Enter your lastname:")
x =  dt.datetime.now()
print(x)

hello(fname, lname, datestring =  x)
