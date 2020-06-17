from matplotlib import pyplot as plt

import sqlite3
#Loading Data
conn = sqlite3.connect('file:executed_offenders.sqlite?mode=ro', uri=True)
cur = conn.cursor()

cur.execute('''SELECT city FROM Offenders''')

city_count = dict()

for row in cur:
    city = row[0]
    city_count[city] = city_count.get(city, 0) + 1

cur.close()

#Data Visualisation

plt.style.use('fivethirtyeight')
#plt.xkcd()

cities = sorted(city_count, key=city_count.get, reverse=True)
count = list()

for city in cities:
    count.append(city_count[city])

#Plotting Top 15 only
cities = cities[:15]
count = count[:15]

cities.reverse()
count.reverse()

plt.barh(cities, count)

plt.ylabel('Cities')
plt.xlabel('No. of Executed Offenders')
plt.title('Death Row Information in Texas')

plt.show()