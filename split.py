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
		if id == "":
			beginhtml = True
		if id != "":
			print("</p>", file=of)
			print("</p>", file=of0)
			print("", file=of)
			print("", file=of0)
			print(footer, file=of)
			first = False
			of.close()
		ids = line.split()
		# print(ids[1])
		line = ids[1]
		id = line
		(chapter, verse) = id.split('.')
		print("chapter", chapter)
		print("verse", verse)
		ofilename = id + ".html"
		ofilename0 = chapter + ".html"
		of = open(ofilename, "w")
		print(ofilename)
		print(ofilename0)
		print(header, file=of)
		if beginhtml:
			of0 = open(ofilename0, "w")
			print(header, file=of0)
			print("<title>Bhagavad-gita "+chapter+"</title>", file=of0)
		print("<title>Bhagavad-gita "+id+"</title>", file=of)
		print(header2, file=of)
		if beginhtml:
			print(header2, file=of0)
			beginhtml = False
		print("<br>", file=of)
		print("<br>", file=of0)
		print("<h2><a href=\"http://bhagavad-gita.today/"+chapter+"\">"+chapter+"</a>."+verse+"</h2>", file=of)
		print("<h2><a href=\"http://bhagavad-gita.today/"+chapter+"\">"+chapter+"</a>."+verse+"</h2>", file=of0)
		print("", file=of)
		print("", file=of0)
		print("<p>", file=of)
		print("<p>", file=of0)

		print("<a href=\"http://bhagavad-gita.today/"+id+"\"><b>"+id+"</b></a>", file=of)
		print("<a href=\"http://bhagavad-gita.today/"+id+"\"><b>"+id+"</b></a>", file=of0)
		print("", file=of)
		print("", file=of0)
		continue
	if id != "":
		print(line, file=of)
		print(line, file=of0)

fileinput.close()

print(footer, file=of0)
of0.close()
