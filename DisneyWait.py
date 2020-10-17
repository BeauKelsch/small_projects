# Get Disney Wait Times
import bs4
import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.laughingplace.com/w/p/magic-kingdom-current-wait-times/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
times_raw = soup.table
ride_wait = []

for i in times_raw:
    wait = str(i.find('span'))
    ride_wait.append(wait)

for i in ride_wait:
    end = i.find('"', 12)
    i.replace('_', ' ')
    ride_name = (i[12:end])
    rts = i.find('">',12)
    rte = i.find('<',rts)
    ride_time = (i[(rts + 2):rte])
    print ('Ride Name:', ride_name, '\nRide wait time: ', ride_time)







