# Date and time program
# Import the datetime module give it an alias of it.

import datetime as dt
#import timezone helpers from dateutill
from dateutil.tz import gettz # install pip install python-dateutil

# Working with Time Zones
# Get the time from computer clock
here_now = dt.datetime.now()

# Get the UTC datetime right now
utc_now = dt.datetime.utcnow()

# Substract to see difference
time_difference = (utc_now - here_now)

#USA Mountain time
mst = dt.datetime.now(gettz('America/Boise'))
print(f"{mst:%A %D %I: %M %p %Z}")
print(f"My time : {here_now:%I:%M %p}")
print(f"UTC time : {utc_now:%I:%M %p}")
print(f"Difference : {time_difference}")




"""
# put today's date in today variable
today = dt.date.today()
midnight = dt.time()

curr_time = dt.datetime(" %A, %B %d at %I:%M%p ")

print(f"{today:%A,%B %d, %Y,}", midnight)

print(curr_time)
"""


"""
# Calculating age in yers and months from a timedelta
# today's date
today = dt.date.today()

# Birthday express as year, month, day
birthdate =dt.date(1997,12,31)

# Duration between the date as timedelta
delta_age = (today -birthdate)

# Duration between the date as a number (of days)

days_old = delta_age.days

# Floor divide days by 365 to get the number of years
year = days_old // 365

# Days Left over is remainder of days_old divided by 365
#  divide that remainder by 30 for approximate month .

months = (days_old % 365) // 30


# Print in a format to your  liking
print(f" You are {year} years and {months} month old.")

"""
