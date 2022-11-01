import sys
input = sys.argv[1]
output = sys.argv[2]

file = open(output, "wt")
with open(input, "rt") as f:
	while True:
		line = f.readline().split('::')
		if not line[0]:
			break
		title = line[1][0:-7]
		id = line[0]
		file.write("%s %s\n" %(title, id))
file.close()
