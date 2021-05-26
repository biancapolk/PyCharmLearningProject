'''DateTime Modules'''

import datetime
from datetime import date
'''create new date instances uses the replace() method of an existing date'''
d1 = datetime.date(2015, 3, 11)
print('d1:', d1)

d2 = d1.replace(year=1990)
print('d2:', d2)

'''mytime module'''
mytime = datetime.time(2,20)
print(mytime)
print(mytime.hour)
print(mytime.tzinfo)

'''Useful date functions'''
from datetime import date
today = datetime.date.today()
print(today.day)
print(today.weekday())
print(today.today())

# mydatetime = datetime(2021, 10, 2, 14, 20, 1)
# print(mydatetime)

'''Arithmetic on date objects Day 1 - Day 2'''
date1 = date(2023,11,3)
date2 = date(2021,11,3)
result = date1 - date2
print(f"There is a {result.days} day difference between these daytes.")

'''Determining range by using min and max attributes'''
print('Earliest  :', datetime.date.min)
print('Latest    :', datetime.date.max)
print('Resolution:', datetime.date.resolution)



