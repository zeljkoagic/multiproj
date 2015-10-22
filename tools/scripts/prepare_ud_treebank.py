import sys
import codecs

reload(sys)
sys.setdefaultencoding('utf8')

sys.stdin = codecs.getreader('utf8')(sys.stdin)
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

for line in codecs.open(sys.argv[1], encoding="utf8"):
	line = line.strip()
	if line:
		if line[0] == "#":
			continue
		ex = line.split("\t")
		id = ex[0]
		form = ex[1]
		pos = ex[3]
		head = ex[6]
		deprel = ex[7]

		if sys.argv[2] == "delex":
			form = "_"

		if id.isdigit():
			print("%s\t%s\t_\t%s\t_\t_\t%s\t%s\t_\t_" % (id, form, pos, head, deprel))
	else:
		print
