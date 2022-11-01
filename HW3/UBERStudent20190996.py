#!/usr/bin/python3

import sys
input = sys.argv[1]
output = sys.argv[2]

file = open(output, "wt")
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
weekday = [{}, {}, {}, {}, {}, {}, {}]


with open(input, "rt") as f:
	while True:
		line = f.readline()
		if not line:
			break
		
		cont = line.split(',')
		num = cont[0]
		date = cont[1].split('/')

		import calendar
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		if num in weekday[day].keys():
			vehicles = int(weekday[day][num].split(',')[0]) + int(cont[2])
			trips = int(weekday[day][num].split(',')[1]) + int(cont[3])
			weekday[day][num] = str(vehicles) + ',' + str(trips)
		else:
			weekday[day][num] = cont[2] + ',' + cont[3]
		weekday[day][num]

		vehicles = cont[2]
		trips = cont[3]

#		file.write("%s,%s %s,%s" %(num, weekday[day], vehicles, trips))

for n in range(7):
	for w in weekday[n].keys():
		file.write("%s,%s %s\n" %(w, week[n], weekday[n][w]))

file.close()
