from __future__ import division
import sys

file1 = open(sys.argv[1]).readlines()
file2 = open(sys.argv[2]).readlines()

total = 0
correct = 0

for i in range(0, len(file1)):
	if file1[i].strip():
		ex1 = file1[i].strip().split()[9]
		ex2 = file2[i].strip().split()[8]
		if ex1 == ex2:
			correct += 1
		total += 1

print correct / total

