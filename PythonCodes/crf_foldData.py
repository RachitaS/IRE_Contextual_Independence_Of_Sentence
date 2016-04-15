# coding: utf-8
import sys
import glob
from xml.etree import ElementTree as ET
import nltk
from nltk.tag import pos_tag, map_tag, StanfordNERTagger

ld = ['i','at','by','he','she','they','so','because','since','therefore','hence','but','whether','although','them','his','her','their','there','despite','however','further']
st = StanfordNERTagger('stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
								   'stanford-ner/stanford-ner.jar',encoding='utf-8')
#Coordinating conjunctions
def calcF1(sen):
	t = nltk.word_tokenize(sen);
	posTagged = pos_tag(t)
	ccNum=0
	for i in posTagged:
		if (i[1]=='CC'):
			ccNum += 1
	return ccNum

#First window terms
def calcF2(sen):	
	global ld
	t = nltk.word_tokenize(sen);
	if (len(t)<4):
		t += ['.','.','.','.']
	l = pos_tag(t)
	words = [t[0], t[1], t[2], t[3]]
	tags = [l[0][1], l[1][1], l[2][1], l[3][1]]
	if (words[0] in ld or words[1] in ld or words[2] in ld or words[3] in ld):
		return 0
	'''
	if (t[0]=='the' and l[1][1]=='NN'):
		return 1
	if ('WDT' in tags or 'WP' in tags or 'WP$' in tags or 'WRB' in tags):
		return 0
	'''
	return 1

#PronounsCount
def calcF3(sen):
	t = nltk.word_tokenize(sen);
	posTagged = pos_tag(t)
	prpNum=0
	for i in posTagged:
		if (i[1]=="PRP" or i[1]=="PRP$"):
			prpNum += 1
	return prpNum

#WhCount
def calcF4(sen):
	t = nltk.word_tokenize(sen);
	posTagged = pos_tag(t)
	whNum=0
	for i in posTagged:
		if (i[1] in ['WDT','WP','WP$','WRB']):
			whNum += 1
	return whNum

#NEcount
def calcF5(sen):
	global st
	t = nltk.word_tokenize(sen);
	ct = st.tag(t)
	cnt=0
	for i in ct:
		if i[1]!='O':
			cnt +=1
	return cnt

def getSentences(f):
	l = []
	sentences = ET.parse(f).getroot()
	for sentence in sentences:	
		sen = sentence.find('sentencestring')
		label = sentence.find('contextualindependence')
		l.append((sen.text,label.text))
	return l

print "Generating {0} file\n\n".format(sys.argv[1])
fp = open('training_final.txt','w')
ftr = open('training_sentences','w')
fte = open('testing_sentences','w')
#fp.write("f1,f2,f3,f4,f5,isIndependent\n")
i=0
Sentences = []
allFiles = glob.glob("./LDU_identification/*")
for f in allFiles:
	Sentences = getSentences(f)
	for s in Sentences:
		i += 1
		sen1 = s[0].encode('ascii', 'ignore').decode('ascii')
		sen = sen1.lower()
		f1 = calcF1(sen)
		f2 = calcF2(sen)
		f3 = calcF3(sen)
		f4 = calcF4(sen)
		f5 = calcF5(sen)
		c = "d"
		if (s[1]=='1'):
			c = "\"yes\""
		else:
			c = "\"no\""

		fp.write('s{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(i,f1,f2,f3,f4,f5,c))
		if (str(sys.argv[1])=="test"):
			fte.write('s{0}:\t{1}\n'.format(i,sen1))
		else:
			ftr.write('s{0}:\t{1}\n'.format(i,sen1))

	fp.write("\n")
	print "One folder written"
fp.close()
ftr.close()
fte.close()
