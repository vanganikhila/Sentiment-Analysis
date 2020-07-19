# -*- coding: utf-8 -*-

import codecs
fo = codecs.open("onlyVectors.txt","r",encoding="utf-8")
fo1= codecs.open("trainedVectors.txt","w",encoding="utf-8")
currLine = ""
for line in fo:

	if "[" in line:
		words = line.split()
		if words[0]=="[":
			words = words[1:]
		else:
			words[0]=words[0][1:]
		for word in words:
			currLine += word + ","
	elif "]" in line:
		words = line.split()
		if words[len(words)-1]=="]":
			words=words[:-1]
		else:
			words[len(words)-1]=words[len(words)-1][:-1]
		for word in words:
			currLine += word + ","
		currLine = currLine[:-1]
		fo1.write(currLine+u"\n")
		currLine=""
	else:
		words=line.split()
		for word in words:
			currLine+= word+","


fo1.close()
fo.close()