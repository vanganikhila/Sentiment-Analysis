# -*- coding: utf-8 -*-

import gensim
import logging
import codecs
import sys

class LabeledLineSentence(object):
    def __init__(self, filename):
        self.filename = filename
    def __iter__(self):
        for lid, line in enumerate(codecs.open(self.filename,encoding='utf-8')):
            yield gensim.models.doc2vec.LabeledSentence(words=line.split(), tags=[lid])

def model_generator(filename,lang_tag):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    #textfile = codecs.open(filename,encoding='utf-8')
    lines = LabeledLineSentence(filename)
#    for line in lines:
#    	print line
    model11 = gensim.models.doc2vec.Doc2Vec(lines, size=300, window=4, min_count=0, workers=4)
#    try:
#        print model.docvecs['0']
#    except:
#        print model.docvecs[0]
    model11.save('model11.'+lang_tag)
model_generator("tdata.txt","tel")# -*- coding: utf-8 -*-

'''vector.py'''
import numpy

def vectorize(lang_tag,filename):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model11 = gensim.models.doc2vec.Doc2Vec.load('model11.'+lang_tag)
    #print ("The model is loaded.")
    data_file = codecs.open(filename,'rb',encoding='utf-8')
    #print ("Reading the data file is done.")

    word_vector_file = codecs.open("onlyVectors11.txt",'wb',encoding='utf-8')
    done,count = [],0
    unsolved_default_vector = numpy.array([0 for i in range(0,200)])
    #print ("Starting the vectorization.")
    for uid,line in enumerate(data_file):
        try:
            word_vector_file.write(str(model11.docvecs[uid])+'\n')
        except:
            count+=1
            word_vector_file.write(str(unsolved_default_vector)+'\n')

    #print (count)
    word_vector_file.close()

if __name__ == '__main__':
    vectorize("tel","tdata.txt")
# -*- coding: utf-8 -*-

'''vec2CF.py'''
# -*- coding: utf-8 -*-


fo = codecs.open("onlyVectors11.txt","r",encoding="utf-8")
fo1= codecs.open("trainedVectors11.txt","w",encoding="utf-8")
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

'''naiveout.py'''
# -*- coding: utf-8 -*-
from sklearn.naive_bayes import GaussianNB
text_file2 = open("tags.txt", "r")
trainTags1 = text_file2.readlines()

text_file4 = open("ttags.txt", "r")
testTags1 = text_file4.readlines()

testTags = []
for item in testTags1:
    testTags.append(int(item))
'''print(testTags)'''

trainTags = []
for item in trainTags1:
    trainTags.append(int(item))

c = open("trainedVectors11.txt", 'r')
testData = [line.split(',') for line in c.readlines()]

cr = open("trainedVectors.txt", 'r')
trainData = [line.split(',') for line in cr.readlines()]

for i in range(len(testData)):
    for j in range(len(testData[i])):
         testData[i][j]=float(testData[i][j])
         
for i in range(len(trainData)):
    for j in range(len(trainData[i])):
         trainData[i][j]=float(trainData[i][j])

nb = GaussianNB()
model = nb.fit(trainData,trainTags)
output = model.predict(testData)
print("polarity of the song is")
print(output)
'''
c=0
#for (i,j) in [(i,j) for i in range(testTags) for j in range(output)]
for i in range(0,len(testTags)):
  if testTags[i]==output[i]:
      c=c+1
print("accuracy is ",(c*100)/len(testTags),"%")      
'''
    
#accuracy = (sum(output==testTags)/len(testTags))*100;

