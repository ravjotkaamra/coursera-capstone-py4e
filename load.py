import urllib.request, urllib.parse, urllib.error
import ssl
import sqlite3
from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.tdcj.texas.gov/death_row/dr_executed_offenders.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

print('Retrieving:',url)
conn = sqlite3.connect('executed_offenders.sqlite')
cur = conn.cursor()

cur.execute('''
            CREATE TABLE IF NOT EXISTS Offenders
            (id INTEGER UNIQUE, first_name TEXT, last_name TEXT, age INTEGER, date TEXT, race TEXT, city TEXT)
            ''')

tags = soup('tr')
count = 0
for tag in tags:
    
    data = tag('td')

    if(len(data)<1):continue

    count = count + 1

    last_name = data[3].text.strip()
    first_name = data[4].text.strip()
    age = int(data[6].text.strip())
    date = data[7].text.strip()
    race = data[8].text.strip()
    city = data[9].text.strip()

    cur.execute('''INSERT OR IGNORE INTO Offenders (id, first_name, last_name, age, date, race, city) VALUES (?, ?, ?, ?, ?, ?, ?)''',
    (count ,first_name, last_name, age, date, race, city))
    
    if(count%100==0):conn.commit()

print('No of offenders executed:',count)

conn.commit()