import datetime
import time
from datetime import datetime
from datetime import timedelta

print('Hello! I am able to tell you how many seconds old you are!')
print('First you must tell me some information:')

#year
valid=1
while valid > 0:
    print('Birth Year (ex. 1919):')
    byear = int(input())
    if byear > 2020:
        print('Your Birth Year cannot be larger than 2020!')
    elif byear < 1903:
        print('You are not the oldest person alive!')
    else:
        valid=valid-1
#month/day
valid = 1
while valid > 0:
    print('Birth Month (numeric ex. 3 = March):')
    bmonth = int(input())
    if bmonth < 1 or bmonth > 12:
        print('That is not a valid month!')
    elif bmonth == 2:
        if byear%4==0:
            print('Birth Day (1-29):')
            bday = int(input())
            if bday <0 or bday >29:
                print('This is not a valid day')
            else:
                valid=valid-1
        else:
            print('Birth Day (1-28):')
            bday = int(input())
            if bday <0 or bday >28:
                print('This is not a valid day')
            else:
                valid=valid-1
    elif bmonth == 4 or bmonth == 6 or bmonth == 9 or bmonth == 11:
        print('Birth Day (1-30):')
        bday = int(input())
        if bday <0 or bday >30:
            print('This is not a valid day')
        else:
            valid=valid-1
    else:
        print('Birth Day (1-31):')
        bday = int(input())
        if bday <0 or bday >31:
            print('This is not a valid day')
        else:
            valid=valid-1
#Hour
print('The hour you were born (0-23):')
bhour = int(input())
while bhour>23 or bhour<0:
    print('Enter a valid hour:')
    bhour = int(input())
#minute
print('The minute you were born (0-59):')
bmin = int(input())
while bmin>59 or bmin<0:
    print('Enter a valid minute:')
    bmin = int(input())
#second
print('The second you were born (0-59):')
bsec = int(input())
while bsec>59 or bsec<0:
    print('Enter a valid second:')
    bsec = int(input())

#current time

today = datetime.now()
curyear = today.year
curmonth = today.month
curday = today.day
curhour = today.hour
curmin = today.minute
cursec = today.second

#calculation

datetimeFormat = '%Y %m %d %H %M %S'
bdate = datetime(int(byear), int(bmonth), int(bday), int(bhour), int(bmin), int(bsec))
curdate = datetime(int(curyear), int(curmonth), int(curday), int(curhour), int(curmin), int(cursec))


diff = curdate - bdate

print("You are", diff.total_seconds(), "seconds old!")