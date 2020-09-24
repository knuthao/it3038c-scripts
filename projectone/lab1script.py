from datetime import date
from datetime import datetime

curdate = date.today()
showdate = curdate.strftime("%B %d, %Y")
curtime = datetime.now()
showtime = curtime.strftime("%H:%M")

answer=1
print('Hello! Please type "Time" if you would like to know the current time, type "Date" if you would like to know the current date, or "Both" if you would like to know the current date and time!')
dtb = input()
while answer > 0:
    if dtb == 'Time':
        print("The current time is ", showtime, "!")
        answer=answer-1
    elif dtb == 'Date':
        print("The curent date is ", showdate, "!")
        answer=answer-1
    elif dtb == 'Both':
        print("The current time is ", showtime, " and the current date is ", showdate,"!")
        answer=answer-1
    else: 
        print("Please enter a valid option. Check your Capitalization!")
        dtb = input()
print("Check back any time for the current date, time, or both!")
