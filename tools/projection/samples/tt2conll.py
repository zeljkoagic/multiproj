import sys

i = 1
s = 1
for line in file(sys.argv[1]):
	line = line.strip()
	if line:
		ex = line.split()
		ex.append("meh")
		print("%s\t%s\t_\t%s\t_\t_\t%s\t_\t_\t_" % (i, ex[0], ex[1], i))
		i += 1
	else:
		print
		i = 1
		s += 1
		if s == int(sys.argv[2]):
			break

