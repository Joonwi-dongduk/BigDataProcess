#!/usr/bin/python3

import sys
input = sys.argv[1]
output = sys.argv[2]

file = open(output, "wt")
weekday = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
with open(input, "rt") as f:
	while True:
		line = f.readline().split(',')
		if not line[0]:
			break

		num = line[0]
		date = line[1].split('/')
		vehicles = line[2]
		trips = line[3]

		import calendar
		day = calendar.weekday(int(date[2]), int(date[0]), int(date[1]))
		file.write("%s,%s %s,%s" %(num, weekday[day], vehicles, trips))
	#	print("%s,%s %s,%s" %(num, weekday[day], vehicles, trips), end='')

file.close()
