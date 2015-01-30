#!/bin/env python

import fileinput

header = ""
for line in open("sloka-begin-html"):
	header += line

header2 = ""
for line in open("sloka-begin2-html"):
	header2 += line

footer = ""
for line in open("sloka-end-html"):
	footer += line

first = True
id = ""
for line in fileinput.input():
	line = line.strip()	
	if line == "":
		continue
	if "TEXT" in line:
		if id != "":
			print(footer, file=of)
			first = False
			of.close()
		ids = line.split()
		# print(ids[1])
		line = ids[1]
		id = line
		ofilename = id + ".html"
		of = open(ofilename, "w")
		print(ofilename)
		print(header, file=of)
		print("<title>Bhagavad-gita "+id+"</title>", file=of)
		print(header2, file=of)
		print("<h2>"+id+"</h2>", file=of)
		print("", file=of)
		print(id, file=of)
		print("", file=of)
		continue
	if id != "":
		print(line, file=of)

fileinput.close()

