#!/usr/bin/python
import sys

resFile = str(sys.argv[1])
# Open a file
fo=open(resFile, "rw+")
lines = fo.readlines()
corr=0
incorr=0
c=0
i=0
space=' '
fout=open("../Output/output"+str(sys.argv[2]), "wa")
sent=""
for line in lines:
	lineArr=line.split('\t')
	sent+=space+lineArr[0]
	if (lineArr[0]=='\n'):
		if(c>=i):
#print "Classified:    \t {0}\n".format(sent)
			fout.write("Classified:    \t {0}\n".format(sent))
			corr+=1
		else:
#print "Misclassified: \t {0}\n".format(sent)
			fout.write("Misclassified: \t {0}\n".format(sent))
			incorr+=1
		c=0
		i=0
		sent=""
		continue
	if (lineArr[-1][0]==lineArr[-2]):
		c+=1
	else:
		i+=1
# Close opend file
fo.close()
fout.close()

acc = corr*100/(corr+incorr)
print acc

