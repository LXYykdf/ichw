#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Liuxinyi"
__pkuid__  = "1800011815"
__email__  = "1800011815@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
	"""count words from lines of text string, then sort by their counts
	in reverse order, output the topn (word count), each in one line. 
	"""
	punctuals=[',','.','?','!','"',"'",'_',\
			'(',')','@',';','--',':','/',' - ','*']
	for i in punctuals:
		lines=lines.replace(i,' ')	#delet the punctuals 

	words=lines.lower().split()		#split the text into words

	
	counts={}

	for k in words:
		if not k.isdigit():
			counts[k]=counts.get(k,0)+1 


	ans=sorted(counts.items(),key=lambda x:x[1],reverse=True)
	if 0<topn<=len(ans):
		newans=ans[0:topn]
	else:
		newans=ans
	
	for result in newans:
		print(result[0]+'\t',result[1])


	return


def main():
	'''
	main function
	'''
	if  len(sys.argv) == 1:
		print('Usage: {} url [topn]'.format(sys.argv[0]))
		print('  url: URL of the txt file to analyze ')
		print(' topn: how many (words count) to output. If not given, will output top 10 words')
		sys.exit(1)
	
	else :
		doc=urlopen(sys.argv[1])
		doc=urlopen(sys.argv[1])
		text=doc.read()
		utext=text.decode('utf8')
		doc.close()

		if  len(sys.argv) == 2:
			wcount(utext)
		if  len(sys.argv) == 3:
			wcount(utext,int(sys.argv[2]))

	return


if __name__ == '__main__':
	main()

	
