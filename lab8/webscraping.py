from bs4 import BeautifulSoup
import requests, re


r = requests.get('https://nakedsecurity.sophos.com/').content
soup = BeautifulSoup(r, 'lxml')
span = soup.find("h2", {"class":"slide-title"})
title = span.text
#span = soup.find("span", {"class":id="by"})
#author = span.text

print('The most recent story from nakedsecurity.sophos.com is: %s' % (title))
