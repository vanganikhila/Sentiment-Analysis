import gensim
import numpy
import codecs
import logging
import sys

def vectorize(lang_tag,filename):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = gensim.models.doc2vec.Doc2Vec.load('model.'+lang_tag)
    print ("The model is loaded.")
    data_file = codecs.open(filename,'rb',encoding='utf-8')
    print ("Reading the data file is done.")

    word_vector_file = codecs.open("onlyVectors.txt",'wb',encoding='utf-8')
    done,count = [],0
    unsolved_default_vector = numpy.array([0 for i in range(0,200)])
    print ("Starting the vectorization.")
    for uid,line in enumerate(data_file):
        try:
            word_vector_file.write(str(model.docvecs[uid])+'\n')
        except:
            count+=1
            word_vector_file.write(str(unsolved_default_vector)+'\n')

    print (count)
    word_vector_file.close()

if __name__ == '__main__':
    vectorize("tel","data.txt")
# -*- coding: utf-8 -*-

