# coding: utf-8

import glob
import nltk
from nltk.tag import pos_tag, map_tag
from nltk.tag import SennaChunkTagger
from xml.etree import ElementTree as ET

def getSentences(f):
	l = []
	sentences = ET.parse(f).getroot()
	for sentence in sentences:	
		sen = sentence.find('sentencestring')
		label = sentence.find('contextualindependence')
		l.append((sen.text,label.text))
	return l

def main():

	Sentences = []
	allFiles = glob.glob("../../LDU_identification/*")
	for f in allFiles:
		Sentences += getSentences(f)

	totSent=len(Sentences)
	for a in range(1,6):
		
		ftrain = open("../TrainingFiles/trainFile"+str(a), "wa")
		ftest = open("../TestFiles/testFile"+str(a), "wa")
		k=0 
		for sentC in Sentences:
			k+=1
			sent = sentC[0].encode('ascii', 'ignore').decode('ascii')
			t = nltk.word_tokenize(sent);
			posTagged = pos_tag(t)
			sent = sent.split()
			chktagger = SennaChunkTagger('../../senna')
			tagged_sent = chktagger.tag(sent)
			l = len(posTagged)
			j=-1
			for i in range(l):
				if (len(posTagged[i][0])<=1):
					continue
				else:
					bio = tagged_sent[j][1]
				
				if ( k > ((a-1)*(totSent/5)) and k < ((a*totSent)/5) ):
					ftest.write('{0}\t{1}\t{2}\t{3}\n'.format(posTagged[i][0], posTagged[i][1], bio, sentC[1]))
				else:
					ftrain.write('{0}\t{1}\t{2}\t{3}\n'.format(posTagged[i][0], posTagged[i][1], bio, sentC[1]))
				
			if ( k > ((a-1)*(totSent/5)) and k < ((a*totSent)/5) ):
				ftest.write('\n')
			else:
				ftrain.write('\n')

		ftrain.close()
		ftest.close()
		print a,"Fold completed"

main()
