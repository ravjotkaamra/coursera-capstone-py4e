from matplotlib import pyplot as plt
import sqlite3

#Loading Data
conn = sqlite3.connect('file:executed_offenders.sqlite?mode=ro', uri=True)
cur = conn.cursor()

cur.execute('''SELECT age,race FROM Offenders''')

black_age = list()
white_age = list()
hispanic_age = list()

for row in cur:
    age = row[0]
    race = row[1]

    if race=='Black':black_age.append(age)
    elif race=='White':white_age.append(age)
    elif race=='Hispanic':hispanic_age.append(age)

cur.close()


#Data Visualisation
plt.style.use('bmh')
#plt.xkcd()

legend = ['Black', 'White', 'Hispanic']
bins = [10, 20, 30, 40, 50, 60, 70, 80]
plt.hist([black_age, white_age, hispanic_age], bins=bins)


plt.xlabel('Age Range')
plt.ylabel('No Of Exectuted Offenders')
plt.title('Death Row Information in Texas')

plt.legend(legend)

plt.show()