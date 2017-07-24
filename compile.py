#!/opt/local/bin/python
import re, sys

titleLine = ""
chords = set()
lines = []
availableChords = ["Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G"]

for line in sys.stdin.read().splitlines():
	isChord = False
	isTitleLine = False
	isverseLine = False
	verseLine = ""
	chordLine = ""
	latestChord = ""
	lyricLine = ""
	chordChars = 0
	for char in line:
		if char == '#':
			isTitleLine = True
		elif char == '{':
			isverseLine = True
		elif char == '[':
			isChord = True
			latestChord = ""
			while (chordChars > 0):
				if len(lyricLine.replace("&nbsp;", "").strip()) == 0:
					lyricLine = lyricLine + "&nbsp;"
				else:
					lyricLine = lyricLine + "-"
				chordChars = chordChars - 1
		else:
			if isChord:
				if char == ']':
					isChord = False
					chords.add(latestChord)
				else:
					latestChord = latestChord + char
					chordLine = chordLine + char
					chordChars = chordChars + 1
			elif isverseLine:
				if char != '}':
					verseLine = verseLine + char
			elif isTitleLine:
				titleLine = titleLine + char
			else:
				if (chordChars == 0):
					chordLine = chordLine + "&nbsp;"
				else:
					chordChars = chordChars - 1
				lyricLine = lyricLine + char
	if isverseLine:
		lines.append("[" + verseLine.upper() + "]")
	else:
		lines.append((chordLine, lyricLine))

print("*" + titleLine + "*")
print("Chords: " + ", ".join(sorted(chords)))

for line in lines:
	if type(line) == tuple:
		print("<div class='line'>" + line[0] + "<br/>" + line[1] + "</div>")
	else:
		print(line + "<br/>")
