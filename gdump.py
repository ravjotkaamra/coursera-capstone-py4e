import sqlite3

conn = sqlite3.connect('file:executed_offenders.sqlite?mode=ro', uri=True)
cur = conn.cursor()

cur.execute('''SELECT race,city FROM Offenders''')

race_count = dict()
city_count = dict()

for row in cur:
    race = row[0]
    city = row[1]
    race_count[race] = race_count.get(race, 0) + 1
    city_count[city] = city_count.get(city, 0) + 1

cur.close()

rlist = sorted(race_count, key=race_count.get, reverse=True)
clist = sorted(city_count, key=city_count.get, reverse=True)

print('By Race:')
for race in rlist:
    print(race,race_count[race])

print('\nTop 10 by City')
for city in clist[:10]:
    print(city,city_count[city])