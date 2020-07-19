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
    model = gensim.models.doc2vec.Doc2Vec(lines, size=300, window=4, min_count=0, workers=4)
#    try:
#        print model.docvecs['0']
#    except:
#        print model.docvecs[0]
    model.save('model.'+lang_tag)
model_generator("data.txt","tel")# -*- coding: utf-8 -*-

