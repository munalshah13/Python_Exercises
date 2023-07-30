import datetime, time, calendar
import sys

# The default  string represent of datetime object use the ISO-8601 format(YYYY -MM -DDTHH:MM:SS.mmmmmm).
# Alternative formats can be generated using strftime()

today  = datetime.date.today()
print(today)

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format) # datetime.strptime() to convert frmateed string to datetime instance
print('strptime:', d.strftime(format))

"""
 calender ; work with Dates
Calender modules define the calendar calss which calculations for value such as the date of the weeks in agiven month or year

c  = calendar.TextCalendar(calendar.SUNDAY)
c.prmonth(2023,3) # Prmonth() methid is a simple funcation the produce the formatted text output for a month
"""

cal  = calendar.TextCalendar(calendar.SUNDAY).formatyear(2023, 2,1,1,3) # formattyear() print all the months calander
print(cal)
"""
To produce a clander formated for a local other than the current defualt, use Locale- TextCalender or LocaleHTMLCalendar

"""

ca = calendar.LocaleTextCalendar(locale='fr_FR')
print(ca.prmonth(2023,3))




"""
Calculating Date.
Ex: Atlanta user's group meets on the second thursday of every month. To calculate the date for the mettings for a year, use the return value of monthcalendar()
( Assuming they are always on the second thursday of everymonth). look at the output of monthcalendar() to find the dates on
which Thursdays fall. The first and last weeks of the month are padded with 0 values as
placeholders for the days falling in the preceding and subsequent months, respectively. For
example, if a month starts on a Friday, the value in the first week in the Thursday position
will be 0.

"""

"""
year = int(sys.argv[1])

# Show every month
for month in range(1,13):
    # Comput the dates for each week that overlaps the month.

  cale = calendar.monthcalendar(year, month)
  first_week = c[0]
  second_week = c[1]
  third_week = c[2]

  #If there is a thursday in the first_week
  # the second Thursday is in the second week
  # Otherwise, the second Thursday must be in the third week
  if first_week[calendar.THURSDAY]:
      meeting_date = second_week[calendar.THURSDAY]
  else:
      meetting_date = third_week[calendar.THIURSDAY]

  print('{:>3}:{:>2}'.format(calendar.month_abbr[month], meeting_date))
  
"""
