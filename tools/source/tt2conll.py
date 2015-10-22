import sys

i = 1

for line in file(sys.argv[1]):
	line = line.strip()
	if line:
		ex = line.split()
		print("%s\t%s\t_\t%s\t_\t_\t%s\t_\t_\t_" % (i, ex[0], ex[1], i))
		i += 1
	else:
		print
		i = 1
