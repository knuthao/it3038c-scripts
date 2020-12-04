import re
import json
import requests

count =1
print(' ')
print('    - Welcome to TDW Version 3.0! -   ')
print('I can provide the Time, Date, and Weather for any U.S. zipcode.')
print('Enter your zipcode here:')
while count>0:
    zip= input()
    if re.search("^[0-9]{5}(?:-[0-9]{4})?$", zip):
        count=count-1
    else:
        print('This is not a valid ZIP code. Enter a valid zipcode:')

tzapi = requests.get("http://www.zipcodeapi.com/rest/xW708eUARknS04iKfYzRl0q5bXbnDHVXd5XKtzsCjLvJp1V17hdKIxZAx2cj4zBS/info.json/%s/degrees" % zip)
tzdata = tzapi.json()
tz = tzdata['timezone']['timezone_identifier']

tdapi = requests.get("https://api.ipgeolocation.io/timezone?apiKey=a2e669fce72a4083a49021d7a5125711&tz=%s" % tz)
tddata = tdapi.json()
time = tddata['time_12']
datewt = tddata['date_time_txt']
date = datewt[:-8]

wapi = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=68216b2c61a58b2d3f3e1f481e601e78" % zip)
wdata = wapi.json()
weather = wdata['weather'][0]['description']

recount = 1
print('Now type "Time", "Date", or "Weather"!')
dtb = input().lower()

while recount>0:
    if dtb == "time":
        print(time)
        recount=recount-1
    elif dtb == "date":
        print(date)
        recount=recount-1
    elif dtb == "weather":
        print(weather)
        recount=recount-1
    else:
        print('Unfortunately we do not provide that feature yet. Please enter "Time", "Date", or "Weather":')
