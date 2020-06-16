import sqlite3

conn = sqlite3.connect('file:executed_offenders.sqlite?mode=ro', uri=True)
cur = conn.cursor()

cur.execute('''SELECT race,country FROM Offenders''')

race_count = dict()
country_count = dict()

for row in cur:
    race = row[0]
    country = row[1]
    race_count[race] = race_count.get(race, 0) + 1
    country_count[country] = country_count.get(country, 0) + 1

cur.close()

rlist = sorted(race_count, key=race_count.get, reverse=True)
clist = sorted(country_count, key=country_count.get, reverse=True)

print('By Race:')
for race in rlist:
    print(race,race_count[race])

print('\nTop 10 by County')
for country in clist[:10]:
    print(country,country_count[country])