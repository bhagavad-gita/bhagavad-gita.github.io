#!/C/Python34/python.exe

import sys
import fileinput

debug = False
debug2 = False
header = ""
for line in open("../sloka-begin-html"):
	header += line

header2 = ""
for line in open("../sloka-begin2-html"):
	header2 += line

footer = ""
for line in open("../sloka-end-html"):
	footer += line

first = True
id = ""
tcanto = sys.argv[1]
canto = int(tcanto)
rawfilename = "SB-Canto-" + tcanto + "-Raw.txt"
rawpathname = "raw/" + rawfilename
raw = open(rawpathname, "r")
print("Canto", canto)
chapter = "0"
for line in raw:
	line = line.strip()	
	if debug2:
		print("LINE[", line, "]")
	if line == "":
		if debug:
			print("SKIP")
		continue

	if "SYNONYMS" in line:
		if debug:
			print("SKIP")
		print("<br>", file=of)
		print("<h2>Synonyms</h2>", file=of)
		continue

	if "PURPORT" in line:
		if debug:
			print("SKIP")
		print("<br>", file=of)
		print("<h2>Purport</h2>", file=of)
		continue

	if "TRANSLATION" in line:
		if debug:
			print("SKIP")
		print("<br>", file=of)
		print("<h2>Translation</h2>", file=of)
		continue

	if line == "TEXT":
		if debug:
			print("SKIP")
		print("<br>", file=of)
		print("<h2>Text</h2>", file=of)
		continue

	if line == "TEXT 1":
		if debug:
			print("NEW CHAPTER BEGINS (TEXT 1)")
		chapter = str(1 + int(chapter))

	if line == "TEXTS 1-":
		if debug:
			print("NEW CHAPTER BEGINS (TEXTS 1.. multiplesloka)")
		chapter = str(1 + int(chapter))

	if "TEXT " in line or "TEXTS " in line:
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
		if debug:
			print(ids[1])
		line = ids[1]
		id = line
		if debug:
			print("DEBUG: id to split is", id)
		verse = str(id)
		if "-" in verse:
			print("VERSE: DEBUG: canto", canto)
			print("VERSE: DEBUG: chapter", chapter)
			print("VERSE: DEBUG: id", str(id))
			print("VERSE: DEBUG: verse", verse)
			vids = verse.split("-")
			startvid = str(vids[0])
			stopvid = str(vids[1])
			print("VERSE: DEBUG: start verse id", startvid)
			print("VERSE: DEBUG: stop  verse id", stopvid)
		else:
			startvid = verse
			stopvid = ""

		if debug:
			print("canto", canto)
			print("chapter", chapter)
			print("verse", verse)
		summary = str(canto) + "." + chapter + "." + verse
		summary0 = str(canto) 
		ofilename = summary + ".html"
		opathname = str(canto) + "/" + ofilename
		ofilename0 = summary0 + ".html"
		of = open(opathname, "w")
		if debug:
			print(opathname)
			# print(opathname)
		print(header, file=of)
		if beginhtml:
			of0 = open(ofilename0, "w")
			print(header, file=of0)
			print("<title>Bhagavad-gita "+chapter+"</title>", file=of0)
		print("<title>Srimadh-bhagavatam "+summary+"</title>", file=of)
		print(header2, file=of)
		if beginhtml:
			print(header2, file=of0)
			beginhtml = False
		print("<br>", file=of)
		print("<br>", file=of0)
		print("<h2><a href=\"http://bhagavad-gita.today/sb/"+str(chapter)+"\">"+chapter+"</a>."+verse+"</h2>", file=of)
		print("<h2><a href=\"http://bhagavad-gita.today/sb/"+str(chapter)+"\">"+chapter+"</a>."+verse+"</h2>", file=of0)
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
		if debug2:
			print(str(canto)+"."+chapter+"."+verse, line)
		print(line, file=of)
		print(line, file=of0)

fileinput.close()

# print(footer, file=of0)
# of0.close()
