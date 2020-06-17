from matplotlib import pyplot as plt

import sqlite3
#Loading Data
conn = sqlite3.connect('file:executed_offenders.sqlite?mode=ro', uri=True)
cur = conn.cursor()

cur.execute('''SELECT race FROM Offenders''')

race_count = dict()

for row in cur:
    race = row[0]
    race_count[race] = race_count.get(race, 0) + 1

cur.close()

#Data Visualisation

plt.style.use('fivethirtyeight')
#plt.xkcd()

race_x = list(race_count.keys())
count_y = list(race_count.values())

plt.xlabel('Race')
plt.ylabel('No. of Executed Offenders')
plt.title('Death Row Information in Texas')
plt.bar(race_x, count_y, width=0.3)

plt.show()