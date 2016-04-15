#!/usr/bin/python
import sys

resFile = str(sys.argv[1])
# Open a file
fo=open(resFile, "r")
fout=open("Output_clasification", "wr")
lines = fo.readlines()
corr=0
incorr=0
for line in lines:
	lineArr=line.split('\t')
	if (lineArr[0]=='\n'):
		fout.write('\n')
		continue
	
	if (lineArr[-1][:-1]==lineArr[-2]):
		fout.write(lineArr[0]+":\Classified")
		corr+=1
	else:
		incorr+=1
		fout.write(lineArr[0]+":\Misclassified")
# Close opend file
fo.close()
fout.close()

acc = corr*100/(corr+incorr)
print acc
