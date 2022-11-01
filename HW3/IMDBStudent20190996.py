#!/usr/bin/python3

import sys
input = sys.argv[1]
output = sys.argv[2]

file = open(output, "wt")
genList = {}
with open(input, "rt") as f:
	while True:
		line = f.readline()
		if not line:
			break
		cont = line.split('::')
		genre = cont[2].split('|')
		for g in genre:
			if '\n' in g:
				g = g[:-1]
			if g in genList.keys():
				genList[g] += 1
			else:
				genList[g] = 1
for g in genList.keys():
	file.write("%s %d\n" %(g, genList[g]))
file.close()
