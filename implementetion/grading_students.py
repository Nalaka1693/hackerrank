#!/bin/python

import sys

def solve(grades):
	glen = len(grades)
	for i in range(glen):
		if grades[i] < 38:
			pass
		elif (5 - grades[i] % 5) < 3:
			grades[i] += (5 - grades[i] % 5)
	return grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
	grades_t = int(raw_input().strip())
	grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))


