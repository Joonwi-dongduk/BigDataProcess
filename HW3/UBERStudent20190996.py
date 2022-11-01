#!/usr/bin/python3

import sys
input = sys.argv[1]
output = sys.argv[2]

file = open(output, "wt")
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
with open(input, "rt") as f:
	while True:
		line = f.readline()
		if not line:
			break
		cont = line.split(',')
		num = cont[0]
		date = cont[1].split('/')
		vehicles = cont[2]
		trips = cont[3]

		import calendar
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		file.write("%s,%s %s,%s" %(num, weekday[day], vehicles, trips))

file.close()
