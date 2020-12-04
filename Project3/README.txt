TWD Version 3.0 documentation

I created a python script that prompts the user and responds based on input.

The script can be downloaded and run from a folder of your chosing. 
Download the file to the desired folder, navigate to that folder in powershell, and type the command "python .\FinalProject3.py" to run the script.

The user can use this script to find the current date, current time, or weather based on their zipcode rather than manual entry.
    To get the time users should enter "Time"
    To get the date users should enter "Date"
    To get the weather users should enter "Weather"

The script now references multiple API's and pulls data based on Zip Code rather than multiple entries from the user.

I use the re module to check the zip code for a valid 5 number format

The script is not case sensitive.

Any invalid option for either entry will produce a gentle error and loop the user until a valid entry is received.







Version 2.0

Documentation for lab2script.py
Updated Project One
I created a python script that prompts the user and responds based on input.

The script can be downloaded and run from a folder of your chosing. 
Download the file to the desired folder, navigate to that folder in powershell, and type the command "python .\proj2script.py" to run the script.

The user can use this script to find the current date, current time, or both.
    To get the time users should enter "Time"
    To get the date users should enter "Date"
    To get both users should enter "Both"
    
When asking for time or both the user will now be prompted to enter a time zone and given the options "Central", "Eastern", "Mountain", or "Pacific".

The script alters the current time to resemble the time zone the user has selected.

The script is no longer case sensitive!

Any option other than "Time", "Date", or "Both" will loop the user until a valid entry is received.
Any option other than "Central", "Eastern", "Mountain", or "Pacific" will result in an intended user error message and the time is presented in eastern time.



Original Documentation
Documentation for lab1script.py

I created a script that prompts the user and responds based on input.

The user can use this script to find the current date, current time, or both.
    To get the time users should enter "Time"
    To get the date users should enter "Date"
    To get both users should enter "Both"

Script is case sensitive!

Any option other than "Time", "Date", or "Both" will loop the user until a valid entry is received.
