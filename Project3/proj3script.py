from datetime import date
from datetime import datetime
from datetime import timedelta

curdate = date.today()
showdate = curdate.strftime("%B %d, %Y")
curtime = datetime.now()


print('    Welcome to TDW Version 3.0!   ')
print('I can provide the Time, Date, and Weather for any U.S. zipcode.')
print('Enter your zipcode here:')
zip= input()
answer=1
print('Now type "Time", "Date", or "Weather"!')
dtb = input().lower()
if dtb == 'time' or dtb == 'both':
    print('Please select one of the available timezones. The options are "Eastern", "Central", "Mountain", and "Pacific" Standard Time.')
    tz = input().lower()
    if tz =="central":
        curtime = datetime.now() - timedelta(hours=1)
    elif tz =="mountain":
        curtime = datetime.now() - timedelta(hours=2)
    elif tz =="pacific":
        curtime = datetime.now() - timedelta(hours=3)
    else:
        print('That is not a valid time zone. The default time zone (Eastern) has been used.')
showtime = curtime.strftime("%I:%M")
while answer > 0:
    if dtb == 'time':
        print("The current time is ", showtime, "!")
        answer=answer-1
    elif dtb == 'date':
        print("The curent date is ", showdate, "!")
        answer=answer-1
    elif dtb == 'both':
        print("The current time is ", showtime, " and the current date is ", showdate,"!")
        answer=answer-1
    else: 
        print("Please enter a valid option. Check your Capitalization!")
        dtb = input()
print("Check back any time for the current date, time, or both! Now in any timezone!")
